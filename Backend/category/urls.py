from django.urls import path , include

from . import views
#from .views import SearchResultsView

from rest_framework import routers

r_category = routers.DefaultRouter()
r_category.register('',views.category_list)



app_name='category'


urlpatterns = [
    path('Category/apis/', include(r_category.urls)),

]