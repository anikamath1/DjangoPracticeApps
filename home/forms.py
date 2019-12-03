from django import forms
from home.models import Post,Chat


class HomeForm(forms.ModelForm):
    post=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write post here'
        }


    ))
    class Meta:
        model=Post
        fields=('post',)


class ChatForm(forms.ModelForm):
    Sendmessage=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write message here'
        }


    ))
    class Meta:
        model=Chat
        fields=('Sendmessage','from_user','to_user')
