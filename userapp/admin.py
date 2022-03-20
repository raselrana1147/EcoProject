from django.contrib import admin
from userapp.models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display=['phone','address','city','country','full_name','profile_image']

admin.site.register(UserProfile,UserProfileAdmin)
