from django.views.generic import TemplateView
from sqlalchemy.sql.functions import current_user

from home.forms import HomeForm, ChatForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import Post, Friend,Chat


class HomeView(TemplateView):
    template_name='home/home.html'

    def get(self,request):
        form=HomeForm()
        post=Post.objects.all().order_by('-created')
        users=User.objects.exclude(id=request.user.id)
        friend=Friend.objects.get(current_user=request.user)
        friends=friend.users.all()
        args={'post':post,'form':form,'users':users, \
              'friends':friends}
        return render(request,self.template_name,args)


    def post(self,request):
        form=HomeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            text=form.cleaned_data['post']
            form=HomeForm()
        args={'form':form,'text':text}
        return render(request,'home/afterdone.html',args)

def change_friends(request,operation,pk):
    new_friend=User.objects.get(pk=pk)
    if(operation=='add'):
        Friend.make_friend(request.user,new_friend)
    elif(operation=='remove'):
        Friend.remove_friend(request.user,new_friend)
    return redirect('home')


class ChatView(TemplateView):

    template_name='home/chat.html'

    def get(self,request,pk):
        form=ChatForm()
        messages=Chat.objects.filter(from_user=User.objects.get(id=pk)).values('message')
        print(messages.values('message'))
        user=request.user
        args={'messages':messages,'form':form,'user':user}
        return render(request,self.template_name,args)


    def post(self,request,pk):
        form=ChatForm(request.POST)
        text=form['Sendmessage'].value()
        x=request.user
        y=User.objects.get(id=pk)
        obj=Chat.objects.create(from_user=x, to_user=y,  message=text)
        obj.save()
        print("------------************---------done")
        return redirect('home')

