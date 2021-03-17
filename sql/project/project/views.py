from django.shortcuts import render
from project.models import Insert
# Create your views here.
data=Insert.objects.all()

isLiked=0
def liked(request):
      if request.method=="POST":
        global isLiked
        isLiked=request.POST['isLiked']
        a=int(isLiked)
      
        tmp=Insert.objects.get(id=isLiked)

        if tmp.isLiked==0:
          tmp.isLiked=1
        else:
          tmp.isLiked=0 
        Insert.objects.filter(id=isLiked).update(isLiked=tmp.isLiked)
        print(type(tmp.isLiked)," ",tmp.isLiked," ",type(a)," ",a)
        return render(request,"project/index.html",{'data':data,'correct':tmp.isLiked,'val':a})
      
      return render(request,"project/index.html",{'data':data,'val':isLiked})
    

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
       
