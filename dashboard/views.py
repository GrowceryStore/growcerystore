from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from dashboard.forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from orders.models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# DASHBOARD WORK

@login_required
def dashview(request):
    cate=Category.objects.all().count()
    produ=Product.objects.all().count()
    suppl=Supplier.objects.all().count()
    purc=Purchase.objects.all().count()
    context={'cate':cate,'produ':produ,'suppl':suppl,'purc':purc}
    return render(request,"dashboard.html",context)

# SEARCH WORK



# PASSWORD CHANGE 

class passwordview(TemplateView):
    template_name='password.html'


# INVOICE VIEW

def invoiceview(request):
    order=Order.objects.all()
    return render(request,'invoice.html',{'order':order})

def invgenerateview(request,id):
    order=Order.objects.get(id=id)
    orderitems=OrderItem.objects.filter(order_id=id)
    #ordernows=Ordernow.objects.all()
    return render(request,'invgenerate.html',{'order':order,'orderitems':orderitems})

    
# CATEGORY VIEWS    

class addcatview(TemplateView):
    template_name="add-category.html"

def mancatview(request):
    categorys=Category.objects.all()
    return render(request, "managecat.html",{'categorys':categorys})

def insertcategory(request):
    if request.method=='POST':
        form=addcatform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dash/')
        else:
            return HttpResponse("Failed To Insert Data")
    else:
        form=addcatform()
    return render(request,"add-category.html",{'form':form})

def editcat(request,id):
    categorys=Category.objects.get(id=id)
    return render(request,'editcat.html',{'categorys':categorys})

def deletecat(request,id):
    categorys=Category.objects.get(id=id)
    categorys.delete()
    return redirect('/dash/')

def updatecat(request,id):
    categorys=Category.objects.get(id=id)
    form=Categoryform(request.POST,request.FILES,instance=categorys)
    if form.is_valid():
        form.save()
        return redirect('/dash/')
    return render(request,'editcat.html',{'form':form})

# ORDER VIEWS 

def orderlistview(request):
    order=Order.objects.all()
    orderitem=OrderItem.objects.all()
    return render(request,'orderlist.html',{'order':order,'orderitem':orderitem})


# CUSTMOR VIEWS 

class custlistview(TemplateView):
    template_name="custlist.html" 

# PRODUCT VIEWS 

def addproview(request):
    categorys=Category.objects.all()
    return render(request,"add-product.html",{'categorys':categorys})

def manproview(request):
    products=Product.objects.all()
    categ=Category.objects.all()
    return render(request, "managepro.html",{'products':products,'categ':categ})

def insertproduct(request):
    if request.method=='POST':
        form=addproform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dash/')
        else:
            return HttpResponse("Failed To Insert Data")
    else:
        form=addproform()
    return render(request,"add-product.html",{'form':form})

def editpro(request,id):
    products=Product.objects.get(id=id)
    categ=Category.objects.all()
    return render(request,'editpro.html',{'products':products,'categ':categ})

def deletepro(request,id):
    products=Product.objects.get(id=id)
    products.delete()
    return redirect('/dash/')

def updatepro(request,id):
    products=Product.objects.get(id=id)
    form=Productform(request.POST,request.FILES,instance=products)
    if form.is_valid():
        form.save()
        return redirect('/dash/')
    return render(request,'editpro.html',{'form':form})

def viproview(request,id):
    products=Product.objects.get(id=id)
    return render(request,'viewproduct.html',{'products':products})

# STOCK VIEWS 

def stockview(request):
    prods=Product.objects.all()
    
    #prods=OrderItem.objects.select_related('product').all()
    return render(request, "stocklist.html",{'prods':prods})

# PURCHASE VIEWS 

def purchaseview(request):
    purchases=Purchase.objects.all()
    products=Product.objects.all()
    employeprofiles=Employeprofile.objects.all()
    suppliers=Supplier.objects.all()
    return render(request,"purchase.html",{'purchases':purchases,'products':products,'employeprofiles':employeprofiles,'suppliers':suppliers})

def addpurchaseview(request):
    products=Product.objects.all()
    employeprofiles=Employeprofile.objects.all()
    suppliers=Supplier.objects.all()
    return render(request,"add-purchase.html",{'products':products,'employeprofiles':employeprofiles,'suppliers':suppliers})

def insertpurchase(request):
    if request.method=='POST':
        form=addpurform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dash/')
        else:
            return HttpResponse("Failed To Insert Data")
    else:
        form=addpurform()
    return render(request,"purchase.html",{'form':form})


def editpurchase(request,id):
    purchases=Purchase.objects.get(id=id)
    prod=Product.objects.all()
    employeprofiles=Employeprofile.objects.all()
    suppli=Supplier.objects.all()
    return render(request,'editpurchase.html',{'purchases':purchases,'prod':prod,'employeprofiles':employeprofiles,'suppli':suppli})

def deletepurchase(request,id):
    purchases=Purchase.objects.get(id=id)
    purchases.delete()
    return redirect('/dash/')

def updatepurchase(request,id):
    purchases=Purchase.objects.get(id=id)
    form=Purchaseform(request.POST,instance=purchases)
    if form.is_valid():
        form.save()
        return redirect('/dash/')
    return render(request,'editpurchase.html',{'form':form})

# PROFILE VIEWS 

def profileview(request):
    return render(request,"profile.html")

# SUPPLIER VIEWS 

def supplierview(request):
    suppliers=Supplier.objects.all()
    return render(request, "supplier.html",{'suppliers':suppliers})

def insertsupplier(request):
    if request.method=='POST':
        form=addsuppform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/dash/')
        else:
            return HttpResponse("Failed To Insert Data")
    else:
        form=addcatform()
    return render(request,"supplier.html",{'form':form})

def addsupplierview(request):
    categorys=Category.objects.all()
    return render(request,"add-supplier.html",{'categorys':categorys})

def editsupplier(request,id):
    suppliers=Supplier.objects.get(id=id)
    categorys=Category.objects.all()
    return render(request,'editsupplier.html',{'suppliers':suppliers,'categorys':categorys})

def deletesupplier(request,id):
    suppliers=Supplier.objects.get(id=id)
    suppliers.delete()
    return redirect('/dash/')

def updatesupplier(request,id):
    suppliers=Supplier.objects.get(id=id)
    form=Supplierform(request.POST,request.FILES,instance=suppliers)
    if form.is_valid():
        form.save()
        return redirect('/dash/')
    return render(request,'editsupplier.html',{'form':form})


# FEEDBACK WORK

def feedview(request):
    contacts=contact1.objects.all()
    return render(request,"feedback.html",{'contacts':contacts})


# CHANGE PASSWORD

def change_passwordview(request):
    if request.method=='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your password was successfully changed.')
            return redirect('change_password')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'change_password.html',{'form':form})
