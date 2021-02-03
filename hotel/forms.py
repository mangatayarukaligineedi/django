from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from hotel.models import Exfd,Room_details,Book_Room

class UsReg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Your PassWord"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confrim PassWord"}))

	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your UserName",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Your Emailid",
			"required":True,
			}),
		} 

class Upd(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			}),
		}

class Pad(forms.ModelForm):
	class Meta:
		model = Exfd
		fields = ["age","gender","lang","address","phno","impf"]
		widgets = {
		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Update your age",
			}),
		"gender":forms.Select(attrs={
			"class":"form-control",
			"title":"gender",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"Update your address"
			}),
		"lang":forms.Select(attrs={
			"class":"form-control",
			"title":"language",
			}),
		"phno":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Your Phone Number"
			}),
		}

class Roomdetails(ModelForm):
	class Meta:
		model = Room_details
		fields = "__all__"
		widgets = {
		"number":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Room Number",
			}),
		"room_type":forms.Select(attrs={
			"class":"form-control",
			"title":"room_type"
			}),
		"category":forms.Select(attrs={
			"class":"form-control",
			"title":"category",
			}),
		"cost":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Cost",
			}),
		}

class BookRoom(ModelForm):
	class Meta:
		model = Book_Room
		fields = "__all__"
		widgets = {
		"room_num":forms.Select(attrs={
			"class":"form-control",
			"title":"room_num",
			}),
		"fromdate":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			}),
		"todate":forms.DateInput(attrs={
			"class":"form-control",
			"type":"date",
			}),
		"people":forms.Select(attrs={
			"class":"form-control",
			"title":"people",
			}),
		}
