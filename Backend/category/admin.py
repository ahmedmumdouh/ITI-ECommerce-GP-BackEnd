from django.contrib import admin

from .models import Category
# Register your models here.


class CategoryAdmin (admin.ModelAdmin):
    search_fields = ['name','desc']
    list_filter = ['name','desc' ] 
    list_display = ['name','desc']


admin.site.register(Category , CategoryAdmin)
