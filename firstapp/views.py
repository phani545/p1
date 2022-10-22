from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.

def home(request):
    post = Blog.objects.all()
    
    return render(request, "basic.html",{"name" : "Phani Deep Challa", "post":post})
    #return HttpResponse("This is my first app sfgh")
def demo(request):
    #return HttpResponse("WELCOME Djangodgghgh")
    return render(request, "demo.html",{"age":33})