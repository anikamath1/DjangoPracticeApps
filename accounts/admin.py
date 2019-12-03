from django.contrib import admin
from accounts.models import UserProfile
from django.db import models

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','city','website','phone')

    def user_info(self,obj):
        return obj.description
    user_info.short_description='INFOOO'


    def get_queryset(self,request):
        queryset=super(UserProfileAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-phone','user')
        return queryset


admin.site.register(UserProfile,UserProfileAdmin)
