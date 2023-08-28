from extras.plugins import PluginTemplateExtension
from .models import McDomain, McLag

class McLagInterfaceExtensions(PluginTemplateExtension):
    model="dcim.interface"
    def buttons(self):
        interface = self.context['object']

        if interface.type == 'lag':
            mc_lag = interface.mc_lags.get()
        elif interface.lag:
            mc_lag = interface.lag.mc_lags.get()
        else:
            mc_lag = None

        if mc_lag:
            return self.render('netbox_plugin_mclag/interface_buttons.html', extra_context={
                'mc_lag_id': mc_lag.id
            })
        else:
            return ""

class McLagDeviceExtensions(PluginTemplateExtension):
    model="dcim.device"
    def buttons(self):
        device = self.context['object']

        mc_domain = device.mc_domains.get()

        if mc_domain:
            return self.render('netbox_plugin_mclag/device_buttons.html', extra_context={
                'mc_domain_id': mc_domain.id
            })
        else:
            return ""

template_extensions = [McLagInterfaceExtensions, McLagDeviceExtensions]