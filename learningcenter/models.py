from django.db import models
from django.utils.text import slugify
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField
from . constants import *

# Create your models here.
class Class(models.Model):
    standard = models.CharField(max_length=10,choices = STANDARD_CHOICES,unique=True)
    def __str__(self):
        return self.standard
class Section(models.Model):
    standard = models.ForeignKey(Class,on_delete=models.CASCADE)
    section = models.CharField(max_length = 1)
    class Meta:
        ordering = ['section']
    def __str__(self):
        return self.standard.standard+'-'+self.section
class Notice(models.Model):
    title = models.CharField(max_length = 100)
    associated_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    description = RichTextUploadingField()
    publish_date = models.DateField(auto_now_add = True)
    slug = models.SlugField(max_length = 200,null = True,blank = True)
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Notice, self).save(*args, **kwargs)

class Classwork(models.Model):
    title = models.CharField(max_length = 100)
    file = models.FileField(upload_to = 'classworks/')
    associated_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(max_length = 200,null = True,blank = True)
    tags = TaggableManager()
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Classwork, self).save(*args, **kwargs)
class Homework(models.Model):
    title = models.CharField(max_length = 100)
    file = models.FileField(upload_to = 'homeworks/')
    associated_class = models.ForeignKey(Class,on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(max_length = 200,null = True,blank = True)
    tags = TaggableManager()
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Homework, self).save(*args, **kwargs)
