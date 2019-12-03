from django.conf.urls import url
from django.urls import path,re_path
from django.contrib.auth.views import LoginView,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import logout
from shopping import views

urlpatterns = [
    url(r'^$',views.shopping,name='shopping'),
]
