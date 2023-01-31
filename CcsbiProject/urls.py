from django.urls import path
from CcsbiProject import views

urlpatterns = [
    path('', views.CcsbiProject, name='index'),
    path('home', views.CcsbiProject, name='index'),
    path('contact', views.contact, name='contact'),
    path('projects', views.project, name='project'),
    path('Networks', views.Networks, name='Networks'),
    path('Datasets', views.Datasets, name='Datasets'),
    path('Resources', views.Resources, name='Resources'),
    path('Capacity', views.Capacity, name='Capacity'),
    path('Events', views.Events, name='Events'),  
    path('Opportunities', views.Opportunities, name='Opportunities'),
    path('Event1', views.Event1, name='Event1'), 
    





]