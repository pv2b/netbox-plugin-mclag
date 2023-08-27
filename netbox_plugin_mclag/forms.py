from django import forms

from netbox.forms import NetBoxModelForm
from .models import McDomain, McLag

class McDomainForm(NetBoxModelForm):
    class Meta:
        model = McDomain
        fields = ('name', 'domain_id', 'description', 'devices', 'tags')

class McLagForm(NetBoxModelForm):
    interfaces = DynamicModelMultipleChoiceField(
        queryset = Interface.objects.all(),
        selector = True
    )
    class Meta:
        model = McLag
        fields = ('name', 'lag_id', 'description', 'mc_domain', 'tags', 'interfaces')