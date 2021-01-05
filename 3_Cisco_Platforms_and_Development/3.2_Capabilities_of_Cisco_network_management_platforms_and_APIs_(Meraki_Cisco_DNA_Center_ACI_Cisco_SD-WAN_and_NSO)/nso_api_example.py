import requests
import pprint

url = "http://192.168.86.31:8080/restconf/data/tailf-ncs:devices/"

payload={}
headers = {
  #'Authorization': 'Basic YWRtaW46YWRtaW4='
  'Content-Type': 'application/yang-data+json'
}

response = requests.get(url, headers=headers,auth=('admin', 'admin'), data=payload).json()


pprint.pprint(response)