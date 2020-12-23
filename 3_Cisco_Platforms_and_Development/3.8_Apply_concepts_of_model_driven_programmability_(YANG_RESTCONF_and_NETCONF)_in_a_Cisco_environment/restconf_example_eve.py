import requests
import json

router = {"ip": "192.168.86.200", "port": "443",
          "user": "cisco", "password": "cisco"}

headers = {"Accept": "application/yang-data+json,application/yang-data.errors+json",
           "Content-Type": "application/yang-data+json"}

url = f"https://{router['ip']}:{router['port']}/restconf/data/ietf-interfaces::interfaces/interface=GigabitEthernet1"


response = requests.get(url, headers=headers, auth=(
    router['user'], router['password']), verify=False)


api_data = response.json()
print("/" * 50)
print(api_data["ietf-interfaces:interface"]["description"])
print("/" * 50)
if api_data["ietf-interfaces:interface"]["enabled"] == True:
    print('Interface is up')