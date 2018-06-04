from django.shortcuts import render, redirect

# Create your views here.

def website(request):
    return render(request, 'Website/home.html')
