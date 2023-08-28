from netbox.views import generic
from . import forms, models, tables
from dcim.tables.devices import InterfaceTable

class McDomainView(generic.ObjectView):
    queryset = models.McDomain.objects.all()

class McDomainListView(generic.ObjectListView):
    queryset = models.McDomain.objects.all()
    table = tables.McDomainTable

class McDomainEditView(generic.ObjectEditView):
    queryset = models.McDomain.objects.all()
    form = forms.McDomainForm

class McDomainDeleteView(generic.ObjectDeleteView):
    queryset = models.McDomain.objects.all()

class McLagView(generic.ObjectView):
    queryset = models.McLag.objects.all()
    def get_extra_context(self, request, instance):
        table = InterfaceTable(instance.interfaces.all())
        table.configure(request)
        return {
            'interfaces_table': table,
        }

class McLagListView(generic.ObjectListView):
    queryset = models.McLag.objects.all()
    table = tables.McLagTable

class McLagEditView(generic.ObjectEditView):
    queryset = models.McLag.objects.all()
    form = forms.McLagForm

class McLagDeleteView(generic.ObjectDeleteView):
    queryset = models.McLag.objects.all()

