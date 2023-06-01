from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Value, F
from django.db.models.aggregates import Count, Max, Min, Avg
from store.models import Product, OrderItem, Order, Customer


def say_hello(request):
#pull data from db
# transform     
#send email
   #keyword = value
  # queryset = Product.objects.all()[:5]# for first page
  # queryset = Product.objects.all()[5:10]# for second page

   #queryset = Product.objects.values('id', 'title', 'collection__title')

   #queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
   
   #slect_related (1)
   #prefetch_related(n)
   #queryset = Product.objects.select_related('collection').all()
   #queryset = Product.objects.prefetch_related('promotions').select_related('collection').all()
   #selection related objects
   #queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[:5]
   #result = Product.objects.filter(collection_id=1).aggregate(count=Count('id'), min_price=Min('unit_price'))
   
   queryset = Customer.objects.annotate(new_id=F('id') + 1)
   
   
   
   return render(request,'hello.html', { 'name': 'AMIT', 'result': list(queryset)}) #parameters (request object ,name of template, put mapping words to change in page)
 