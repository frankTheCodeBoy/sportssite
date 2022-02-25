from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, UserComment

class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(required=False)
    fav_sport = forms.CharField(
        max_length=20,
        help_text="what's the name of your favourite sport?",
        required=False)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'cols':25, 'rows': 15}), 
        required=False
    )

    class Meta:
        model = UserProfile
        fields = ('picture', 'fav_sport' , 'message',)

class UserCommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={'cols':15, 'rows':3}),
        required=False
    )

    class Meta:
        model = UserComment
        exclude = ('blog', 'owner')
