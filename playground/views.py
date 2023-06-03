from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction, connection
from django.db.models import Value, F, Func, Count, ExpressionWrapper,DecimalField
from django.db.models.functions import Concat
from store.models import Product, OrderItem, Order, Customer, Collection
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TaggedItem



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
   
   #queryset = Customer.objects.annotate(
   #   #concat
   #   full_name = Func(F('first_name'),Value(' '), F('last_name'), function='CONCAT')
   #)

   #queryset = Customer.objects.annotate(
   #   #concat
   #   full_name = Concat('first_name',Value(' '),'last_name'), function='CONCAT')
   
   
   
   #discounted_price = ExpressionWrapper(F('unit_price') * 0.8, output_field=DecimalField())
   #   
   #queryset = Product.objects.annotate(
   #   discounted_price = discounted_price
   #)

#multiple transacitons 

   # with transaction.atomic():

   #    order = Order()
   #    order.customer_id = 1
   #    order.save()

   #    item = OrderItem()
   #    item.order = order
   #    item.product_id = 1
   #    item.quantity = 1
   #    item.unit_price = 10
   #    item.save()

   with connection.cursor() as cursor:
      cursor.execute()

   return render(request,'hello.html', { 'name': 'AMIT'}) # , 'result': list(queryset)})#parameters (request object ,name of template, put mapping words to change in page)
 