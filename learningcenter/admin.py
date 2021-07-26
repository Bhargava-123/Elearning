from django.contrib import admin
from . models import Class, Section, Notice, Classwork, Homework

# Register your models here.
admin.site.register(Class)
admin.site.register(Section)
admin.site.register(Notice)
admin.site.register(Classwork)
admin.site.register(Homework)
