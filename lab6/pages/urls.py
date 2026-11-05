from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("resources/", views.resources, name="resources"),
    path("about/", views.about, name="about"),
    path("faq/", views.faq, name="faq"),
    path("contact/", views.contact, name="contact"),
    path("topics/<slug:slug>/", views.topic_detail, name="topic-detail"),
]