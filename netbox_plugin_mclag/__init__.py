from extras.plugins import PluginConfig

class NetBoxMcLagConfig(PluginConfig):
    name = 'netbox_plugin_mclag'
    verbose_name = 'NetBox Multi-Chassis LAG'
    description = 'Manage Multi-Chassis Link Aggregation Groups in Netbox (MC-LAG / MLAG / vPC / etc)'
    version = '0.1'
    base_url = 'mclag'

config = NetBoxMcLagConfig