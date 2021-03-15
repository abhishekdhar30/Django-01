from django.shortcuts import render
from project.models import Insert
from django.contrib import messages
# Create your views here.
def func(request):
    return render(request,"project/index.html")

def new(request):
    if request.method=="POST":
            eventname=request.POST['eventname']
            date=request.POST['date']
            time=request.POST['time']
            location=request.POST['location']
            image=request.POST['image']
            ins=Insert(eventname=eventname,date=date,time=time,location=location,image=image)
            ins.save()
            # print(date,eventname)
            data=Insert.objects.all()
            print(data)
            return render(request,"project/index.html",{'data':data}) 
    
    return render(request,"project/new.html")         
       
