#! user/bin/env python
import pprint, requests, json

base_url = "https://api.meraki.com/api/v0"

# Get list of Organizations
orgs = "/organizations"
headers = {"X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"}

response = requests.get(base_url + orgs, headers=headers )

# pprint.pprint(response.json())

# Get list of single organization
organization_id = "463308"
org = f"/organizations/{organization_id}"

response = requests.get(base_url + org, headers=headers)

# pprint.pprint(response.json())

# Get list of organziation networks
org_networks = f"/organizations/{organization_id}/networks"
response = requests.get(base_url + org_networks, headers=headers)

# pprint.pprint(response.json())

# Get list of network devices
network_id = 'L_573083052582908089'
network_devices = f"/networks/{network_id}/devices"

response = requests.get(base_url + network_devices, headers=headers)

devices = response.json()

for device in devices:
    #print(device)
    print(f"Model: {device['model']} Name: {device['serial']}")


# pprint.pprint(devices.json())



