from django.urls import path , include

from . import views
#from .views import SearchResultsView

from rest_framework import routers

r_buy = routers.DefaultRouter()
r_buy.register('',views.buy_item)





app_name='buy'


urlpatterns = [
    path('Buy/apis/', include(r_buy.urls)),
]