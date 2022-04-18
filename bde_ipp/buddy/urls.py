from django.urls import path

from . import views

urlpatterns = [
    path('buddlunteer/register', views.buddlunteers_form, name='buddlunteers_form'),
    path('buddy/register', views.buddy_form, name='buddy_form'),
    path('', views.choice_page, name='choice_page'),
]
