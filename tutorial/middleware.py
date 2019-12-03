from django.conf import settings
from django.shortcuts import redirect
import re
from django.urls import reverse
from django.contrib.auth import logout
EXEMPT_URL=[re.compile(settings.LOGIN_URL.lstrip("/"))]
if hasattr(settings,'LOGIN_EXEMPT_URLS'):
    EXEMPT_URL+=[re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class LoginRequiredMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        return response

    def process_view(self,request,view_func,view_args,view_kwargs):
        assert hasattr(request,'user')
        path = request.path_info.lstrip('/')
        url_is_exempt=any(url.match(path)for url in EXEMPT_URL)
        print(path)
        if path == reverse('logout').lstrip("/"):
            logout(request)
        elif request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)
