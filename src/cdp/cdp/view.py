from django import forms
from django .http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    my_title = "helooooo..............."
    context = {"title":my_title, "my_list" : [1,2,3,4,5]}
    return render (request, "home.html",context)

def about_us(request):
    my_title = "About us.."
    return render (request, "about.html",{"title": my_title})

def content(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    context = {
        "title": "Contact Us",
        "form": form
    }
    return render (request, "form.html",context)