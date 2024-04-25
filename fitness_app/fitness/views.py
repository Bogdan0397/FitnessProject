from django.shortcuts import render

def home(request):
    categories = {'cat1':'catchek',
            'cat2':'catchek',
            'cat2':'catchek'}

    return render(request,'fitness/home.html',categories)

