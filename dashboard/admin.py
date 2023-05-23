from django.contrib import admin
from dashboard.models import *
# Register your models here.

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    pass

@admin.register(Supplier)
class Supplieradmin(admin.ModelAdmin):
    pass

@admin.register(Purchase)
class Purchaseadmin(admin.ModelAdmin):
    pass

@admin.register(Employeprofile)
class Employeprofileadmin(admin.ModelAdmin):
    pass