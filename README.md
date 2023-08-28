# netbox-plugin-mclag

## WORK IN PROGRESS

This plugin is currently a work in progress and is currently functional but untested.

## Description

This project aims to create a NetBox Plugin to manage MC-LAG ([Multi-Chassis Link Aggregation Groups](https://en.wikipedia.org/wiki/Multi-chassis_link_aggregation_group)).

MC-LAG is a generic name for vendor-specific technologies allowing multiple switches to form a common LAG with a remote system. In the interest of discoverability, here is a list of various vendor-specific names for MC-LAG technologies.

 * CLAG
 * Distributed Resilient Network Interconnect
 * Distributed Split Multi-Link Trunking
 * Distributed Trunking
 * MC-LAG
 * mLACP (Multichassis Link Aggregation Control Protocol)
 * MLAG
 * M-LAG
 * Multichassis Etherchannel (MEC)
 * Multi-Chassis Trunking
 * Split multi-link trunking
 * StackWise Virtual
 * Virtual Link Trunking
 * Virtual Port Channel (vPC)
 * vLAG

The plugin itself aims be vendor-neutral, and to use vendor-neutral terminology, and to fit most common MC-LAG implementations. Cisco Nexus Virtual Port Channel (vPC) will be used as a sample implementation in examples.

## Data model

This plugin will creates two new data models, a *Multi-Chassis Domain* and an *Multi-Chassis Link Aggregation Group*.

A *Multi-Chassis Domain* groups two or more devices that participate in creating a *Multi-Chassis Link Aggregation Group*. Optionally, a *Domain ID* may be added here to hold any vendor-specific ID required for configuration of the domain.

A *Multi-Chassis Link Aggregation Group* groups two or more LAG interfaces on domain member devices. Optionally, a *Group ID* may be added here to hold any vendor-specific ID required for configuration of the group.

To clarify, each switch in the Multi-Chassis Domain will need a regular NetBox LAG interface created, typically just with a single physical interface associated with it. These LAGs are then grouped together by the data models described above.

Here is an example configuration of an MC-LAG setup containing two peer devices, each with one physical participating in a single LAG, using Cisco Nexus vPC terminology.

  * A *Multi-Chassis Domain* named *My VPC Domain*, with *Domain ID* set to 100. This corresponds to the Cisco vPC Domain ID.
  * A *Multi-Chassis Link Aggregation Group* named *My VPC Group*, with *Group ID* set to 200. This corresponds to the Cisco VPC number assigned to the virtual port channel.
  * On each member device *Switch1* and *Switch2*
    * A LAG interface named *Po200*, representing the local port channel configuration.
    * A physical interface named *Te1/0/1* which is a member of the *Po200* LAG.

If more configuration fields beyond an ID are required on the *Multi-Chassis Domain* or *Multi-Chassis Link Aggregation Group* objects, they may be added as [custom fields](https://docs.netbox.dev/en/stable/customization/custom-fields/) by the user.

## Functionality

The following functionality is offered by this plugin to create a minimum viable product:

  * The ability to view/create/update/delete *Multi-Chassis Domain* objects through the web UI and by API.
  * The ability to view/create/update/delete *Multi-Chassis Link Aggregation Group* objects through the web UI and by API.
  * Button added to Device view to "Show MC Domain" if a device is associated with an MC Domain
  * Butten added to Interface fiew to "Show MC-LAG" if an interface is associated with an MC-LAG

## Configuration template example

The following example proof-of-concept template demonstrates that the model contains the required richness to model Cisco VPC. It's incomplete and will require some improvement before it can actually be used for anything:

```jinja2
{% if device.mc_domains.count() == 1 %}
feature vpc
vpc domain {{ device.mc_domains.get().domain_id }}
  peer-keepalive destination 10.1.1.20 source 10.1.1.10 vrf VPC-KEEPALIVE ### TODO Actually populate IP addresses and VRF names here ###
exit

interface port-channel 1 ### TODO actually figure out correct interface ###
  vpc peer-link
exit
{% endif %}

{%- for interface in device.interfaces.filter(type='lag') %}
{%-   if interface.mc_lags.count() == 1 %}
interface {{ interface.name }}
  vpc {{ interface.mc_lags.get().lag_id }}
exit
{%-   endif %}
{%- endfor %}
{%  for interface in device.interfaces.filter(lag__isnull=False) %}
interface {{ interface.name }}
  channel-group {{ interface.lag.name|replace("Po","") }} mode active
exit
{%  endfor %}
```

## Acknowledgements and references

The following materials were instrumental in developing this plugin:

 * The [NetBox Plugin Development Tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)
 * The [Plugins Development](https://docs.netbox.dev/en/stable/plugins/development/) chapter of the NetBox documentation.
 * The Wikipedia page for [Multi-Chassis Link Aggregation Groups](https://en.wikipedia.org/wiki/Multi-chassis_link_aggregation_group)
 * The [Virtual Port Channels](https://www.ciscopress.com/articles/article.asp?p=3150966&seqNum=2) section of the [Port Channels and vPCs chapter](https://www.ciscopress.com/articles/article.asp?p=3150966) from the [Cisco Data Center Fundamentals](https://www.ciscopress.com/store/cisco-data-center-fundamentals-9780137638246) by [Somit Maloo](https://www.ciscopress.com/authors/bio/75b726d0-f107-4c19-98bd-77d9f3558184) and [Iskren Nikolov](https://www.ciscopress.com/authors/bio/301612bc-152f-4827-b31e-ab7a1dd35c61), published by [Cisco Press](https://www.ciscopress.com/).