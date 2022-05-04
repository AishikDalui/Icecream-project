from tkinter import Variable
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from matplotlib.style import context
from datetime import datetime
from polls.models import Contract
from django.contrib import messages
from sqlalchemy import desc

def index(request):
    context={
        "varibale":"This is my variable"
    }
    return render(request,"index.html",context)

def about(request):
    # return HttpResponse("This is my about page")
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")
    # return HttpResponse("This is my about page")
def contract(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contract=Contract(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contract.save()
        messages.success(request, 'Profile details updated.')
    
    return render(request,"contract.html")

# Create your views here.
