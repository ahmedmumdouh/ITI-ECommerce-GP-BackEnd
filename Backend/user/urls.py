from django.urls import path , include
from rest_framework.authtoken import views as authViews

from . import views
from django.conf.urls.static import static
from django.conf import settings

# r_puser = routers.DefaultRouter()
# r_puser.register('',views.PUserListApi)

# r_user = routers.DefaultRouter()
# r_user.register('',views.UserListApi)

app_name='user'


urlpatterns = [
    # path('Puser/apis/', include(r_puser.urls)),
    # path('user/apis/', include(r_user.urls)),
    path('api/pusers/', views.PUserListAPI.as_view()),
    path('api/puserdetails/<int:pk>/', views.PUserDetailAPI.as_view()),
    path('api/users/', views.UserListAPI.as_view()),
    path('api/userdetails/<int:pk>/', views.UserDetailAPI.as_view()),
    path('api/tokens/', views.TokenAPI.as_view()), 
    path('api/users-auth/', authViews.obtain_auth_token),
    path('api/users-login/', views.CustomObtainAuthToken.as_view()),
    path('api/loggedin/<int:pk>', views.logged_in_user),
     
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)