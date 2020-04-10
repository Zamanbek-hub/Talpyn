from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from .tokenize import add_token


# Create your models here.



class Course(models.Model):
    course_name = models.CharField('Course', max_length = 100,)
    description = models.TextField(blank=True)
    old_price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField()
    date = models.DateTimeField('date published')

    TOKEN_CHOICES = [
        (50, '50'),
        (100, '100'),
        (200, '200'),
        (500, '500'),
        (1000, '1000'),
    ]

    tokens = models.PositiveIntegerField(
        choices=TOKEN_CHOICES,
        default = 50
    )

    def save(self, *args, **kwargs): 
        super(Course, self).save(*args, **kwargs)
        add_token(self.tokens,self.id)


    def __str__(self):
        return self.course_name


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img  = models.ImageField(upload_to='avatars/',blank=True, verbose_name = "IMAGE", default = 'avatars/user.png')
    city = models.CharField('City', max_length = 100,)
    course = models.CharField('Course', max_length = 100,)
    phone = models.CharField('Phone', max_length = 100,)
    sex = models.NullBooleanField()
    status = models.BooleanField(default=False)
    courses = models.ManyToManyField(Course)
    # age  = models.PositiveIntegerField(verbose_name = 'age')
    # phone = models.CharField(max_length = 12, verbose_name = 'phone number')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user.username

class Lesson(models.Model):
    lesson_name = models.CharField('Lesson', max_length = 100,)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_name

class Video(models.Model):
    video_name = models.CharField('Course', max_length = 100,)
    url = models.CharField('Video', max_length = 225,)
    time = models.DurationField()
    desctiprion = models.TextField(blank=True)
    lesson =  models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return self.video_name

class Token(models.Model):
    token =  models.CharField('Course', max_length = 50, unique=True)
    recerved = models.BooleanField(default=False)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.id

class Comment(models.Model):
    text = models.TextField('Opinion', blank=False)
    date = models.DateTimeField('date published')
    client =  models.ForeignKey(Client, on_delete=models.CASCADE)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

class Answer(models.Model):
    text = models.TextField('Opinion', blank=False)
    date = models.DateTimeField('date published')
    comment =  models.ForeignKey(Comment, on_delete=models.CASCADE)
    course =  models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

