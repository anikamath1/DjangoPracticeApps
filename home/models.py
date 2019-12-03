from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

class Friend(models.Model):
    users=models.ManyToManyField(User)
    current_user=models.ForeignKey(User,related_name='owner',on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls,current_user,new_friend):
        friend, created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)



class Chat(models.Model):
    from_user=models.ForeignKey(User,related_name='from_user',on_delete=models.CASCADE)
    to_user=models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    message=models.CharField(max_length=200)
