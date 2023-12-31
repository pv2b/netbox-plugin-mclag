from netbox.views import generic
from . import forms, models, tables
from dcim.models import Interface
from dcim.tables.devices import InterfaceTable
from .filtersets import McDomainFilterSet, McLagFilterSet
from .tables import McLagTable

class McDomainView(generic.ObjectView):
    queryset = models.McDomain.objects.all()
    def get_extra_context(self, request, instance):
        mclag_table = McLagTable(instance.mc_lags.all())
        mclag_table.configure(request)

        return {
            'mclag_table': mclag_table,
        }

class McDomainListView(generic.ObjectListView):
    queryset = models.McDomain.objects.all()
    table = tables.McDomainTable
    filterset = McDomainFilterSet

class McDomainEditView(generic.ObjectEditView):
    queryset = models.McDomain.objects.all()
    form = forms.McDomainForm

class McDomainDeleteView(generic.ObjectDeleteView):
    queryset = models.McDomain.objects.all()

class McLagView(generic.ObjectView):
    queryset = models.McLag.objects.all()
    def get_extra_context(self, request, instance):
        lag_interfaces_table = InterfaceTable(instance.interfaces.all())
        lag_interfaces_table.configure(request)

        physical_interfaces_table = InterfaceTable(Interface.objects.filter(lag__mc_lags=instance))
        physical_interfaces_table.configure(request)
        return {
            'lag_interfaces_table': lag_interfaces_table,
            'physical_interfaces_table': physical_interfaces_table,
        }

class McLagListView(generic.ObjectListView):
    queryset = models.McLag.objects.all()
    table = tables.McLagTable
    filterset = McLagFilterSet

class McLagEditView(generic.ObjectEditView):
    queryset = models.McLag.objects.all()
    form = forms.McLagForm

class McLagDeleteView(generic.ObjectDeleteView):
    queryset = models.McLag.objects.all()

