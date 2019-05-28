# Django registration with confirmation email
확인 메일을 통한 Django 회원가입

# Facts
회원 가입 시 이메일을 통한 본인 인증 기능을 따라했다.

# Feelings
'email과 관련된 기능이 어떤 것이 있을까?' 생각하다가 회원 가입 시 '이메일을 통한 본인 인증'이 생각나서 구현해봐야 겠다는 생각이 들었다.

# Findings
'어떻게 구현해야할까?'를 며칠동안 고민했지만 뭔가 떠오르지 않았다. 어떠한 실마리도 찾지 못해서 결국 구글링을 통해 따라해봤다.

1. 사용자가 회원가입을 하면 User(계정)의 Primary Key(기본키, 동일한 레코드를 식별해주는 키)에 해당하는 token을 생성한다.
1. 계정의 pk와 token을 이용하여, 사용자에게 다음과 같은
`https://www.example.com/account-activate/encoding(userid)/encoding(token)`링크를 클릭할 수 있는 메일을 전송한다.
1. 사용자가 메일 링크를 클릭하여 url에 접속한다.
1. 서버에서 url의 userid와 token를 확인하여 userid-token이 유효하면 계정을 활성화한다.

## 이메일 전송 셋팅 settings.py
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "youremail@gmail.com"
EMAIL_HOST_PASSWORD = "userpassword"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
- 이메일을 전송할 EMAIL_HOST_USER는 '보안 수준이 낮은 앱이 계정에 액세스하도록 허용'되어야 합니다.
[참고링크](https://support.google.com/accounts/answer/6010255?hl=ko)

## 회원가입 시 pk에 해당하는 token 생성
```python
def signup(request):
    """
    회원 가입
    """
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = '당신의 ToDo List 계정을 활성화 하세요.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('회원가입을 마치려면 이메일을 확인해주세요.')
    else:
        form = SignupForm()
    return render(request, 'registration/register.html', {'form': form})
```
- 회원가입 시 비활성 상태로 저장함
- userid에 해당하는 token을 생성함
- render_to_string을 통해 생성된 html을 회원에게 전송함
 
## 토큰 생성
```python
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )


account_activation_token = TokenGenerator()
```
- token 생성은 PasswordResetTokenGenerator를 통해 이뤄진다.
[참고링크](https://github.com/django/django/blob/master/django/contrib/auth/tokens.py)
 
 ## 전송할 이메일 템플릿
```html
{% autoescape off %}
Hi {{ user.username }},
Please click on the link to confirm your registration,
http://{{ domain }}{% url 'activate' uidb64=uid token=token %}
{% endautoescape %}
```
- render_to_string 메소드의 두번째 인자로 전달된 값을 이용하여 템플릿을 렌더링한다.

## 활성화 url 등록
```python
urlpatterns = [
            '''
    path('activate/<str:uidb64>/<str:token>', activate, name='activate'),
            '''
]
```

## 활성화 view 구현
```python
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('확인해주셔서 감사합니다. 회원가입이 완료되었습니다.')
    else:
        return HttpResponse('계정 활성 링크가 유효하지 않습니다.')
```
- `activate/<str:uidb64>/<str:token>`에 접속 시 check_token 메소드를 통해 활성화 할지 여부를 확인한다. 

# Future
- 인증 메일 재전송 구현
- 비밀번호 초기화 구현

# 참고 자료 링크
- [Django registration with confirmation email](https://medium.com/@frfahim/django-registration-with-confirmation-email-bb5da011e4ef)
- [django.contrib.auth.tokens](https://github.com/django/django/blob/master/django/contrib/auth/tokens.py)
- [django email settings](https://docs.djangoproject.com/en/2.2/topics/email/#smtp-backend)
- [Let less secure apps access your account](https://support.google.com/accounts/answer/6010255?hl=ko)