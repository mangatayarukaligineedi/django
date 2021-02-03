from django.shortcuts import render,redirect
from django.http import HttpResponse
from hotel.forms import UsReg,Upd,Pad,Roomdetails,BookRoom
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from booking import settings
from django.core.mail import send_mail
from django.contrib import messages
from hotel.models import Exfd,Room_details,Book_Room

# Create your views here.

def home(request):
	return render(request,'sa/home.html') 

def facilities(request):
	return render(request,'sa/facilities.html')

def contact(request):
	return render(request,'sa/contact.html')

def regis(request):
	if request.method == "POST":
		y = UsReg(request.POST)
		if y.is_valid():
			p = y.save(commit=False)
			rc = p.email
			sb = "Holiday Inn"
			mg = "Hi Welcome {} you have successfully registered in our portal with password: {}".format(p.username,p.password)
			sd = settings.EMAIL_HOST_USER
			snt = send_mail(sb,mg,sd,[rc])
			if snt == 1:
				p.save()
				messages.success(request,"Please check your {} for login creadentials".format(rc))
				return redirect('/lg')
			messages.danger(request,"please enter correct emailid or username or password")
	y = UsReg()
	return render(request,'sa/register.html',{"t":y}) 

@login_required
def prfle(request):
	return render(request,'sa/profile.html')

@login_required
def updf(request):
	if request.method == "POST":
		p = Upd(request.POST,instance=request.user)
		t = Pad(request.POST,request.FILES,instance=request.user.exfd)
		if p.is_valid() and t.is_valid():
			p.save()
			t.save()
			messages.success(request,"{}your profile updated successfully".format(request.user.username))
			return redirect('/pf')
	p = Upd(instance=request.user)
	t = Pad(instance=request.user.exfd)
	return render(request,'sa/update.html',{'r':p,'q':t})
	
def strg(request):
	if request.method == "POST":
		nm = request.POST['n']
		rmt = request.POST['rty']
		ct = request.POST['ca']
		cs = request.POST['cb'] 
		t = Room_details(number=nm,room_type=rmt,category=ct,cost=str(cs))
		t.save()
		return redirect('/displ')
	return render(request,'sa/roomlist.html')

@login_required
def usd(request):
	y = Room_details.objects.all()
	return render(request,'sa/display.html',{'u':y})
	

def viewinfo(request,ty):
	m = Room_details.objects.get(id=ty)
	return render(request,'sa/vwinf.html',{'vi':m})


def upf(request,rq):
	n = Room_details.objects.get(id=rq)
	if request.method == "POST":
		a = Roomdetails(request.POST,instance=n)
		if a.is_valid():
			a.save()
			return redirect('/displ')
	a = Roomdetails(instance=n)
	return render(request,'sa/edpf.html',{'k':a})


def dlt(request,ze):
	c = Room_details.objects.get(id=ze)
	if request.method == "POST":
		c.delete()
		return redirect('/displ')
	return render(request,'sa/dltusr.html',{'fe':c})


@login_required
def bookrm(request):
	if request.method == "POST":
		rm = request.POST['r']
		fd = request.POST['f']
		td = request.POST['t']
		pp = request.POST['p'] 
		t = Book_Room(room_num=rm,fromdate=fd,todate=td,people=str(pp))
		t.save()
		return redirect('/bk')
	return render(request,'sa/bookrm.html')


@login_required
def bkroom(request):
	p = Book_Room.objects.all()
	return render(request,'sa/bkroom.html',{'y':p})


def cnl(request,ze):
	d = Book_Room.objects.get(id=ze)
	if request.method == "POST":
		d.delete()
		return redirect('/displ')
	return render(request,'sa/cancel.html',{'cn':d})


# def bookrm(request):
# 	if request.method == "POST":
# 			r = BookRoom(request.POST)
# 			if r.is_valid():
# 				t = r.save(commit=False)
# 				t.id = request.user.id
# 				t.save()
# 				messages.success(request,"Room booked successfully")
# 				return redirect('/bk')
# 	r = BookRoom()
# 	return render(request,'sa/bookrm.html',{'d':r})



# @login_required
# def bkroom(request):
# 	p = Book_Room.objects.filter(id=request.user.id)
# 	return render(request,'sa/bkroom.html',{'y':p})	