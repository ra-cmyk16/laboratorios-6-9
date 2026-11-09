from django.http import HttpResponse
from django.shortcuts import render
from .models import Resource


def home(request):
    context = {
        "welcome_message": "Explore learning resources and project ideas.",
    }
    return render(request, "pages/home.html", context)


def resources(request):
    context = {
        "resources": Resource.objects.select_related("category").all(),
    }
    return render(request, "pages/resources.html", context)


def about(request):
    context = {
        "purpose": "Practice URL routing, views, and templates.",
    }
    return render(request, "pages/about.html", context)

def faq(request):
    return render(request, "pages/faq.html")    

def contact(request):
    return HttpResponse("Contact information")

def topic_detail(request, slug):
    return HttpResponse(f"Requested topic: {slug}")

def available_resources(request):
    context = {
        "resources": Resource.objects.filter(available=True).select_related("category"),
    }
    return render(request, "pages/resources.html", context)