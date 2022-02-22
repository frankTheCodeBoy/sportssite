from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Sport, SportBlog, Player, UserProfile, UserComments, Like

class IndexView(View):
    def get(self, request):
        sports_list = Sport.objects.all()
        blog_list = SportBlog.objects.order_by('date_published')
        context_dict = {'sports_list': sports_list, 'blog_list': blog_list}
        return render(request, 'sportsApp/index.html', context_dict)

class AboutView(View):
    def get(self,request):
        return render(request, 'sportsApp/about.html', {})

class SportsView(View):
    def get(self,request, sports_slug):
        """Navigate to each sport"""
        context_dict = {}
        sports = get_object_or_404(Sport, slug=sports_slug)
        blogs = sports.sportblog_set.order_by('date_published')
        context_dict['sports'] = sports
        context_dict['blogs'] = blogs
        return render(request, 'sportsApp/sports.html', context_dict)
