from django.urls import path
from . import views

urlpatterns = [
    path('parier/', views.parier_view, name='parier'),
    path('parier/<int:match_id>/', views.parier_detail, name='parier_detail'),
    path('historique/', views.historique_view, name='historique'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]
