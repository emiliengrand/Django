from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import home  
from parions.views import regles_view

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),  
    path('api/paris/', include('parions.urls_paris')),      
    path('parions/', include('parions.urls_web')), 
    path('regles/', regles_view, name='regles'),
]
