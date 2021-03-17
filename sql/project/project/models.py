from django.db import models

class Insert(models.Model):
    eventname= models.CharField(max_length=100)
    date= models.DateField()
    time= models.TimeField()
    location= models.CharField(max_length=100)
    image= models.URLField(max_length=1000000)
    isLiked=models.BooleanField(default=0)
    

    class Meta:
        db_table="dhar"