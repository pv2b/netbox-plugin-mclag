from netbox.api.viewsets import NetBoxModelViewSet

from .. import models
from .serializers import McLagSerializer, McDomainSerializer


class McDomainViewSet(NetBoxModelViewSet):
    queryset = models.McDomain.objects.prefetch_related('tags')
    serializer_class = McDomainSerializer

class McLagViewSet(NetBoxModelViewSet):
    queryset = models.McLag.objects.prefetch_related('mc_domain', 'tags')
    serializer_class = McLagSerializer

