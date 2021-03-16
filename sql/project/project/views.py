from django.shortcuts import render
from project.models import Insert
# Create your views here.
data=Insert.objects.all()
def liked(request):
        
     return render(request,"project/index.html",{'data':data})

def new(request):
    message=0
    if request.method=="POST":
            eventname=request.POST['eventname']
            date=request.POST['date']
            time=request.POST['time']
            location=request.POST['location']
            image=request.POST['image']
            ins=Insert(eventname=eventname,date=date,time=time,location=location,image=image)
            ins.save()
            # print(date,eventname)
            global data
            data=Insert.objects.all()
            message=1;
            return render(request,"project/new.html",{'message':message}) 
    
    return render(request,"project/new.html",{'message':message})         
       
