from django.contrib import admin
from orderapp.models import Cart, Order,OrderProduct



# Register your models here.

class CartAdmin(admin.ModelAdmin):
	list_display=['product','user','quantity','product_price','unit_total','created_at']
	list_filter=['user']

class OrderAdmin(admin.ModelAdmin):
	list_display=['first_name','last_name','phone','country','city','address','total','transaction_id','status','created_at']


class OrderProductAdmin(admin.ModelAdmin):
	list_display=['quantity','price','status','product_id','order_id','created_at']


admin.site.register(Cart,CartAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(OrderProduct,OrderProductAdmin)