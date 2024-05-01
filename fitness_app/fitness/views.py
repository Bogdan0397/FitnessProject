from django.shortcuts import render

def home(request):
    return render(request,'fitness/home.html')


def about(request):
    return render(request,'fitness/about.html')

def contact(request):
    return render(request,'fitness/contact.html')

