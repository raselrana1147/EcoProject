from django.contrib import admin
import admin_thumbnails
from mptt.admin import DraggableMPTTAdmin
from product.models import (
			Category,
			Product,
			Images,
			Comment,
			Color,
			Size,
			Varient,
	)


class productImageInline(admin.TabularInline):
	model=Images
	readonly_fields=('id',)
	extra=1


class ProductVariantInline(admin.TabularInline):
	model=Varient
	readonly_fields=('image_tag',)
	extra=1
	show_change_link=True


class ImagesAdmin(admin.ModelAdmin):
	list_display=['title','product','show_image']
	list_filter=['title']
	list_per_page=10
	search_fields=['title']



class ProductAdmin(admin.ModelAdmin):
	list_display=['title','category','old_price','new_price','image_tag','stock','created_at','updated_at']
	list_filter=['title','created_at']
	list_per_page=10
	search_fields=['title','new_price','description']
	inlines=[productImageInline,ProductVariantInline]
	prepopulated_fields={'slug':('title',)}

class CategoryAdmin(admin.ModelAdmin):
	list_display=['title','subCat','image_tag','created_at']

class CommentAdmin(admin.ModelAdmin):
	list_display=['subject','comment','rating','created_at']



class ColorAdmin(admin.ModelAdmin):
	list_display=['name','code','color_tag']


class SizeAdmin(admin.ModelAdmin):
	list_display=['name','code']

class VarientAdmin(admin.ModelAdmin):
	list_display=['title','product','color','size','quantity','price','image_id','image_tag','created_at','updated_at']
 	
 	


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImagesAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Color,ColorAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Varient,VarientAdmin)
