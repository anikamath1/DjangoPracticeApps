from django.conf.urls import include
from django.urls import path,re_path
from tutorial import views
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

#import django
app_name="accounts"

"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views
#from tutorial import views

urlpatterns = [
    url(r'^$',views.login_redirect, name="login_redirect"),
    url(r'admin/', admin.site.urls),
    url(r'^home/',include('home.urls')),
    url(r'^accounts/',include('accounts.urls')),
    #url(r'accounts/', include('django.contrib.auth.urls')),
    #url('account/', include('django.contrib.auth.urls')),
    url(r'^account/',include('accounts.urls')),
    url(r'^shop/',include('shopping.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
