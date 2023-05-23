from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
#pull data from db
# transform     
#send email
   return render(request,'hello.html', { 'name': 'AMIT'}) #parameters (request object ,name of template, put mapping words to change in page)
