from django.urls import path
from product import views

app_name='adminProduct'

urlpatterns=[
	path('category_list/',views.category_list,name='admin_categori_list'),
	path('category_add/',views.category_add,name='admin_categori_add'),
	path('category_delete/',views.category_delete,name='admin_category_delete'),
]

