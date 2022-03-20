from django.contrib import admin
from ecomapp.models import Setting, Slider


# Register your models here.

class SettingAdmin(admin.ModelAdmin):
	list_display=['title','kewword','phone','fax','email','smtpserver','smtpemail',
	'smtpport','facebook','instragram','contact','status','created_at']

admin.site.register(Setting,SettingAdmin)

class SliderAdmin(admin.ModelAdmin):
	list_display=['title','image','button_title','created_at']

admin.site.register(Slider,SliderAdmin)
