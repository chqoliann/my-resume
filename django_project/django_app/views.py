from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return redirect('https://www.instagram.com/nar.chqolyann/')
