from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Sport, SportBlog, Player, UserProfile, UserComments
from .forms import UserProfileForm

class IndexView(View):
    def get(self, request):
        sports_list = Sport.objects.all()
        blog_list = SportBlog.objects.order_by('date_published')[:4]
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
 
# @login_required
# def like_category(request):
#     sports_id = None
#     if request.method == 'GET':
#         sports_id = request.GET.get('sports_id')
#         likes=0
#         if sports_id:
#             sports = Sport.objects.get(id=int(sports_id))
#             if sports:
#                 likes = sports.likes + 1
#                 sports.likes = likes
#                 sports.save()
#     return HttpResponse(likes)

@login_required
def register_profile(request):
    form = UserProfileForm()
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            
            return redirect("/")
        else:
            print(form.errors)
    
    context_dict = {'form': form}
    return render(request, 'sportsApp/profile_registration.html', context_dict)

class ProfileView(View):
    def get_user_details(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        
        user_profile = UserProfile.objects.get_or_create(user=user)[0]
        form = UserProfileForm({
                                'picture': user_profile.picture,
                                'message': user_profile.message
                            })
        
        return (user, user_profile, form)
    
    @method_decorator(login_required)
    def get(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect("/")
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'sportsApp/profile.html', context_dict)
    
    @method_decorator(login_required)
    def post(self, request, username):
        try:
            (user, user_profile, form) = self.get_user_details(username)
        except TypeError:
            return redirect("/")
        
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if form.is_valid():
            form.save(commit=True)
            return redirect("/")
        else:
            print(form.errors)
        
        context_dict = {'user_profile': user_profile,
                        'selected_user': user,
                        'form': form}
        
        return render(request, 'sportsApp/profile.html', context_dict)
        
class ListProfileView(generic.ListView):
  model = UserProfile
  template_name = 'sportsApp/list_profiles.html'
  context_object_name = 'userprofile_list'