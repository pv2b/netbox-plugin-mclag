from django import forms

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelMultipleChoiceField
from dcim.models import Interface
from .models import McDomain, McLag

class McDomainForm(NetBoxModelForm):
    class Meta:
        model = McDomain
        fields = ('name', 'domain_id', 'description', 'devices', 'tags')

class McLagForm(NetBoxModelForm):
    interfaces = DynamicModelMultipleChoiceField(
        queryset = Interface.objects.all(),
        selector = True,
        query_params = {
            'device__mc_domains': '$mc_domain'
        }
    )
    class Meta:
        model = McLag
        fields = ('name', 'lag_id', 'description', 'mc_domain', 'tags', 'interfaces')