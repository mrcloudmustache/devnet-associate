import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Declare local variables
api_path = "https://10.10.20.85/dna"
auth = ("admin", "Cisco1234!")
headers = {"Content-Type": "application/json"}

def get_token():
    """
    Get acccess token from Cisco DNA Center
    """

    # Issue HTTP POST request to URL to request a token
    auth_resp = requests.post(
        f"{api_path}/system/api/v1/auth/token", auth=auth, headers=headers, verify=False
    )
    # If succesful, print token. Else, raise HTTPError with details
    auth_resp.raise_for_status()
    token =auth_resp.json()["Token"]
    return token

def get_devices():
    """
    Get devices from Cisco DNA Center
    """
    headers = {"Content-Type": "application/json", "X-Auth-Token": get_token()}
    auth_resp = requests.get(f"{api_path}/dna/intent/api/v1/netork-device", headers=headers, verify=False)
    devices = auth_resp.json()
    return devices

    



def main():
    """
    Execution starts here
    """

    devices = get_devices()
    print(devices)

if __name__ == "__main__":
    main()
