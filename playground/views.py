from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
#pull data from db
# transform     
#send email
    return HttpResponse('Hello world')
