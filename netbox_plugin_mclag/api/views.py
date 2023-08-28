from netbox.api.viewsets import NetBoxModelViewSet, NetBoxReadOnlyModelViewSet

from .. import models
from .serializers import McLagSerializer, McDomainSerializer, McInterfaceSerializer
from ..filtersets import McInterfaceFilterSet
from dcim.models import Interface

class McDomainViewSet(NetBoxModelViewSet):
    queryset = models.McDomain.objects.prefetch_related('tags')
    serializer_class = McDomainSerializer

class McLagViewSet(NetBoxModelViewSet):
    queryset = models.McLag.objects.prefetch_related('mc_domain', 'tags')
    serializer_class = McLagSerializer

class McInterfaceViewSet(NetBoxReadOnlyModelViewSet):
    # Force disabling of brief mode that is implemented in the BriefModeMixin.
    # We don't want to support brief mode at all (it doesn't do what we want it to,
    # it ends up using a different serializer than the custom one we're trying to use)
    # and there's no way to stop apiSelect.ts from including the brief flag, so we just
    # do this stupid thing to ignore the brief flag.
    def initialize_request(self, request, *args, **kwargs):
        ret = super().initialize_request(request, *args, **kwargs)
        self.brief = False
        return ret
    queryset = Interface.objects.prefetch_related('device')
    serializer_class = McInterfaceSerializer
    filterset_class = McInterfaceFilterSet