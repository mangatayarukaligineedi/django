from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Exfd(models.Model):
	g = [('M','Male'),('FM','FeMale')]
	l = [('English','English'),('Hindi','Hindi'),('Telugu','Telugu'),('Urdhu','Urdhu')] 
	d = models.OneToOneField(User,on_delete=models.CASCADE)
	age = models.IntegerField(null=True)
	gender = models.CharField(max_length=10,choices=g)
	lang = models.CharField(max_length=10,choices=l)
	address = models.CharField(max_length=200,null=True)
	phno = models.CharField(max_length=10,null=True)
	impf = models.ImageField(upload_to="Profile/",default="avathar.png")

@receiver(post_save,sender=User)
def Crpf(sender,instance,created,**kwargs):
	if created:
		Exfd.objects.create(d=instance)

class Room_details(models.Model):
	tp=[('AC','AC'),('NON-AC','NON-AC')]
	cat=[('Suit','Suit'),('Double Bed','Double Bed'),('Single Bed','Single Bed'),('Triple Bed','Triple Bed')]
	number = models.IntegerField(default=101)
	room_type = models.CharField(max_length=12,choices=tp)
	category = models.CharField(max_length=10,choices=cat)
	cost = models.IntegerField(default=2000)
	image = models.ImageField(upload_to="Image/",default="avathar.png")

class Book_Room(models.Model):
	p=[('1 person','1 person'),('2 persons','2 persons'),('3 persons','3 persons'),('4 persons','4 persons')]
	rm = [('101','101'),('102','102'),('103','103'),('104','104'),('105','105'),('106','106'),('107','107'),('108','108')]
	room_num = models.IntegerField(default=101,choices=rm)
	fromdate = models.DateField()
	todate = models.DateField()
	people = models.CharField(max_length=10,choices=p)

# class Reservation(models.Model):
#     check_in = models.DateField(auto_now =False)
#     check_out = models.DateField()
#     room = models.ForeignKey(Room_details, on_delete = models.CASCADE)
#     guest = models.ForeignKey(User, on_delete= models.CASCADE)

#     booking_id = models.CharField(max_length=100,default="null")
#     def __str__(self):
#         return self.guest.username