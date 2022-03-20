from django.contrib import admin
from ecommerceApp.models import ContactUs, Faq

# Register your models here.

class ContractAdmin(admin.ModelAdmin):
	list_display=['name','email','subject','message','created_at']


class FaqsAdmin(admin.ModelAdmin):
	list_display=['question','answer','order_number','status','created_at','updated_at']

admin.site.register(ContactUs,ContractAdmin)
admin.site.register(Faq,FaqsAdmin)

