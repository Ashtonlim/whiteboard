from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.conf import settings
from .models import Video, Course
from .serializers import VideoSerializer
from rest_framework import generics
from .forms import q
from django.db.models import Q
from itertools import chain

def sortVids(videos, course):
    catVids = {}
    courseVids = [[] for _ in range(course.count())]
    for vid in videos:
        courseVids[vid.course.id - 1].append({
            "id" : vid.id,
            "courseID" : vid.course.id,
            "title" : vid.title,
            "desc" : vid.desc,
            "video" : vid.video.url,
            "thumbnail" : vid.thumbnail.url,
            "likes" : vid.likes,
            "dislikes" : vid.dislikes,
            "uploadDate" : vid.uploadDate,
        })
    for c in course:
        if len(courseVids[c.id-1]) != 0:
            vids = {i["id"]:i for i in courseVids[c.id-1] if i["courseID"] == c.id}
            catVids[str(c.id)] = {
                "courseName" : c.course,
                "courseCode" : c.courseCode,
                "ve" : vids
            }
    return catVids

def index(request):
    videos = Video.objects.all()
    course = Course.objects.all()
    # courses = Video.objects.values_list('course', flat=True).distinct()
    # print(videos[0])
    context = {
        # "videos" : videos,
        "vids" : sortVids(videos, course),
        # "form" : form
    }

    if request.method == 'GET':
        form = q(request.GET)
        if form.is_valid():
            query = form.cleaned_data['q']
            if query is not "":
                # vids
                result_list = []
                for word in query.split():
                    print(word)
                    videos = Video.objects.filter(
                        Q(pk__icontains=word) |
                        Q(title__icontains=word) |
                        Q(subs__icontains=word)
                    )
                    print(videos)
                    result_list = set(chain(result_list, videos))
                print(result_list)
                context["vids"] = sortVids(result_list, course)
                context["form"] = form
                
                # return HttpResponseRedirect(render(request, 'vidboard/index.html', context))
                # return render(request, 'vidboard/results.html', context)
    # else:
    form = q()
    context["form"] = form
    
    # print(form.errors)

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