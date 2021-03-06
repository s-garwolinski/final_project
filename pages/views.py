from django.shortcuts import render
from django.http import HttpResponse
# Create your views here

def home_view(request, *args, **kwargs):
    print(f"args = {args}, kwargs = {kwargs}, request = {request}")
    print('request.user:', request.user)    # shows who is requesting
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

def about_view(request, *args, **kwargs):
    return render(request, 'about.html', {})

def social_view(request, *args, **kwargs):
    return render(request, 'social.html', {})