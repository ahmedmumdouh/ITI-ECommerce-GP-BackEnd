from django.urls import path , include

from . import views
from django.conf.urls.static import static
from django.conf import settings
#from .views import SearchResultsView

from rest_framework import routers

r_product = routers.DefaultRouter()
r_product.register('',views.product_list)

r_product_imgs = routers.DefaultRouter()
r_product_imgs.register('',views.product_list_imgs)

app_name='product'


urlpatterns = [
    path('Product/apis/', include(r_product.urls)),
    path('ProductImgs/apis/', include(r_product_imgs.urls)),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)