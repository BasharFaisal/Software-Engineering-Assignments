from django.shortcuts import render

# Create your views here.
def index(request):
     return render(request,'index.html')

def home(request):
     return render(request,'home.html')

def show_student(request):
     return render(request,'showstudent.html')

def add_student(request):
     return render(request,'addstudent.html')

def delete_student(request):
     return render(request,'deletestudent.html')

def idet_student(request):
     return render(request,'idetstudent.html')
