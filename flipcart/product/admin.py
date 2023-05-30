from django.contrib import admin

from .models import Product, Customer
from .category import Category
class productinfo(admin.ModelAdmin):
    list_display=['id','name','category','price']

admin.site.register(Product,productinfo)
class catinfo(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Category,catinfo)
admin.site.register(Customer)
