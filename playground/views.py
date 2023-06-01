from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from store.models import Product


def say_hello(request):
#pull data from db
# transform     
#send email
   #keyword = value
   queryset = Product.objects.filter(Q(inventory__lt=10) | ~Q(umit_price__lt=20))
   #for product in product:
      #print (product)

   return render(request,'hello.html', { 'name': 'AMIT', 'products': list(queryset)}) #parameters (request object ,name of template, put mapping words to change in page)
