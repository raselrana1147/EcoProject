from django.urls import path
from dashboard import views

app_name='dashboard'
urlpatterns=[
	path('index/',views.index, name='dashboard_index')
]
