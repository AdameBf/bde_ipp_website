from django.urls import path

from . import views

urlpatterns = [
    path('buddlunteer/register', views.buddlunteers_form_view, name='buddlunteer_form'),
    path('buddy/register', views.buddy_form_view, name='buddy_form'),
    path('', views.choice_page, name='choice_page'),
]
