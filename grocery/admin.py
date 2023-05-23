from django.contrib import admin
from grocery.models import *
# Register your models here.


@admin.register(contact1)
class contactadmin(admin.ModelAdmin):
    list_display=('name','phone','email','address','message')


@admin.register(newsletter)
class newsletteradmin(admin.ModelAdmin):
    list_display=('email',)

@admin.register(faq)
class faqadmin(admin.ModelAdmin):
    pass

@admin.register(review)
class reviewadmin(admin.ModelAdmin):
    pass


@admin.register(like)
class likeadmin(admin.ModelAdmin):
    pass

@admin.register(fav)
class favadmin(admin.ModelAdmin):
    pass