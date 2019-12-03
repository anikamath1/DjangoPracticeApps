from django.conf.urls import url
from . import views
from django.urls import path,re_path
from django.contrib.auth.views import LoginView,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
from django.contrib.auth import logout

#app_name="accounts"
urlpatterns = [
    re_path(r'^$', views.home),
    #re_path(r'register/', views.register),
    re_path(r'^logout/$',views.logout_view,name='logout'),
    re_path(r'^login/$',LoginView.as_view(template_name='accounts/login.html')),
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^login_done/$',views.after_log_in),
    re_path(r'^profile/$',views.profile,name='profile'),
    re_path(r'^profile/(?P<pk>\d+)$', views.profile, name='view_profile_with_pk'),
    re_path(r'^editprofile/$',views.edit_profile),
    re_path(r'^change_password/$',views.change_password),
    re_path(r'^reset_password/$',PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='reset_password'),
    re_path(r'^reset_password/done/',PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_done'),
    re_path(r'^reset_password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    re_path(r'^reset_password/complete/$',PasswordResetCompleteView.as_view(),name='password_reset_complete'),


]
