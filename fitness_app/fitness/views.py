from django.shortcuts import render

def home(request):
    categories = {'cat1':'catchek',
            'cat2':'catchek',
            'cat2':'catchek'}

    return render(request,'fitness/home.html',categories)


def about(request):
    return render(request,'fitness/about.html')

def contact(request):
    return render(request,'fitness/contact.html')

