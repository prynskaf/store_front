from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# def say_hello(request):
#     # Pull data from db
#     # Transform data
#     # send email and so on 
#     return HttpResponse('Hello, world')


# templates 
def say_hello(request):
   return render(request, 'hello.html', {'name': 'Prince'})


