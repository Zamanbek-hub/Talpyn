from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img  = models.ImageField(upload_to='avatars/',blank=True, verbose_name = "IMAGE", default = 'avatars/user.png')
    # age  = models.PositiveIntegerField(verbose_name = 'age')
    # phone = models.CharField(max_length = 12, verbose_name = 'phone number')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.user.username
