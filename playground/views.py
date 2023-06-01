from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from store.models import Product


def say_hello(request):
#pull data from db
# transform     
#send email
   #keyword = value
   product = Product.objects.order_by('unit_price', '-title')[0]
   product = Product.objects.earliest('unit_price')
   #for product in product:
      #print (product)

   return render(request,'hello.html', { 'name': 'AMIT', 'product': product}) #parameters (request object ,name of template, put mapping words to change in page)
