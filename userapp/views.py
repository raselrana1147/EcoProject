from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth import logout,authenticate,login, update_session_auth_hash
from userapp.forms import RegistrationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from userapp.models import UserProfile
from product.models import Category
from django.contrib import messages
from product.models import Comment


# Create your views here.

def login_register(request):

	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			messages.success(request, 'Sccessfully login.')
			return redirect('ecommerce:home_page')
		else:
			messages.warning(request, 'Invalid credentials.')
			return redirect('profile:login_register')

	
	
	return render(request,'login_register.html')

def user_logout(request):
	logout(request)
	return redirect('ecommerce:home_page')

def user_register(request):
	if request.method=="POST":
		form=RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			password1=form.cleaned_data.get('password1')
			user=authenticate(username=username,password=password1)
			if user is not None:
				login(request,user)
				profile=UserProfile()
				profile.user_id=request.user.id
				profile.image='profile/profile.jpg'
				profile.save()

			return redirect('ecommerce:home_page')
		else:
			messages.warning(request,'Your reset password is not matching')
	else:
		form=RegistrationForm()
	context={
		'form':form
	}
	return render(request,'user_register.html',context)

def user_profile(request):
	profile=UserProfile.objects.get(user_id=request.user.id);
	context={
		
		'profile':profile
	}
	return render(request,'user_profile.html',context)



@login_required(login_url='/user/login_register')
def update_user_profile(request):
	
	if request.method=="POST":
		user_form=UserUpdateForm(request.POST, instance=request.user)
		profile_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.userprofile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.warning(request,'Your profile has been updated')
			return redirect('profile:user_profile')
	else:
		user_form=UserUpdateForm(instance=request.user)
		profile_form=ProfileUpdateForm(instance=request.user)

		context={
			'user_form':user_form,
			'profile_form':profile_form,
		}
	return render(request,'user_update.html',context)

@login_required(login_url='/user/login_register')
def change_password(request):
	
	if request.method=="POST":
		password_form=PasswordChangeForm(request.user,request.POST)
		if password_form.is_valid():
			user=password_form.save()
			update_session_auth_hash(request,user)
			messages.warning(request,'Your password has been updated')
			return redirect('profile:user_profile')
		else:
			messages.warning(request,'Something went wrong')
			return redirect('profile:change_password')
	else:
		password_form=PasswordChangeForm(request.user)
		
		context={
			'password_form':password_form,
		}
	return render(request,'change_password.html',context)



@login_required(login_url='/user/login_register')
def user_product_review(request):

	reviews=Comment.objects.filter(user_id=request.user.id)
	context={	
		'reviews':reviews
	}
	return render(request,'user_review.html',context)

def delete_review(request,id):
	url=request.META.get('HTTP_REFERER')
	Comment.objects.get(id=id).delete()
	messages.warning(request,'Reviews has been deleted successfully')
	return HttpResponseRedirect(url)









		

