from django.conf import settings
from extras.plugins import PluginMenuButton, PluginMenuItem, PluginMenu
from utilities.choices import ButtonColorChoices


mc_domain_buttons = [
    PluginMenuButton(
        link='plugins:netbox_plugin_mclag:mcdomain_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

mc_lag_buttons = [
    PluginMenuButton(
        link='plugins:netbox_plugin_mclag:mclag_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.GREEN
    )
]

_menu_items = (
    PluginMenuItem(
        link='plugins:netbox_plugin_mclag:mcdomain_list',
        link_text='Multi-Chassis Domains',
        buttons=mc_domain_buttons
    ),
    PluginMenuItem(
        link='plugins:netbox_plugin_mclag:mclag_list',
        link_text='Multi-Chassis LAGs',
        buttons=mc_lag_buttons
    ),
)

plugin_settings = settings.PLUGINS_CONFIG.get('netbox_plugin_mclag', {})

if plugin_settings.get('top_level_menu'):
    menu = PluginMenu(
        label="MC-LAG",
        groups=(("MC-LAG", _menu_items),),
        icon_class="mdi mdi-alpha-m-box",
    )
else:
    menu_items = _menu_items
