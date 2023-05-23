from django.urls import path
from grocery import views
from django.contrib.auth.views import LoginView, LogoutView,PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView

# Create your views here.
urlpatterns=[
    path('login1/',views.loginview.as_view()),
    path('register1/',views.registerview.as_view()),
    path('log1/',views.logview.as_view()),
    path('home/',views.homeview),
    path('contact/',views.contactview.as_view()),
    path('legal/',views.legalview.as_view()),
    path('terms/',views.termsview.as_view()),
    path('insertcontact/',views.insertcontact),
    path('subscribe/',views.subscribe),
    path('productdetails/<int:id>',views.productdetailsview),
    path('product/<int:id>',views.productview),
    path('fruveg/',views.fruvegview.as_view()),
    path('grains/',views.grainsview.as_view()),
    path('dairy/',views.dairyview.as_view()),
    path('meategg/',views.meateggview.as_view()),
    path('faq/',views.faqview),
    path('search_res/',views.searchview),
    path('signup/',views.signup),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('logincustomer/',views.logincustomer),
    path('shop/',views.shopview),
    path('shopfilter/<int:id>',views.shopfilterview),
    path('dolike/',views.dolike),
    path('dofav/',views.dofav),
    path('fav/',views.favview),
    path('myorder/',views.myorderview),
    path('insertreview/',views.insertreview),
    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
]