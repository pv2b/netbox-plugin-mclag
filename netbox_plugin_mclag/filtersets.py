from netbox.filtersets import NetBoxModelFilterSet
from dcim.models import Interface
from .models import McDomain
from django_filters import ModelMultipleChoiceFilter

class McInterfaceFilterSet(NetBoxModelFilterSet):
    mc_domain = ModelMultipleChoiceFilter(
        field_name='device__mc_domains',
        queryset=McDomain.objects.all()
    )
    
    class Meta:
        model = Interface
        fields = ['id', 'mc_domain']