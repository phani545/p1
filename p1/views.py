from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is first project sdfd")
def demo(request):
    return HttpResponse("WELCOME Djangoaaaaa")