
from home.views import HomeView,ChatView
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',HomeView.as_view(),name='home'),
    url(r'connect/(?P<operation>.+)/(?P<pk>\d+)/$',views.change_friends,name='change_friends'),
    url(r'^chat/(?P<pk>\d+)$', ChatView.as_view(), name='view_chat'),
]
