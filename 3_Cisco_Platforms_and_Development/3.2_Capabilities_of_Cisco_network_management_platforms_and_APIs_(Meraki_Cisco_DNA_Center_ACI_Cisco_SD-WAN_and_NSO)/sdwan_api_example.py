import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from pprint import pprint

# Set URL and login body
# Note the body is a python dictionary = NOT a JSON body

url = 'https://sandbox-sdwan-1.cisco.com/j_security_check'
login_body = {'j_username': 'devnetuser', 'j_password': 'RG!_Yw919_83'}

# MUST use a session for SD-WAN
session = requests.session()

response = session.post(url, data=login_body, verify=False)

# Response returns a 200 OK no matter what
# IF the response body contains any text then auth failed
if not response.ok or response.text:
    print('login failure')
    import sys
    sys.exit(1)
else:
    print('login worked! Yay!')

# Get devices
url = 'https://sandbox-sdwan-1.cisco.com/dataservice/device'

device_response = session.get(url, verify=False).json()['data']

for device in device_response:
    print(f"Hostname: {device['host-name']}")
    ip = device['local-system-ip']
    print(f"IP: {device['local-system-ip']}")
    print(f"Model: {device['device-model']}")

# pprint(device_response)
