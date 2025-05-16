from django.urls import path
from .views import PariListCreateAPIView

urlpatterns = [
    path('', PariListCreateAPIView.as_view(), name='paris'),
]
