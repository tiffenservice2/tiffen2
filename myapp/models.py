from django.db import models
import datetime
from tinymce.models import HTMLField


# Create your models here.
class contect(models.Model): 
    fname=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    contect=models.CharField(max_length=10)
    day=models.CharField(max_length=15)
    class Meta:
            db_table = 'contect'
            
#class registration(models.Model): 
    #fname=models.CharField(max_length=50)
    #email=models.CharField(max_length=20)
    #contect=models.CharField(max_length=10)
   # password=models.CharField(max_length=15)
    #class Meta:
           # db_table = 'registration'
            
class blog(models.Model): 
        title=models.CharField(max_length=300)
        descripaction=HTMLField()
        postby=models.CharField(max_length=20 , default="Admin")
        photo=models.ImageField(upload_to='blog/')
        poston =models.DateField(default=datetime.date.today())
        class Meta:
                db_table = 'blog'

        def __self__(self):
                return self.title
        
class service(models.Model):
       type=models.CharField(max_length=50)
       descripaction=models.TextField()
       photo=models.ImageField(upload_to='service/')
       class Meta:
                db_table = 'service'

       def __str__(self):
                return self.type
        
class serviceitem(models.Model):
        itemname=models.CharField(max_length=100)
        serviceid=models.ForeignKey(service,on_delete=models.CASCADE)
        
        price=models.FloatField()
        photo=models.ImageField(upload_to='items/')

        class Meta:
                db_table="serviceitem"
        def __str__(self):
                return self.itemname



class cusion(models.Model):
       type=models.CharField(max_length=50)
       descripaction=models.TextField()
       photo=models.ImageField(upload_to='service/')
       serviceitemid=models.ForeignKey(serviceitem,on_delete=models.CASCADE,blank=True,null=True)
       class Meta:
                db_table = 'cusion'

       def __str__(self):
                return self.type     


class typecusion(models.Model):
        itemname=models.CharField(max_length=100)
        cusioneid=models.ForeignKey(cusion,on_delete=models.CASCADE)
        descripaction=models.TextField()
        price=models.FloatField()

        photo=models.ImageField(upload_to='items/')

        class Meta:
                db_table="typecusion"
        def __str__(self):
                return self.itemname


    

    

