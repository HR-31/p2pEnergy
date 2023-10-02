from rest_framework import serializers
from .models import EnergyResource

class EnergyResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyResource
        fields = '__all__'
