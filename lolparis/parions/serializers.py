from rest_framework import serializers
from .models import Pari

class PariSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pari
        fields = '__all__'