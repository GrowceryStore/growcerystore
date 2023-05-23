from django.urls import path
from dashboard import views
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import PasswordChangeView


# Create your views here.
urlpatterns=[
    path('dash/',views.dashview),

    path('addcat/',views.addcatview.as_view()),
    path('mancat/',views.mancatview),
    path('insertcategory/',views.insertcategory),
    path('editcat/<int:id>',views.editcat),
    path('deletecat/<int:id>',views.deletecat),
    path('updatecat/<int:id>',views.updatecat),

    path('addpro/',views.addproview),
    path('manpro/',views.manproview),
    path('insertproduct/',views.insertproduct),
    path('editpro/<int:id>',views.editpro),
    path('deletepro/<int:id>',views.deletepro),
    path('updatepro/<int:id>',views.updatepro),
    path('viewpro/<int:id>',views.viproview),
    
    path('orderlist/',views.orderlistview),

    path('custlist/',views.custlistview.as_view()),

    path('profile/',views.profileview),
     
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),

    path('supplier/',views.supplierview),
    path('addsupplier/',views.addsupplierview),
    path('insertsupplier/',views.insertsupplier),
    path('editsupplier/<int:id>',views.editsupplier),
    path('deletesupplier/<int:id>',views.deletesupplier),
    path('updatesupplier/<int:id>',views.updatesupplier),

    path('stock/',views.stockview),
    
    path('purchase/',views.purchaseview),
    path('addpurchase/',views.addpurchaseview),
    path('insertpurchase/',views.insertpurchase),
    path('editpurchase/<int:id>',views.editpurchase),
    path('deletepurchase/<int:id>',views.deletepurchase),
    path('updatepurchase/<int:id>',views.updatepurchase),
    
    path('invoice/',views.invoiceview),
    path('invgenerate/<int:id>',views.invgenerateview),

    path('feedback/',views.feedview),

    path('change_password/',views.change_passwordview,name='change_password'),
]