from netbox.views import generic
from . import forms, models, tables

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

class McLagListView(generic.ObjectListView):
    queryset = models.McLag.objects.all()
    table = tables.McLagTable

class McLagEditView(generic.ObjectEditView):
    queryset = models.McLag.objects.all()
    form = forms.McLagForm

class McLagDeleteView(generic.ObjectDeleteView):
    queryset = models.McLag.objects.all()
