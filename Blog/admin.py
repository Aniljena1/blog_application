from django.contrib import admin
from .models import post

class postAdmin(admin.ModelAdmin):
    list_display = ['title','content','date_posted','author']
admin.site.register(post,postAdmin)
