from django.urls import path
from CcsbiProject import views

urlpatterns = [
    path('', views.CcsbiProject, name='index'),
    path('contact', views.contact, name='contact'),
]