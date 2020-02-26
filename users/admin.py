from django.contrib import admin
from users.models import profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','image']
admin.site.register(profile,ProfileAdmin)
