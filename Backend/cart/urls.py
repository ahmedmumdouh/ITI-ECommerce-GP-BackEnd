from django.urls import path , include

from . import views
#from .views import SearchResultsView

from rest_framework import routers

r_cart = routers.DefaultRouter()
r_cart.register('',views.cart_list)

r_cart_item = routers.DefaultRouter()
r_cart_item.register('',views.cart_item)



app_name='cart'


urlpatterns = [
    path('Cart/apis/', include(r_cart.urls)),
    path('CartItem/apis/', include(r_cart_item.urls)),

]