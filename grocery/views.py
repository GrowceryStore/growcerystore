from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from grocery.forms import *
from dashboard.forms import *
from dashboard.models import Product
from django.contrib.auth import login,authenticate
# from django.contrib.auth.decorators import login_required
# from cart.cart import Cart
from cart.forms import CartAddProductForm
from django.http import JsonResponse
from django.db.models import Count
from orders.models import *


class loginview(TemplateView):
    template_name="login.html"   
class registerview(TemplateView):
    template_name="register.html"     
class logview(TemplateView):
    template_name="log.html"
# class homeview(TemplateView):
#     template_name="home.html"
class contactview(TemplateView):
    template_name="contact.html"
class legalview(TemplateView):
    template_name="legal.html"
class termsview(TemplateView):
    template_name="terms.html"        
class fruvegview(TemplateView):
    template_name="fruvegdetails.html"        
class dairyview(TemplateView):
    template_name="dairyprod.html"        
class meateggview(TemplateView):
    template_name="meategg.html"        
class grainsview(TemplateView):
    template_name="grainsnutri.html"         




def insertcontact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/')
    else:
        form=contactform()
    return render(request,"contact.html",{'form':form})
   
def subscribe(request):
    if request.method=='POST':
        form=subscribeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form=subscribeform()
    return render(request,"home.html",{'form':form})   

def homeview(request):
    categorys=Category.objects.all()
    products=Product.objects.all()[0:8]
    cart_product_form=CartAddProductForm
    return render(request, "home.html",{'products':products, 'categorys':categorys,'cart_product_form':cart_product_form})

def productdetailsview(request,id):
    p=Product.objects.get(id=id)
    pro=like.objects.filter(Productid_id=id).count()
    cart_product_form=CartAddProductForm
    reviews=review.objects.all()
    return render(request,"productdetails.html",{'p':p,'cart_product_form':cart_product_form,'reviews':reviews,'pro':pro})

def productview(request,id):
    pro=Product.objects.filter(Categoryid_id=id)
    cart_product_form=CartAddProductForm
    return render(request,"products.html",{'pro':pro,'cart_product_form':cart_product_form})

def faqview(request):
    faqs=faq.objects.all()
    return render(request, "faq.html",{'faqs':faqs})

def searchview(request):
    srh=request.GET['searchbox']
    pro=Product.objects.filter(Product_Name__icontains=srh)
    cart_product_form=CartAddProductForm
    context={'pro':pro,'cart_product_form':cart_product_form}
    return render(request, 'search-result.html', context)

def signup(request):
    next=""
    if request.GET:
        next=request.GET['next']
    if request.method=='POST':
        form=signupform(request.POST)
        if form.is_valid():
            User=form.save()
            login(request,User)
            if next=="":
                return redirect('/home/')
            else:
                return redirect(next)
    else:
        form=signupform()
    return render(request,"registration/signup.html",{'form':form})     

def logincustomer(request):
    next=""
    if request.GET:
        next=request.GET['next']
    print(next)    
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            User=authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )  
            login(request,User)
            if next=="":
                return redirect('/home/')
            else:
                return redirect(next) 


def shopview(request):
    catego=Category.objects.all()
    products=Product.objects.all()
    cart_product_form=CartAddProductForm
    return render(request,"shop.html",{'products':products, 'catego':catego,'cart_product_form':cart_product_form})

def shopfilterview(request,id):
    pro=Product.objects.filter(Categoryid_id=id)
    catego=Category.objects.all()
    cart_product_form=CartAddProductForm
    return render(request,"shopfilter.html",{'pro':pro,'cart_product_form':cart_product_form,'catego':catego})

def dolike(request):
    #form=dolike()
    Productid=request.GET['pid']
    Userid=request.GET['uid']
    data={
        'is_taken': like.objects.filter(Userid_id=Userid,Productid_id=Productid).exists()
    }
    print(data['is_taken'])
    if data['is_taken']:
        data['error_message'] = 'Your like is already registered. You cannot do like again.'
        return JsonResponse(data)
    else:
        form=like.objects.create(Productid_id=Productid,Userid_id=Userid)
        form.save()
        data['message']='Your like is registred.'
        return JsonResponse(data)
    return render(request,'productdetails.html',{'form':form})


def dofav(request):
    Productid=request.GET['Pid']
    Userid=request.GET['Uid']
    data={
        'is_taken': fav.objects.filter(Userid_id=Userid,Productid_id=Productid).exists()
    }
    print(data['is_taken'])
    if data['is_taken']:
        data['error_message'] = 'Your product is already added to the list.'
        return JsonResponse(data)
    else:
        form=fav.objects.create(Productid_id=Productid,Userid_id=Userid)
        form.save()
        data['message']='Your product is registred.'
        return JsonResponse(data)
    return render(request,'productdetails.html',{'form':form})

def favview(request):
    Userid=request.user.id
    favs=fav.objects.select_related('Productid').filter(Userid_id=Userid)
    cart_product_form=CartAddProductForm
    return render(request,"fav.html",{'favs':favs,'cart_product_form':cart_product_form})

def myorderview(request):
    C=OrderItem.objects.select_related('order').filter(order__userid=request.user.id)
    return render(request,'myorder.html',{'C':C})

def insertreview(request):
    if request.method=='POST':
        form=reviewform(request.POST)
        next=request.POST.get('next')
        if form.is_valid():
            form.save()
            return redirect(next)
    else:
        form=reviewform()
    return render(request,"productdetails.html",{'form':form})    

