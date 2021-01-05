#! /usr/bin/env python
from dnacentersdk import api

# Create a DNACenterAPI connection object;
# it uses DNA Center sandbox URL, username and password
DNAC = api.DNACenterAPI(username="devnetuser", password="Cisco123!", base_url="https://sandboxdnac2.cisco.com")

# Find all devices
DEVICES = DNAC.devices.get_device_list()

# Print select information about the retrieved devices
for DEVICE in DEVICES.response:
    print(DEVICE.hostname)
    print(DEVICE.type)
    print(DEVICE.id)
    print('-'*25)

# Get a specfic device 
device = DNAC.devices.get_device_by_id('5bc5b967-3f83-4195-891c-788f3e9048f3').response
print(device.hostname)

# Get the health of all clients on Thursday, August 22, 2019 8:41:29 PM GMT
# CLIENTS = DNAC.clients.get_overall_client_health(timestamp="1566506489000")

# # Print select information about the retrieved client health statistics
# print('{0:25s}{1:1}{2:45s}{3:1}{4:15s}'.format("Client Category", "|",\
#     "Number of Clients", "|", "Clients Score"))
# print('-'*95)
# for CLIENT in CLIENTS.response:
#     for score in CLIENT.scoreDetail:
#         print('{0:25s}{1:1}{2:<45d}{3:1}{4:<15d}'.format(
#             score.scoreCategory.value, "|", score.clientCount, "|", \
#             score.scoreValue))
# print('-'*95)