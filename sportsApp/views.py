from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Sport, SportBlog, Player, UserProfile, UserComment, UpComingEvent
from .forms import UserProfileForm, UserCommentForm

class IndexView(View):
    def get(self, request):
        sports_list = Sport.objects.all()[:6]
        other_sports = Sport.objects.all()[6:12]
        blog_list = SportBlog.objects.order_by('date_published')[:2]
        second_blog = SportBlog.objects.order_by('date_published')[2:4]
        player_list = Player.objects.all()[:2]
        event_list = UpComingEvent.objects.order_by('date')
        context_dict = {
            'sports_list': sports_list, 
            'blog_list': blog_list,
            'second_blog': second_blog,
            'other_sports': other_sports,
            'player_list': player_list,
            'event_list': event_list,     
            }
        return render(request, 'sportsApp/index.html', context_dict)

class AboutView(View):
    def get(self,request):
        return render(request, 'sportsApp/about.html', {})

class SportsView(View):
    def get(self,request, sports_slug):
        """Navigate to each sport"""
        context_dict = {}
        sport = get_object_or_404(Sport, slug=sports_slug)
        blogs = sport.sportblog_set.order_by('date_published')
        context_dict['sport'] = sport
        context_dict['blogs'] = blogs
        return render(request, 'sportsApp/sports.html', context_dict)
 
@login_required
def like_sport(request):
    sportid = None
    if request.method == 'GET':
        sportid = request.GET.get('sport_id')
        likes=0
        if sportid:
            sport = Sport.objects.get(id=int(sportid))
            if sport:
                likes = sport.likes + 1
                sport.likes = likes
                sport.save()
                return HttpResponse(likes)

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

def add_comment(request, blog_slug):
    blog = get_object_or_404(SportBlog, slug=blog_slug)
    blog.views += 1
    blog.save()
    user_comments = blog.usercomment_set.order_by('date_published')
    if request.method != 'POST':
        form = UserCommentForm()
    else:
        form = UserCommentForm(data=request.POST)
    if form.is_valid():
        if blog:
            new_comment = form.save(commit=False)
            new_comment.blog = blog
            new_comment.owner = request.user
            new_comment.save()
            return redirect("sportsApp:index")
    else:
        print(form.errors)

    context_dict = {'form': form, 'blog': blog, 'user_comments': user_comments}
    return render(request, 'sportsApp/add_comment.html', context_dict)

def edit_comment(request, item_id):
    comment = get_object_or_404(UserComment, id=item_id)
    blog = comment.blog

    if comment.owner != request.user:
        raise Http404
    else:
        form = UserCommentForm(instance=comment)

    if request.method == 'POST':
        form = UserCommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("sportsApp:index")
    context_dict = {'form': form, 'blog': blog, 'comment': comment}
    return render(request, "sportsApp/edit_comment.html", context_dict)

def search_blog(request):
    search_text = request.GET['query']
    blogs = SportBlog.objects.filter(title__contains=search_text)
    context_dict = {'blogs': blogs}
    return render(request, 'sportsApp/search.html', context_dict)

def contact_us(request):
    return render(request, 'sportsApp/contact-us.html', {})