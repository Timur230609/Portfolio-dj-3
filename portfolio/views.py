from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import Contact



def home_view(request):
    return render(request, 'index.html')

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            new_contact = Contact(name=name, email=email, content=content)
            new_contact.save()
            messages.success(request, "Your message was successfully sent!")
            return redirect('home-page')  # Bu yerda HttpResponseRedirect o'rniga redirect() ishlatilmoqda
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('contact')
    
    return render(request, 'contact.html')



def project_view(request):

    return render(request, 'project.html')

def about_view(request):
    return render(request,'about.html')

def service_view(request):
    return render(request,'service.html')

def team_view(request):
    return render(request,'team.html')


def test_view(request):
    return render(request,'testimonial.html')


def lol404_view(request):
    return render(request,'lol404.html')
