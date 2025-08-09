from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('add/',views.add_student,name="add"),
    path('show/',views.show_student,name="show"),
    path('delete/',views.delete_student,name="delete"),
    path('idet/',views.idet_student,name="idet"),
]