from rest_framework import viewsets

from fridge.models import Fridge

from fridge.serializers import FridgeSerializer


class FridgeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Fridge.objects.all()
    serializer_class = FridgeSerializer
