from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','created','edited']
    list_filter = ['name','edited']
    list_editable = ['price','stock']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Product,ProductAdmin)