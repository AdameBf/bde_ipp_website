from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.urls import path
from .models import Buddy, Buddlunteer
from django.contrib import admin
from django.shortcuts import render

# Register your models here.


class CustomAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super(CustomAdminSite, self).get_urls()
        custom_urls = [
            path('admin/buddy_matching', self.admin_view(self.buddy_matching_view), name="buddy_matching")
        ]
        return urls + custom_urls

    def buddy_matching_view(self, request):
        return render(request, 'admin/action_pages/buddy_buddlunteer_matching.html')

custom_admin = CustomAdminSite()
custom_admin.register(Buddy)
custom_admin.register(Buddlunteer)

# Default model

custom_admin.register(Group, GroupAdmin)
custom_admin.register(User, UserAdmin)

# admin.site.register(Buddy)
# admin.site.register(Buddlunteer)
