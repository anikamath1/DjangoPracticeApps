from django.shortcuts import render, HttpResponse, redirect
#from tutorial import views
#from tutorial import *
def login_redirect(request):
    return redirect('accounts/login')
