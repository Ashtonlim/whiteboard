from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings
from .models import Video

def index(request):
    videos = Video.objects.all()
    context = {
        "videos" : videos,
        "course" : videos[0].course,
        "courseCode" : videos[0].courseCode,
    }
    return render(request, 'vidboard/index.html', context)

def watch(request, video_id):
    video = Video.objects.filter(pk=video_id)
    context = {
        "video" : video,
    }
    return render(request, 'vidboard/watch.html', context)