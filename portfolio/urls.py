from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('contact/', views.contact_view, name='contact'),
    path('contact.html', views.contact_view),  
    path('index.html', views.home_view), 
    path('about.html',views.about_view),
    path('project.html', views.project_view, name='project'),
    path('service.html',views.service_view),
    path('team.html',views.team_view),
    path('testimonial.html',views.test_view),
    path('lol404.html',views.lol404_view),
    path('admin/', admin.site.urls),
    ]
