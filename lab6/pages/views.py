from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {
        "welcome_message": "Explore learning resources and project ideas.",
    }
    return render(request, "pages/home.html", context)

def resources(request):
    context = {
        "resources": [
            {
                "title": "Python basics",
                "category": "Programming",
                "available": True,
            },
            {
                "title": "Git and GitHub",
                "category": "Collaboration",
                "available": False,
            },
            {
                "title": "Django models",
                "category": "Web development",
                "available": False,
            },
              {
                "title": "HTML and CSS Essentials",
                "category": "Web development",
                "available": True,
            },
            {
                "title": "Introduction to Databases",
                "category": "Data Science",
                "available": False,
            },
        ],
    }
    return render(request, "pages/resources.html", context)

def about(request):
    context = {
        "purpose": "Practice URL routing, views, and templates.",
    }
    return render(request, "pages/about.html    ", context)

def faq(request):
    return render(request, "pages/faq.html")    

def contact(request):
    return HttpResponse("Contact information")

def topic_detail(request, slug):
    return HttpResponse(f"Requested topic: {slug}")