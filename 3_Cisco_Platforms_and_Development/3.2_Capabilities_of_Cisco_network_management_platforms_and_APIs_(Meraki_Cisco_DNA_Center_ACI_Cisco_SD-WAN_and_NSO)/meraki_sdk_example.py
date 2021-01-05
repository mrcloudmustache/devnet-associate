import meraki
import json
from pprint import pprint

token = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

dashboard = meraki.DashboardAPI(token)

# Get list of oranizations
organizations = dashboard.organizations.getOrganizations()

for org in organizations:
    print(f'\nAnalyzing oganization {org["name"]}')
    if org['name'] == "DevNet Sandbox":
        org_id = org['id']

pprint(f"DevNet Sandbox Organization ID: {org_id}")

params = {}
params['organization_id'] = org_id

# Get list of networks
networks = dashboard.organizations.getOrganizationNetworks(org_id)
dashboard.organizations.get

pprint(networks)


