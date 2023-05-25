from django.shortcuts import render, redirect,HttpResponse
from django.views.generic import TemplateView
from myapp.forms import *
from django.contrib.auth import login
from cart.forms import CartAddProductForm

def homeview(request):
    ser=service.objects.all()[:3]
    cus=serviceitem.objects.filter(serviceid_id=14)
    return render(request,"home.html",{'ser':ser,'cus':cus})   
class contactview(TemplateView):
    template_name="contact.html"    
      
class loginview(TemplateView):
    template_name="login.html"    
class breakfast(TemplateView):
    template_name="breakfast.html"  
class aboutusview(TemplateView):
    template_name="aboutus.html"    


  

# Create your views here.
def insertcontect(request):
    if request.method=="POST":
        form=contectform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form=contectform()
    return render(request,"home.html",{'form':form})


def regview(request):
    if request.method=="POST":
       form=registrationform(request.POST)
       if form.is_valid():
           user=form.save()
           login(request,user)
           return redirect('/home/')
    else:
     form=registrationform()
    return render(request,"registration/reg.html",{'form':form})

def blogsview(request):
    blg=blog.objects.all()
    return render(request,"blogs.html",{'blg':blg})


def blogdetailview(request,id):
    blg=blog.objects.get(id=id)
    return render(request,"blogdetail.html",{'blg':blg})

def servicesview(request):
    ser=service.objects.all()
    return render(request,"services.html",{'ser':ser})

def serviceitemview(request,id):
    item=serviceitem.objects.filter(serviceid_id=id)
    cart_product_form=CartAddProductForm()
    return render(request,"serviceitem.html",{'item':item,'cart_serviceitem_form':cart_product_form})

def serviceitemdetailview(request,id):
    item=cusion.objects.select_related('serviceitemid').filter(serviceitemid__id=id)
    cart_product_form=CartAddProductForm()
    return render(request,"serviceitemdetail.html",{'item':item,'cart_serviceitem_form':cart_product_form})

def cusionsview(request):
    cus=serviceitem.objects.filter(serviceid_id=14)
    return render(request,"cusion.html",{'cus':cus})

def typecusionsview(request,id):
    cust=typecusion.objects.filter(cusioneid_id=id)
    return render(request,"typecusion.html",{'cust':cust})




