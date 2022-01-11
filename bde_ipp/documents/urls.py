from django.urls import path

from . import views

urlpatterns = [
    path('en/rop', views.rop_en, name='rop_en'),
    path('fr/rop', views.rop_fr, name='rop_fr'),
    path('en/statutes', views.statutes_en, name='statutes_en'),
    path('fr/statutes', views.statutes_fr, name='statutes_fr'),
]