from django.conf import settings
from netbox.plugins import PluginMenuButton, PluginMenuItem, PluginMenu


mc_domain_buttons = [
    PluginMenuButton(
        link="plugins:netbox_plugin_mclag:mcdomain_add",
        title="Add",
        icon_class="mdi mdi-plus-thick"
    )
]

mc_lag_buttons = [
    PluginMenuButton(
        link="plugins:netbox_plugin_mclag:mclag_add",
        title="Add",
        icon_class="mdi mdi-plus-thick"
    )
]

_menu_items = (
    PluginMenuItem(
        link="plugins:netbox_plugin_mclag:mcdomain_list",
        link_text="Multi-Chassis Domains",
        buttons=mc_domain_buttons,
    ),
    PluginMenuItem(
        link="plugins:netbox_plugin_mclag:mclag_list",
        link_text="Multi-Chassis LAGs",
        buttons=mc_lag_buttons,
    ),
)

plugin_settings = settings.PLUGINS_CONFIG.get("netbox_plugin_mclag", {})

if plugin_settings.get("top_level_menu"):
    menu = PluginMenu(
        label="MC-LAG",
        groups=(("MC-LAG", _menu_items),),
        icon_class="mdi mdi-alpha-m-box",
    )
else:
    menu_items = _menu_items
