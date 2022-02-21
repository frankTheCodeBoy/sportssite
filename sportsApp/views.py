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

class IndexView(generic.ListView):
    model = Sport
    template_name = 'sportsApp/index.html'
    context_object_name = 'sports_list'

class AboutView(View):
    def get(self,request):
        return render(request, 'sportsApp/about.html', {})
