"""Defines URL patterns for sportsApp"""
from django.urls import path
from . import views

app_name = "sportsApp"

urlpatterns = [
    path(
        "register_profile/",
        views.register_profile,
        name="register_profile"
    ),
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
    path(
        'profile/<username>/', 
        views.ProfileView.as_view(), 
        name='profile'
    ),
    path(
        'profile/', 
        views.ListProfileView.as_view(), 
        name='list_profiles'
    ),
    path(
        'like/',
        views.like_sport,
        name='like_sport'
    ),
    path(
        'add_comment/<slug:blog_slug>/',
        views.add_comment,
        name='add_comment'
    ),
    path(
        'edit_comment/<int:item_id>/',
        views.edit_comment,
        name='edit_comment',
    ),

]
