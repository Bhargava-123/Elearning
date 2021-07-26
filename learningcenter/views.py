from django.shortcuts import render
from . models import Homework
# Create your views here.
def home(request):
    homework = Homework.objects.all()
    return render(request,"learningcenter/home.html",{"Homeworks":homework})
