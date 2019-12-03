from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from accounts.forms import RegistrationForm
from accounts.forms import EditProfileForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
# def home(request):
#     return HttpResponse('HELLO')

def home(request):
    names=['anirudh','abc','rohan','def','ghi']
    array=[1,2,3,4,5,5,6,6,7,78,8,9,98,87,6,5,432,1,11,2,3,3,3]
    args={'myname':names,'numbers':array}
    return render(request,'accounts/login.html',args)

def logout_view(request):
        logout(request)
        return render(request,'accounts/logout.html')


def after_log_in(request):
        return render(request,'accounts/login_done.html')

def register(request):
        if(request.method=='POST'):
            form=RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/accounts/login')
        else:
            form=RegistrationForm()
            args = {'form':form}
            return render(request,'accounts/register.html',args)

def profile(request,pk=None):
    if pk:
        user=User.objects.get(pk=pk)
    else:
        user=request.user
    args={'user':user}
    return render(request,'accounts/profile.html',args)


def edit_profile(request):
    if(request.method=='POST'):
        form=EditProfileForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/editprofile.html',args)



def change_password(request):
    if(request.method=='POST'):
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
        else:
            return redirect('/accounts/change_password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/editprofile.html',args)
