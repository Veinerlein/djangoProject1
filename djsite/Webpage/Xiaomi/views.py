from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
menu = [
    {"title" : "About web page", "url":"about_us"},
    {"title" :'Add text', "url":"add_text"},
    {"title" :'Feed back', "url":"feed_back"},
    {"title" :'Log in', "url":"log_in"}

]
info = {"pubg":about_me.objects.all(),
        "title1":"About site",
        "menu":menu
}
posts = Smartphones.objects.all()
CONTEXT = {
    "title":"About smartphones",
    'menu': menu,
    "posts": posts
}
def index(request):
    return render(request, "Xiaomi/index.html", {'menu': menu, "title": "General page",})

def smartphone(request):
    return render(request, 'Xiaomi/sm.html', context=CONTEXT )

def add_text(request):
    return render(request,"Xiaomi/about.html", {'menu': menu, "title": "add_text"} )

def feed_back(request):
    return render(request,"Xiaomi/about.html", {'menu': menu, "title": "feed_back"} )

def log_in(request):
    return render(request,"Xiaomi/about.html", {'menu': menu, "title": "log in"} )




def laptop(request, model):
    if int(model) > 8:
        return redirect("home", permanent=True)
    return HttpResponse(f"<h1>Xiaomi Laptop</h1><p>{model}</p>", {'menu': menu, "title": f"Laptop {model} page"})

def pageNotFound(request, exceptions):
    return HttpResponseNotFound("Page not Found")

def about_us(request):
    return render(request, "Xiaomi/about.html", context=info )

def others(request):
    return render(request, "Xiaomi/Others.html", {'menu': menu, "title": "Others",})

def leptops(request):
    return render(request, "Xiaomi/Laptops.html",{'menu': menu, "title": "Laptops",})

