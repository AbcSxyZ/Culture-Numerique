from django.shortcuts import render

# Create your views here.

def articles_home(request):
    return render(request, "articles/homepage.html")
