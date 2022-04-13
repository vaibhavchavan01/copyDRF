from django.contrib import admin
from .models import User, Movie, MovieArtist, Artist, Genre
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    # list_display = ['firstname', 'lastname', 'email','mobile','is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile')}),
        (_('Personal info'), {'fields': ('firstname', 'lastname')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )
    def net_id(self, obj):
        # print(obj.pk)
        return "RBN%s" % obj.pk
    
    net_id.short_description = "Network Id"

    list_display = ('net_id', 'email', 'firstname', 'lastname', 'is_staff')
    search_fields = ('email', 'firstname', 'lastname')
    ordering = ('email',)
# admin.site.register(get_user_model(), UserAdmin)  

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']  

class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "language", "release", "country", "image"]  

class ArtistAdmin(admin.ModelAdmin):
    list_display = ["name"]

class MovieArtistAdmin(admin.ModelAdmin):
    list_display = ["movie","artist","a_type"]

admin.site.register(Movie,MovieAdmin)
admin.site.register(Artist,ArtistAdmin)
admin.site.register(MovieArtist,MovieArtistAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Genre,GenreAdmin)
