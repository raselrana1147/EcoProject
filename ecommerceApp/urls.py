
from django.urls import path
from ecommerceApp import views

app_name="ecommerce"
urlpatterns = [
   
    path('', views.home,name="home_page"),
    path('product_detail/<str:slug>', views.product_detail,name="product_detail"),
    path('category_product/<int:categoty_id>', views.category_wise_product,name="category_product"),
    path('subcategory_product/<int:subcategoty_id>', views.subcategory_wise_product,name="subcategory_product"),
    path('about_us/', views.about_us,name="about_us"),
    path('contact_us/', views.contact_us,name="contact_us"),
    path('search_item/', views.search_item,name="search_item"),
    path('send_review/', views.send_review,name="send_review"),
    path('faqs/', views.faqs,name="faqs"),
]



