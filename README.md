# netbox-plugin-mclag

## WORK IN PROGRESS

This plugin is currently a work in progress and is not currently in a functional state!

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

The following functionality must be offered by this plugin to create a minimum viable product:

  * The ability to view/create/update/delete *Multi-Chassis Domain* objects through the web UI and by API.
  * The ability to view/create/update/delete *Multi-Chassis Link Aggregation Group* objects through the web UI and by API.
  * Adds a "MC-LAG" tab to the interface view. This only shows up if the interface's device is part a *Multi-Chassis Domain*. This view will show:
    * If the interface is a physical interface and has no associated LAG interface, show a descriptive error suggesting the user to create a LAG and add the interface to that LAG first.
    * If the interface is a LAG, and has no associated physical interface, show a descriptive error suggesting the user to associate local device interfaces to that LAG.
    * If the LAG on the local device is not connected to a *Multi-Chassis Link Aggregation Group*, show an informative message that informs the user that this LAG is not part of a *Multi-Chassis Link Aggregation Group*. For convenience, still show a list of associated physical interfaces on the local device.
    * If the LAG on the local device is connected to a *Multi-Chassis Link Aggregation Group*, show cards for the *Multi-Chassis Link Aggregation Group*, and the associated *Multi-Chassis Domain*, along with a list view of associated physical interfaces.
  * Validated ability to generate vPC configurations for the Cisco Nexus platform, as a proof of completeness of the data model, including a provided template sample for this platform.

## Acknowledgements and references

The following materials were instrumental in developing this plugin:

 * The [NetBox Plugin Development Tutorial](https://github.com/netbox-community/netbox-plugin-tutorial)
 * The [Plugins Development](https://docs.netbox.dev/en/stable/plugins/development/) chapter of the NetBox documentation.
 * The Wikipedia page for [Multi-Chassis Link Aggregation Groups](https://en.wikipedia.org/wiki/Multi-chassis_link_aggregation_group)
 * The [Virtual Port Channels](https://www.ciscopress.com/articles/article.asp?p=3150966&seqNum=2) section of the [Port Channels and vPCs chapter](https://www.ciscopress.com/articles/article.asp?p=3150966) from the [Cisco Data Center Fundamentals](https://www.ciscopress.com/store/cisco-data-center-fundamentals-9780137638246) by [Somit Maloo](https://www.ciscopress.com/authors/bio/75b726d0-f107-4c19-98bd-77d9f3558184) and [Iskren Nikolov](https://www.ciscopress.com/authors/bio/301612bc-152f-4827-b31e-ab7a1dd35c61), published by [Cisco Press](https://www.ciscopress.com/).