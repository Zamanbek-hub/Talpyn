from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Client)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Answer)
admin.site.register(Token)