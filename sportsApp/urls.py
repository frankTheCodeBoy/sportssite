"""Defines URL patterns for sportsApp"""
from django.urls import path
from . import views

app_name = "sportsApp"

urlpatterns = [
    path(
        "",
        views.IndexView.as_view(),
        name="index"
    ),
    path(
        "about/",
        views.AboutView.as_view(),
        name="about"
    ),
    path(
        "sports/<slug:sports_slug>/",
        views.SportsView.as_view(),
        name="sports"
    ),
]
