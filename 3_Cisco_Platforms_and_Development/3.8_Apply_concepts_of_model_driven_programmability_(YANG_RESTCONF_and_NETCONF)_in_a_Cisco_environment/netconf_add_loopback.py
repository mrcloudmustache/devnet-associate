#!/usr/bin/env python
"""This script retrieves the list of interfaces from a device using NETCONF

Copyright (c) 2018 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import os
import sys
from ncclient import manager
import xmltodict
import xml.dom.minidom


# Create an XML filter for targeted NETCONF queries
netconf_data = """
<config xmlns:xc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
         <interface>
             <name>Loopback1</name>
             <description>My loopback not yours</description>
             <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                 ianaift:softwareLoopback
             </type>
             <enabled>true</enabled>
             <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                 <address>
                     <ip>100.100.100.100</ip>
                     <netmask>255.255.255.255</netmask>
                 </address>
             </ipv4>
         </interface>
     </interfaces>
 </config>"""

print("Opening NETCONF Connection to cs1000v")

# Open a connection to the network device using ncclient
with manager.connect(
        host="192.168.86.200",
        port="830",
        username="cisco",
        password="cisco",
        hostkey_verify=False
        ) as m:

    print("Sending a <get-config> operation to the device.\n")
    # Make a NETCONF <get-config> query using the filter
    netconf_reply = m.edit_config(netconf_data,target="running")

print("Here is the raw XML data returned from the device.\n")
# Print out the raw XML that returned
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
print("")

# Parse the returned XML to an Ordered Dictionary
# netconf_data = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]

# Create a list of interfaces
#interfaces = netconf_data["interfaces"]["interface"]

#print("The interface status of the device is: ")
# Loop over interfaces and report status
# for interface in interfaces:
#     print("Interface {} enabled status is {}".format(
#             interface["name"],
#             interface["enabled"]
#             )
#         )
# print("\n")
