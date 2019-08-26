import requests
import sys

base_url = "https://api.meraki.com/api/v0"
API_key = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
org_name = "DevNet Sandbox"
network_name = "DevNet Always On Read Only"


def org_get(headers, org):
    url = "/organizations"
    full_url = base_url + url

    r = requests.get(full_url, headers=headers)

    org_data = r.json()

    print(org_data)

    for i in org_data:
        if i["name"] == org:
            return i["id"]
    print("Nothing Found. Are you sure you have the org name correct?")
    sys.exit(1)


def net_get(headers, id, net_name):
    url = "/organizations/%s/networks" % id
    full_url = base_url + url

    r = requests.get(full_url, headers=headers)

    net_data = r.json()

    print(net_data)

    for i in net_data:
        if i["name"] == net_name:
            return i["id"]
    print("Nothing Found. Are you sure you have the org name correct?")
    sys.exit(1)


def dev_get(headers, id):
    url = "/networks/%s/devices" % id
    full_url = base_url + url

    r = requests.get(full_url, headers=headers)

    dev_data = r.json()

    print(dev_data)


def main():
    headers = {
        'X-Cisco-Meraki-API-Key': API_key
    }

    print("Getting Org Data")

    org_id = org_get(headers, org_name)

    print(org_id)

    print("Getting Network Data")

    net_id = net_get(headers, org_id, network_name)

    print(net_id)

    print("Getting Device Data")

    dev_get(headers, net_id)


if __name__ == '__main__':
    main()
