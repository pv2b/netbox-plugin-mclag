from django import forms

from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelMultipleChoiceField
from utilities.forms.widgets import APISelectMultiple
from dcim.models import Interface
from .models import McDomain, McLag
from django.db.models.functions import Concat

class McDomainForm(NetBoxModelForm):
    class Meta:
        model = McDomain
        fields = ('name', 'domain_id', 'description', 'devices', 'tags')

class McInterfaceMultipleChoiceField(DynamicModelMultipleChoiceField):
    def label_from_instance(self, interface):
        return f"{interface.device.name} {interface.name}"

class McLagForm(NetBoxModelForm):
    interfaces = McInterfaceMultipleChoiceField(
        queryset = Interface.objects.all(),
        selector = True,
        query_params = {
            'mc_domain': '$mc_domain',
            'brief': 'false'
        },
        widget=APISelectMultiple(
            api_url='/api/plugins/mclag/interfaces/'
        )
    )
    class Meta:
        model = McLag
        fields = ('name', 'lag_id', 'description', 'mc_domain', 'tags', 'interfaces')