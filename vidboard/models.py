from django.db import models
# from django.utils.timezone import now
# Create your models here.


class Course(models.Model):
    course = models.CharField(max_length=150)
    courseCode = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.course} - {(self.courseCode)}'

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=150, default='Baby Yoda drinking soup', blank=False, unique=True)
    desc = models.TextField(max_length=400)
    video = models.FileField(default='BabyYoda.mp4', upload_to='video_uploads/', blank=False)
    thumbnail = models.ImageField(default='default-thumbnail.png', upload_to='thumbnails/')
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    uploadDate = models.DateTimeField(auto_now_add=True, blank=False)
    subs = models.TextField(default='', blank=False)

    def __str__(self):
        return f'{self.title}'

# class Captions(models.Model):
#     course 
