from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from .models import Course


def index(request):
    context= {
    'courses': Course.objects.all()
    }
    return render(request, 'myapp/index.html', context)

def create(request):
    print(request.POST)
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect ('/')
    else:
        Course.objects.create(name = request.POST['name'], description = request.POST['description'])

        return redirect('/')

def delete(request, number):
    context = {
    'course' : Course.objects.get(id=(number)),
    'courses': Course.objects.all(),
    }

    return render(request, 'myapp/delete.html', context)




def destroy(request, number):
    course = Course.objects.get(id=(number))
    course.delete()
    return redirect ('/')




# errors = Course.objects.basic_validator(request.POST)
# if len(errors):
#     for key, value in errors.items():
#         messages.error(request, value)
#         return redirect ('/index')
# else:
#     Course.objects.create(name = request.POST['name'], description = request.POST['description'])
