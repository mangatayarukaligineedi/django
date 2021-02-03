from django.urls import path
from hotel import views
from django.contrib.auth import views as v 

urlpatterns = [
    path('',views.home,name="hm"),
    path('flt/',views.facilities,name="ft"),
    path('cnt/',views.contact,name="cn"),
    path('reg/',views.regis,name="rg"),
    path('pf/',views.prfle,name="pfe"),
    path('upf/',views.updf,name="upfe"),
    path('bk/',views.bkroom,name="brm"),
    path('br/',views.bookrm,name="bkrm"),
    path('lg/',v.LoginView.as_view(template_name="sa/login.html"),name="lgn"),
    path('lgg/',v.LogoutView.as_view(template_name="sa/logout.html"),name="lgo"),
]
