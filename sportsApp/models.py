from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Sport(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Sport, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class SportBlog(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField(blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    blog = models.TextField()
    picture = models.ImageField(upload_to='blog_images', blank=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SportBlog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Player(models.Model):
    name = models.CharField(max_length=20)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    email = models.CharField(max_length=40, blank=True)
    gender = models.CharField(max_length=6)
    profile_summary = models.TextField(blank=True)
    picture = models.ImageField(upload_to='player_image', blank=True)
    booked = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class UserComments(models.Model):
    blog = models.ForeignKey(SportBlog, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date_published = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'user comments'

    def __str__(self):
        return f"{self.comment[:100]}...."

class Like(models.Model):
    user = models.ForeignKey(
        User, 
        related_name='likes', 
        on_delete=models.CASCADE
    )
    blog = models.ForeignKey(
        SportBlog, 
        related_name='likes', 
        on_delete=models.CASCADE
    )  
