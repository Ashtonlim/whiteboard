from django.contrib import admin
from .models import Video, Course

# class adminForStall(admin.ModelAdmin):
admin.site.register(Video)
admin.site.register(Course)

