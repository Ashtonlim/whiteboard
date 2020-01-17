from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings

from .models import Video, Course
from .forms import q
from django.db.models import Q

from .serializers import VideoSerializer
from rest_framework import generics
from itertools import chain

from .utils import sortVids

def index(request):
    videos = Video.objects.all()
    course = Course.objects.all()
    
    if request.method == 'GET':
        form = q(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            chosen = form['course_filter'].value()
            print(type(chosen))
            if query is not "":
                result_list = []
                for word in query.split():
                    print(word)
                    if chosen != "":
                        videos = Video.objects.filter(
                            Q(course = chosen) & (Q(desc__icontains=word) | Q(title__icontains=word) | Q(subs__icontains=word))
                        )
                    else:
                        videos = Video.objects.filter(
                            Q(desc__icontains=word) | Q(title__icontains=word) | Q(subs__icontains=word)
                        )
                    print(videos)
                    result_list = set(chain(result_list, videos))
                print(result_list)
                videos = result_list
                
                # return HttpResponseRedirect(render(request, 'vidboard/index.html', context))
                # return render(request, 'vidboard/results.html', context)
    else:
        form = q()
    
    context = {
        "vids" : sortVids(videos, course),
        "form" : form
    }

    return render(request, 'vidboard/index.html', context)

def watch(request, video_id):
    video = Video.objects.filter(pk=video_id)
    context = {
        "video" : video,
    }
    return render(request, 'vidboard/watch.html', context)


# def search(request):
#     form = q(request.GET)
#     if form.is_valid():
#         query = form.cleaned_data['q']
#     video = Video.objects.filter(pk=query)
#     print(query)
#     context = {
#         "video" : video,
#     }
#     return render(request, 'vidboard/watch.html', context)
class VideoListCreate(generics.ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer