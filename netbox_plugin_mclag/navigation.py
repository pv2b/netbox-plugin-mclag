from extras.plugins import PluginMenuButton, PluginMenuItem
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

menu_items = (
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