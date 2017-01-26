from django.shortcuts import render,redirect, HttpResponse
from . import models
# Create your views here.
def index(request):
    data =  models.Course.objects.all()
    for x in models.Course.objects.filter(id = 1):
        print x.course

    context = { "datas": data }

    return render(request, "courses/index.html", context)

def add(request):
    models.Course.objects.create(course= str(request.POST['name']), description= str(request.POST['desc']))
    return redirect("/")

def remove(request, course_id):
    context = {"id" : course_id}
    return render(request, "courses/remove.html", context)

def delete_process(request, course_id):
    models.Course.objects.filter(id = course_id).delete()
    return redirect("/")
