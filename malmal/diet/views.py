from rest_framework import viewsets

from diet.models import Diet
from diet.serializers import DietSerializer


class DietViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
