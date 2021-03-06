"""todoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from .views import HomeRedirectView
from django.urls import include, path
from .views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    # ToDo: Home 화면 만들기
    path('', HomeRedirectView.as_view()),
    path('todo/', include('workmanagement.urls')),
    # 장고의 인증 URLconf를 가져와서 사용함
    path('accounts/', include('django.contrib.auth.urls')),
    # 계정 생성(가입) 처리를 하는 URL
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done', UserCreateDoneTV.as_view(), name='register_done'),
]
