from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, TextInput, EmailInput, PasswordInput, Select, FileInput
from userapp.models import UserProfile




class RegistrationForm(UserCreationForm):
	
	username=forms.CharField(max_length=100,label='Username',widget=forms.TextInput(attrs={'placeholder':'Enter your username'}))
	email=forms.EmailField(max_length=100,label='Email',widget=forms.EmailInput(attrs={'placeholder':'Enter your email'}))
	first_name=forms.CharField(max_length=100,label='first name',widget=forms.TextInput(attrs={'placeholder':'Enter your first name'}))
	last_name=forms.CharField(max_length=100,label='last name',widget=forms.TextInput(attrs={'placeholder':'Enter your last name'}))

	class Meta:
		model=User
		fields=('username','email','first_name','last_name','password1','password2')
		widgets={
			'password1':forms.PasswordInput(attrs={'placeholder':'Enter your password','class':'form-control'}),
			'password2':forms.PasswordInput(attrs={'placeholder':'Enter confirm password','class':'form-control'}),
		}

class UserUpdateForm(UserChangeForm):
	class Meta:
		model=User
		fields=('username','email','first_name','last_name')
		widgets={
			'username':TextInput(attrs={'placeholder':'Username','class':'input'}),
			'email':EmailInput(attrs={'placeholder':'Email','class':'input'}),
			'first_name':TextInput(attrs={'placeholder':'first name','class':'input'}),
			'last_name':TextInput(attrs={'placeholder':'last name','class':'input'}),

		}


CITY=[
	('Dhaka','Dhaka'),
	('Rangpur','Rangpur'),
	('Sylhet','Sylhet'),
	('Mymemsing','Mymemsing'),
	('Rajshahi','Rajshahi'),
	('Chittagong','Chittagong'),
	('Barishal','Barishal'),
	('Khulna','Khulna'),
]


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields=('phone','phone','address','city','country','image')
		widgets={
			'phone':TextInput(attrs={'placeholder':'Phone','class':'input'}),
			'address':TextInput(attrs={'placeholder':'address','class':'input'}),
			'city':Select(attrs={'placeholder':'first name','class':'input'},choices=CITY),
			'country':TextInput(attrs={'placeholder':'country','class':'input'}),
			'image':FileInput(attrs={'placeholder':'country','class':'input'}),

		}
