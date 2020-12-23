import requests

url = "https://192.168.86.200:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1"

payload={}
headers = {
  'Accept': 'application/yang-data+json, application/yang-data.errors+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

print(response.text)