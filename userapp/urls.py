from django.urls import path
from userapp import views

app_name='profile'

urlpatterns=[
	path('user_logout',views.user_logout,name='user_logout'),
	path('login_register',views.login_register,name='login_register'),
	path('user_register',views.user_register,name='user_register'),
	path('user_profile',views.user_profile,name='user_profile'),
	path('update_user_profile',views.update_user_profile,name='update_user_profile'),
	path('change_password',views.change_password,name='change_password'),
	path('user_product_review',views.user_product_review,name='user_product_review'),
	path('delete_review/<int:id>',views.delete_review,name='delete_review'),
]

