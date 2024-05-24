from netbox.plugins import PluginConfig


class NetBoxMcLagConfig(PluginConfig):
    name = "netbox_plugin_mclag"
    verbose_name = "Multi-Chassis LAG"
    description = "Manage Multi-Chassis Link Aggregation Groups in Netbox (MC-LAG / MLAG / vPC / etc)"
    version = "0.2.0"
    base_url = "mclag"


config = NetBoxMcLagConfig
