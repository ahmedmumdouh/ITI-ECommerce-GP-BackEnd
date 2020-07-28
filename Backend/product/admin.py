from django.contrib import admin

from .models import Product , ProductImgs
# Register your models here.


class ProductAdmin (admin.ModelAdmin):
    search_fields = ['name','desc','quantity','price','created_date','supplier','category','photo','in_stock']
    list_filter = ['name','desc','quantity','price','created_date','supplier','category','photo','in_stock' ] 
    list_display = ['name','desc','quantity','price','created_date','supplier','category','photo','in_stock']


admin.site.register(Product , ProductAdmin)
# Register your models here.

class ProductImgsAdmin (admin.ModelAdmin):
    search_fields = ['product','photos']
    list_filter = ['product','photos'] 
    list_display = ['product','photos']


admin.site.register(ProductImgs , ProductImgsAdmin)

    
