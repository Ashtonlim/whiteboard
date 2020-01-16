from django.urls import path
from rest_framework import routers
from .api import VideoViewSet
from . import views

router = routers.DefaultRouter()
router.register('api/videos', VideoViewSet, 'videos')
# urlpatterns = router.urls
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:video_id>', views.watch, name='watch'),
    path('api/videos/', views.VideoListCreate.as_view())
]