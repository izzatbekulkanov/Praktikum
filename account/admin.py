from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'data_of_birth')
admin.site.register(Profile, ProfileAdmin)
