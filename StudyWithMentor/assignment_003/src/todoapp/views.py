from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# login_required() 함수를 임포트합니다. 데코레이터로 사용되는 함수로, 일반 함수에 적용합니다.
# 기능은 사용자가 로그인했는지를 확인해 로그인한 경우는 원래 함수를 실행하고,
# 로그인이 되지 않은 경우는 로그인 페이지로 리다이렉트시킵니다.
from django.contrib.auth.decorators import login_required
from django.views.generic.base import RedirectView

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class HomeRedirectView(RedirectView):
    pattern_name = 'workmanagement:index'


# TODO: 나중에 HomeView 만들어서 프로젝트 소개 작성하기
# class HomeView(TemplateView):
#     template_name = 'home.html'


# login_required()함수는 함수에만 적용할 수 있으므로, 클래스형 뷰에서는
# 이 LoginRequiredMixin 클래스를 상속받아 사용하면 login_required() 데코레이터 기능을 제공할 수 있습니다.
class LoginRequiredMixin:
    # as_view() 메소드를 인스턴스 메소드가 아니라 클래스 메소드로 정의합니다.
    @classmethod
    # as_view() 메소드는 항상 클래스 메소드로 정의해야합니다.
    # super() 메소드에 의해 LoginRequiredMixin의 상위 클래스에 있는 as_view() 메소드가 view 변수에 할당됩니다.
    def as_view(cls, **initkwargs):
        # view 변수, 즉 LoginRequiredMixin의 상위 클래스에 있는 as_view() 메소드에
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        # login_required() 기능을 적용하고 그 결과를 반환합니다.
        return login_required(view)

    # 위 소스는 파이썬의 다중 상속 문법을 이해해야 정확히 파악할 수 있습니다.
    # 간단히 정리하면 LoginRequiredMixin 클래스를 상속받는 클래스의 as_view() 메소드를 호출하면,
    # 다중 상속 구조의 메소드를 호출하는 순서에 의해 View 클래스의 as_view() 메소드에 login_required() 기능이 적용됩니다.

    # 클래스형 뷰에 데코레이터 적용 방법
    # 원래 데코레이터 기능은 함수에 적용되어 그 함수의 기능을 확장하는 역할을 합니다.
    # 만일 클래스에 데코레이터 기능을 적용하려면 약간의 추가 작업을 해야 합니다.
    # 앞에서 설명한 LoginRequiredMixin 클래스를 사용해 상속 방식으로 데코레이터 기능을 적용할 수 있습니다.
    # 그 외에도 URLconf 정의에 데코레이터 함수를 적용하는 방법과 dispatch() 메소드에 데코레이터 함수를 적용하는 방법이 있습니다.


# User Creation
class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')


class UserCreateDoneTV(TemplateView):
    template_name = 'registration/register_done.html'
