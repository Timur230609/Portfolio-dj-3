from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home-page'),
    path('contact/', views.contact_view, name='contact'),
    path('contact.html', views.contact_view),  
    path('index.html', views.home_view), 
    path('about.html',views.about_view,name='about-page'),
    path('project.html', views.project_view, name='project'),
    path('service.html',views.service_view,name='service-page'),
    path('team.html',views.team_view,name='team-page'),
    path('testimonial.html',views.test_view,name='test-page'),
    path('lol404.html',views.lol404_view,name='lol404-page'),
    path('admin/', admin.site.urls),
    ]
