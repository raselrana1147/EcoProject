from django.shortcuts import render
from product.models import Category, Product
from django.http import JsonResponse


# Create your views here.

def category_list(request):
    categories = Category.objects.filter(parent=None).order_by('-id')
    context = {
        'categories': categories
    }
    return render(request, 'dashboard/category/index.html', context)


def category_add(request):
    if request.method == "POST":
        category = Category()
        category.title = request.POST.get('title')
        category.parent_id = request.POST.get('parent_id')
        if len(request.FILES) !=0:
        	category.image=request.FILES['image']

        category.save()
        data = {
            'message': 'Successfully added',
            'statu': 200
        }
        
        return JsonResponse(data)

    else:
        categories = Category.objects.filter(parent=None).order_by('-id')
        context = {
            'categories': categories
        }
    return render(request, 'dashboard/category/add_category.html', context)

def category_delete(request):
	if request.method=="POST":
		Category.objects.get(id=request.POST.get('item_id')).delete()
		data={
			'message':'Successfully deleted',
			'status':200
		}
		return JsonResponse(data)
	else:
		data={
			'message':"Something went wrong",
			status:403
		}
		return JsonResponse(data)

	

	

