from django.urls import path
from . import views 

urlpatterns = [
    path('api/paris/', views.PariListCreateAPIView.as_view(), name='paris'),
    path('parier/', views.parier_view, name='parier'),
    path('parier/<int:match_id>/', views.parier_detail, name='parier_detail'),
]
