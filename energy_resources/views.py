from rest_framework import viewsets
from .models import EnergyResource
from .serializers import EnergyResourceSerializer

class EnergyResourceViewSet(viewsets.ModelViewSet):
    queryset = EnergyResource.objects.all().order_by('name')
    serializer_class = EnergyResourceSerializer
