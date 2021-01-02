import requests, json, urllib3
urllib3.disable_warnings()

url = "https://api.meraki.com/api/v0/organizations"

payload={}
headers = {
  'Accept': 'application/json',
  'X-Cisco-Meraki-API-Key': '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
}

# GET Organizations https://developer.cisco.com/meraki/api/#!get-organizations
response = requests.get(url, headers=headers, data=payload, verify=False).json()

for orgs in response:
    if orgs['name'] == "DevNet Sandbox":
        organizationId = orgs['id']


\
print(f"DevNet Sandbox Org ID: {organizationId}")

# GET Organization Networks https://developer.cisco.com/meraki/api/#!get-organization-networks
url = f"https://api.meraki.com/api/v0/organizations/{organizationId}/networks"
response = requests.get(url, headers=headers, data=payload, verify=False).json()

# print(json.dumps(response, indent=2, sort_keys=True))

for nets in response:
    if nets['name'] == "DevNet Sandbox ALWAYS ON":
        networkId = nets['id']

print(f"DevNet Always On Network ID: {networkId}")

# GET Network Devices https://developer.cisco.com/meraki/api/#!get-network-devices
url = f"https://api.meraki.com/api/v0/networks/{networkId}/devices"
response = requests.get(url, headers=headers, data=payload, verify=False).json()

print("DevNet Always On Network Devices")
print(json.dumps(response, indent=2, sort_keys=True))








