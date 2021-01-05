from acitoolkit.acitoolkit import *

url = "https://sandboxapicdc.cisco.com"
user = "admin"
pw = "ciscopsdt"

# Create session object
session = Session(url, user, pw)

# Login to the session
session.login()

endpoints = Endpoint.get(session)
for endpoint in endpoints:
    epg = endpoint.get_parent()
    print(endpoint)
    # print(endpoint.name)
    # print(endpoint.ip)

tenants = Tenant.get(session)
for tenant in tenants:
    print(tenant.name)

