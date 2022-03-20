from django.urls import path
from orderapp import views

app_name='order'
urlpatterns=[
	path('',views.order,name='order'),
	path('add_to_cart/<int:id>',views.add_to_cart,name='add_to_cart'),
	path('view_cart',views.view_cart,name='view_cart'),
	path('cart_delete/<int:id>',views.cart_destroy,name='cart_delete'),
	path('checkout/',views.checkout,name='checkout'),
	path('order_list/',views.order_list,name='order_list'),
	path('order_product_list/<int:id>',views.order_product_list,name='order_product_list'),
	path('billing_detail/<int:id>',views.billing_detail,name='billing_detail'),
]