from django import template
from product.models import Category
from ecomapp.models import Setting

register=template.Library()

@register.simple_tag
def all_categories():
	return Category.objects.filter(parent=None).order_by('-id')

@register.simple_tag
def eco_setting():
	return Setting.objects.get(id=1)

