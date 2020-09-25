from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def mapview(request):
    return render(request, 'mapview.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')