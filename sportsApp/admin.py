from django.contrib import admin
from .models import Sport, SportBlog, Player, UserProfile, UserComments

# Register your models here.
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}

admin.site.register(Sport, SportAdmin)

class SportBlogAdmin(admin.ModelAdmin):
    list_display= (
        'title', 'url', 'views', 'sport', 
        'picture', 'date_published', 'summary',
    )
    search_fields = ('title',)
    prepopulated_fields = {
        'slug': ("title",),
    }
    autocomplete_fields = ('sport',)

admin.site.register(SportBlog, SportBlogAdmin)
admin.site.register(Player)
admin.site.register(UserProfile)
admin.site.register(UserComments)
