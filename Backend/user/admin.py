from django.contrib import admin
from .models import Puser
# Register your models here.


# class PuserAdmin (admin.ModelAdmin):
#     search_fields = ['full_name','email','password','address','phone']
#     list_filter = ['full_name','email','password','address','phone' ] 
#     list_display = ['full_name','email','password','address','phone']


admin.site.register(Puser)