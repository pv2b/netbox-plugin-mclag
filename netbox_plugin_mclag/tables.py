import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import McDomain, McLag

class McDomainTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        name = tables.Column(linkify=True)
        model = McDomain
        fields = ('pk', 'id', 'name', 'domain_id', 'description', 'actions')
        default_columns = ('name', 'domain_id')

class McLagTable(NetBoxTable):
    class Meta(NetBoxTable.Meta):
        name = tables.Column(linkify=True)
        model = McLag
        fields = ('pk', 'id', 'name', 'lag_id', 'description', 'mc_domain', 'actions')
        default_columns = ('name', 'mc_domain', 'lag_id')
