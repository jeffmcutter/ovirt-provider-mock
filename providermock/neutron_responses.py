# Copyright 2016 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Refer to the README and COPYING files for full details of the license
from __future__ import absolute_import

import json
import time

#from neutron_data import networks
#from neutron_data import ports
#from neutron_data import subnets
from vnc_creds import vnc_creds
from vnc_api import vnc_api

GET = 'GET'  # list of entities
SHOW = 'SHOW'  # concrete entity
DELETE = 'DELETE'
POST = 'POST'
PUT = 'PUT'

NETWORKS = 'networks'
PORTS = 'ports'
SUBNETS = 'subnets'


_responses = {}


def vnc():
    vnclib = vnc_api.VncApi(
        api_server_host = vnc_creds['api_server_host'],
        auth_host = vnc_creds['auth_host'],
        username = vnc_creds['username'],
        password = vnc_creds['password'],
        tenant_name = vnc_creds['tenant_name'])
    return vnclib

def rest(method, path):
    """
    Decorator for adding rest request handling methods.
    method -- rest method of the arriving request: GET/POST/DELETE/PUT
    path -- the path of the arriving request
    For example the function handling the following request:
    GET: http://<host>/../networks
    would have to be decorated with:
    rest('GET', 'networks')
    """
    def assign_response(funct):
        if method not in _responses:
            _responses[method] = {}
        _responses[method][path] = funct
        return funct
    return assign_response


def generate_id():
    return str(int(time.time()))


@rest(SHOW, NETWORKS)
def show_network(content, id=None):
    network = vnc().virtual_network_read(id = id)
    return json.dumps({'network': {'id': network.uuid, 'name': network.name}})


@rest(SHOW, PORTS)
def show_port(content, id=None):
    port = vnc().virtual_machine_interface_read(id = id)
    return json.dumps({'port': {'id': port.uuid, 'name': port.name}})


@rest(SHOW, SUBNETS)
def show_subnet(content, id):
    subnet = vnc().subnet_read(id = id)
    return json.dumps({'subnet': {'id': subnet.uuid, 'name': subnet.name}})


@rest(GET, '')
def get_default(content, id):
    return json.dumps({})


'''
-------------
NETWORKS LIST
-------------

Query from ovirt engine:
GET: http://<host>:<port – default:9696>/v2.0/networks
Headers: 
 	Accept=application/json 
 	X-Auth-Token=<token from authentication request>

Minimal response from provider:
Response code: 200
Required headers: "Content-Type", "Application/json"
Body (with sample values):
    "networks": [
        {
            "status": "ACTIVE", 
            "subnets": ["dc594048-a9e2-4ec9-9928-4157cea7e530"], 
            "name": "public", 
            "provider:physical_network": null, 
            "admin_state_up": true, 
            "tenant_id": "547deac3d7f64e2688de188365a139aa", 
            "mtu": 0, 
            "router:external": true, 
            "shared": false, 
            "provider:network_type": "vxlan", 
            "id": "bf864bf3-81d8-438d-bf68-4b0c357309b3", 
            "provider:segmentation_id": 35
        },
 	{ … }
}
'''

@rest(GET, NETWORKS)
def get_networks(content, id):
    response_networks = []
    for network in vnc().virtual_networks_list()['virtual-networks']:
        response_networks.append({'id': network['uuid'], 'name': network['fq_name'][2]})
    return json.dumps({"networks": response_networks})


'''
----------
PORTS LIST
----------

Query from ovirt engine:
GET: http://<host>:<port – default:9696>/v2.0/ports
Headers: 
 	Accept=application/json 
 	X-Auth-Token=<token from authentication request>

Minimal response from provider:
Response code: 200
Required headers: "Content-Type", "Application/json"
Body (with sample values):
    {"ports":
 [
   {
    "status": "DOWN",
    "binding:host_id": "192.168.120.18-1ebb72",
    "allowed_address_pairs": [],
    "extra_dhcp_opts": [],
    "dns_assignment": [
       {
        "hostname": "host-172-24-4-227",
        "ip_address": "172.24.4.227",
        "fqdn": "host-172-24-4-227.openstacklocal."
       }
       ],
    "device_owner": "oVirt",
    "binding:profile": {},
    "fixed_ips": [
       {
        "subnet_id": "dc594048-a9e2-4ec9-9928-4157cea7e530",
        "ip_address": "172.24.4.227"
       }],
    "id": "49ccb785-eadb-469d-8c33-e7bc87d37e4e",
    "security_groups": ["9cca3bc4-416c-4815-b3d7-4ee81ab8bb97"],
    "device_id": "5cc10431-0b25-41bd-941c-3a1aed8edd87",
    "name": "nic5",
    "admin_state_up": true,
    "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
    "dns_name": "",
    "binding:vif_details": {},
    "binding:vnic_type": "normal",
    "binding:vif_type": "binding_failed",
    "tenant_id": "547deac3d7f64e2688de188365a139aa",
    "mac_address": "00:1a:4a:16:01:59"
  }]
}
'''

@rest(GET, PORTS)
def get_ports(content, id):
    response_ports = []
    for port in vnc().virtual_machine_interfaces_list()['virtual-machine-interfaces']:
        response_ports.append({'id': port['uuid'], 'name': port['fq_name'][2]})
    return json.dumps({"ports": response_ports})


'''
------------
SUBNETS LIST
------------

Query from ovirt engine:
GET: http://<host>:<port – default:9696>/v2.0/subnets
Headers: 
 	Accept=application/json 
 	X-Auth-Token=<token from authentication request>

Minimal response from provider:
Response code: 200
Required headers: "Content-Type", "Application/json"
Body (with sample values):
{"subnets":
[
    {
        "name": "private_subnet",
        "enable_dhcp": true,
        "network_id": "59b48a4c-893c-47d2-9df3-84102329bbb9",
        "tenant_id": "472beee27f704a5b8a6f3a15fdac7ba5",
        "dns_nameservers": [],
        "gateway_ip": "10.0.0.1",
        "ipv6_ra_mode": null,
        "allocation_pools":
        [
            {
                "start": "10.0.0.2",
                "end": "10.0.0.254"
            }
        ],
        "host_routes": [],
        "ip_version": 4,
        "ipv6_address_mode": null,
        "cidr": "10.0.0.0/24",
        "id": "6ed90628-5d9c-4eae-8665-0b2420e683d4",
        "subnetpool_id": null
    },
    {
        "name": "public_subnet",
        "enable_dhcp": false,
        "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
        "tenant_id": "547deac3d7f64e2688de188365a139aa",
        "dns_nameservers": [],
        "gateway_ip": "172.24.4.225",
        "ipv6_ra_mode": null,
        "allocation_pools":
        [
            {
                "start": "172.24.4.226",
                "end": "172.24.4.238"
            }
        ],
        "host_routes": [],
        "ip_version": 4,
        "ipv6_address_mode": null,
        "cidr": "172.24.4.224/28",
        "id": "dc594048-a9e2-4ec9-9928-4157cea7e530",
        "subnetpool_id": null
    }
]}
'''

@rest(GET, SUBNETS)
def get_subnets(content, id):
    response_subnets = []
    for subnet in vnc().subnets_list()['subnets']:
        response_subnets.append({'id': subnet['uuid'], 'name': subnet['fq_name'][0]})
    return json.dumps({"subnets": response_subnets})


'''
------
DELETE
------

Query from ovirt engine:
POST: http://<host>:<port – default:9696>/v2.0/[ports|subnets|networks]/<id of entity to delete>
Headers: 
 	Accept=application/json 
 	X-Auth-Token=<token from authentication request>
Body (with sample values):

Minimal response from provider:
Response code: 204
Required headers: "Content-Type", "Application/json"
'''

@rest(DELETE, NETWORKS)
def delete_network(content=None, id=None):
    if id is not None:
        vnc().virtual_network_delete(id = id)


@rest(DELETE, PORTS)
def delete_port(content=None, id=None):
    if id is not None:
        vnc().virtual_machine_interface_delete(id = id)

@rest(DELETE, SUBNETS)
def delete_subnet(content, id):
    if id is not None:
        vnc().subnet_delete(id = id)


'''
--------------
CREATE NETWORK
--------------

No specifics given in presentation.

Collected by creating a network against the mock provider using RHV-M:

DEBUG:Request: POST : /v2.0/networks
DEBUG:Request body:
{
  "network" : {
    "name" : "test_create_net_1",
    "admin_state_up" : true,
    "tenant_id" : "oVirt"
  }
}
UPDATE NETWORK:{'tenant_id': u'oVirt', 'admin_state_up': True, 'id': 'network_id_1551728885', 'name': u'test_create_net_1'}
192.168.122.23 - - [04/Mar/2019 14:48:05] "POST /v2.0/networks HTTP/1.1" 200 -
DEBUG:Response code: 200
DEBUG:Response body: {"network": {"tenant_id": "oVirt", "admin_state_up": true, "id": "network_id_1551728885", "name": "test_create_net_1"}}

'''

@rest(POST, NETWORKS)
def post_networks(content, id):
    content_json = json.loads(content)

    received_network = content_json['network']
    network = dict()

#    #  The port id 'id' will be passed to the VIF driver as "vnic_id"
#    if getattr(received_network, 'id', None):  # existing port is updated
#        network_id = received_network['id']
#    else:  # if port has no id, create a new one
#        network_id = 'network_id_' + generate_id()
#
#    # only copy the relevant keys, fail if any of them is missing
#    network['id'] = network_id
    network['name'] = received_network['name']
#
#    if 'admin_state_up' in received_network:
#        network['admin_state_up'] = received_network['admin_state_up']
#
#    if 'tenant_id' in received_network:
#        network['tenant_id'] = received_network['tenant_id']
#    if 'provider:physical_network' in received_network:
#        network['provider:physical_network'] = received_network['provider:physical_network']
#    # 'vlan' if a vlan network
#    if 'provider:network_type' in received_network:
#        network['provider:network_type'] = received_network['provider:network_type']
#    # vlan segment
#    if 'provider:segmentation_id' in received_network:
#        network['provider:segmentation_id'] = received_network['provider:segmentation_id']

    print "UPDATE NETWORK:" + str(network)
    obj = vnc_api.VirtualNetwork(network['name'])
    network['id'] = vnc().virtual_network_create(obj)
    return json.dumps({'network': network})


'''
-----------
CREATE PORT
-----------

Query from ovirt engine:
POST: http://<host>:<port – default:9696>/v2.0/ports
Headers: 
 	Accept=application/json 
 	X-Auth-Token=<token from authentication request>
Body (with sample values):
{
  "port" : {
    "name" : "nic2",
    "binding:host_id" : "192.168.120.18-1ebb72",
    "admin_state_up" : true,
    "device_id" : "7b2fa61c-2a88-424a-93b5-adc63328efe4",
    "device_owner" : "oVirt",
    "mac_address" : "00:1a:4a:16:01:53",
    "network_id" : "bf864bf3-81d8-438d-bf68-4b0c357309b3",
    "tenant_id" : "547deac3d7f64e2688de188365a139aa"
  }
}



Minimal response from provider:
Response code: 200
Required headers: "Content-Type", "Application/json"
Body (with sample values):
{
    "port":
    {
        "status": "DOWN",
        "binding:host_id": "192.168.120.18-1ebb72",
        "allowed_address_pairs": [],
        "extra_dhcp_opts": [],
        "device_owner": "oVirt",
        "binding:profile": {},
        "fixed_ips": [{
            "subnet_id": "dc594048-a9e2-4ec9-9928-4157cea7e530",
            "ip_address": "172.24.4.232"
        }],
        "id": "3c10bb5a-3d73-43a2-9c5a-9349d449e2a6",
        "security_groups": ["9cca3bc4-416c-4815-b3d7-4ee81ab8bb97"],
        "device_id": "7b2fa61c-2a88-424a-93b5-adc63328efe4",
        "name": "nic2",
        "admin_state_up": true,
        "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
        "dns_name": "",
        "binding:vif_details": {},
        "binding:vnic_type": "normal",
        "binding:vif_type": "binding_failed",
        "tenant_id": "547deac3d7f64e2688de188365a139aa",
        "mac_address": "00:1a:4a:16:01:53"
    }
}

Collected by creating a port against the mock provider using RHV-M:

DEBUG:Request: GET : /v2.0/ports
127.0.0.1 - - [04/Mar/2019 18:20:30] "GET /v2.0/ports HTTP/1.1" 200 -
DEBUG:Response code: 200
DEBUG:Response body: {"ports": [{"device_owner": "oVirt", "binding:host_id": "binding_host_id", "name": "dummy port", "mac_address": "00:00:00:00:00:00", "network_id": "network_id_1", "admin_state_up": true, "id": "port_id_1", "device_id": "dummy port"}, {"binding:host_id": "rhvh1.example.com", "name": "nic1", "admin_state_up": true, "network_id": "network_id_2", "device_owner": "oVirt", "mac_address": "00:1a:4a:16:01:51", "id": "port_id_1551739049", "device_id": "202a6d03-0926-491e-82f7-d6834e3a6bdf"}]}
DEBUG:Request: PUT : /v2.0/ports/port_id_1551739049
DEBUG:Request body:
{
  "port" : {
    "security_groups" : null
  }
}
PUT PORT:{'binding:host_id': u'rhvh1.example.com', 'name': u'nic1', 'admin_state_up': True, 'network_id': u'network_id_2', 'device_owner': u'oVirt', 'mac_address': u'00:1a:4a:16:01:51', 'id': 'port_id_1551739049', 'device_id': u'202a6d03-0926-491e-82f7-d6834e3a6bdf'}
127.0.0.1 - - [04/Mar/2019 18:20:30] "PUT /v2.0/ports/port_id_1551739049 HTTP/1.1" 200 -
DEBUG:Response code: 200
DEBUG:Response body: {"port": {"binding:host_id": "rhvh1.example.com", "name": "nic1", "admin_state_up": true, "network_id": "network_id_2", "device_owner": "oVirt", "mac_address": "00:1a:4a:16:01:51", "id": "port_id_1551739049", "device_id": "202a6d03-0926-491e-82f7-d6834e3a6bdf"}}
DEBUG:Request: GET : /v2.0/ports
127.0.0.1 - - [04/Mar/2019 18:20:34] "GET /v2.0/ports HTTP/1.1" 200 -
DEBUG:Response code: 200
DEBUG:Response body: {"ports": [{"device_owner": "oVirt", "binding:host_id": "binding_host_id", "name": "dummy port", "mac_address": "00:00:00:00:00:00", "network_id": "network_id_1", "admin_state_up": true, "id": "port_id_1", "device_id": "dummy port"}, {"binding:host_id": "rhvh1.example.com", "name": "nic1", "admin_state_up": true, "network_id": "network_id_2", "device_owner": "oVirt", "mac_address": "00:1a:4a:16:01:51", "id": "port_id_1551739049", "device_id": "202a6d03-0926-491e-82f7-d6834e3a6bdf"}]}
DEBUG:Request: PUT : /v2.0/ports/port_id_1551739049
DEBUG:Request body:
{
  "port" : {
    "binding:host_id" : "rhvh2.example.com",
    "mac_address" : "00:1a:4a:16:01:51",
    "security_groups" : null
  }
}
PUT PORT:{'binding:host_id': u'rhvh1.example.com', 'name': u'nic1', 'admin_state_up': True, 'network_id': u'network_id_2', 'device_owner': u'oVirt', 'mac_address': u'00:1a:4a:16:01:51', 'id': 'port_id_1551739049', 'device_id': u'202a6d03-0926-491e-82f7-d6834e3a6bdf'}
127.0.0.1 - - [04/Mar/2019 18:20:34] "PUT /v2.0/ports/port_id_1551739049 HTTP/1.1" 200 -
DEBUG:Response code: 200
DEBUG:Response body: {"port": {"binding:host_id": "rhvh1.example.com", "name": "nic1", "admin_state_up": true, "network_id": "network_id_2", "device_owner": "oVirt", "mac_address": "00:1a:4a:16:01:51", "id": "port_id_1551739049", "device_id": "202a6d03-0926-491e-82f7-d6834e3a6bdf"}}

'''

@rest(POST, PORTS)
def post_ports(content, id):
    content_json = json.loads(content)
    received_port = content_json['port']
    port = dict()

#    #  The port id 'id' will be passed to the VIF driver as "vnic_id"
#    if getattr(received_port, 'id', None):  # existing port is updated
#        port_id = received_port['id']
#    else:  # if port has no id, create a new one
#        port_id = 'port_id_' + generate_id()
#
#    # only copy the relevant keys, fail if any of them is missing
#    port['id'] = port_id
    port['name'] = received_port['name']  # vm nic name (eg. ens3)
#    port['network_id'] = received_port['network_id']  # external network id
#    port['device_id'] = received_port['device_id']  # vm nic id
#    port['mac_address'] = received_port['mac_address']  # vm nic mac
#    port['device_owner'] = received_port['device_owner']  # always 'oVirt'
#    port['admin_state_up'] = received_port['admin_state_up']
#    port['binding:host_id'] = received_port['binding:host_id']

    print "UPDATE PORT:" + str(port)
    obj = vnc_api.VirtualMachineInterface(port['name'])
    port['id'] = vnc().virtual_machine_interface_create(obj)
    return json.dumps({'port': port})


'''
-------------
CREATE SUBNET
-------------

Query from ovirt engine:
POST: http://<host>:<port – default:9696>/v2.0/subnets
Headers: 
 	Accept=application/json 
 	X-Auth-Token=<token from authentication request>
Body (with sample values):
{
  "subnet" : {
    "name" : "public2",
    "cidr" : "7.7.7.0/24",
    "enable_dhcp" : true,
    "network_id" : "bf864bf3-81d8-438d-bf68-4b0c357309b3",
    "tenant_id" : "547deac3d7f64e2688de188365a139aa",
    "dns_nameservers" : [ ],
    "ip_version" : 4
  }
}


Minimal response from provider:
Response code: 200
Required headers: "Content-Type", "Application/json"
Body (with sample values):
{
    "subnet":
    {
        "name": "public2",
        "enable_dhcp": true,
        "network_id": "bf864bf3-81d8-438d-bf68-4b0c357309b3",
        "tenant_id": "547deac3d7f64e2688de188365a139aa",
        "dns_nameservers": [],
        "gateway_ip": "7.7.7.1",
        "ipv6_ra_mode": null,
        "allocation_pools": [{"start": "7.7.7.2", "end": "7.7.7.254"}],
        "host_routes": [],
        "ip_version": 4,
        "ipv6_address_mode": null,
        "cidr": "7.7.7.0/24",
        "id": "6ea2550b-960a-4988-97aa-892e8bbca52b",
        "subnetpool_id": null
    }
}

Collected by creating a network against the mock provider using RHV-M:

DEBUG:Request: SHOW : /v2.0/networks/network_id_1551728885
192.168.122.23 - - [04/Mar/2019 14:51:51] "GET /v2.0/networks/network_id_1551728885 HTTP/1.1" 200 -
DEBUG:Response code: 200
DEBUG:Response body: {"network": {"tenant_id": "oVirt", "admin_state_up": true, "id": "network_id_1551728885", "name": "test_create_net_1"}}
DEBUG:Request: POST : /v2.0/subnets
DEBUG:Request body:
{
  "subnet" : {
    "name" : "test_create_subnet_1",
    "cidr" : "192.168.0.0/24",
    "enable_dhcp" : true,
    "network_id" : "network_id_1551728885",
    "tenant_id" : "oVirt",
    "dns_nameservers" : [ "192.168.0.1" ],
    "ip_version" : 4,
    "gateway_ip" : "192.168.0.1"
  }
}
UPDATE SUBNET:{'network_id': u'network_id_1551728885', 'cidr': u'192.168.0.0/24', 'id': 'subnet_id_1551729111', 'name': u'test_create_subnet_1'}
192.168.122.23 - - [04/Mar/2019 14:51:51] "POST /v2.0/subnets HTTP/1.1" 200 -
DEBUG:Response code: 200
DEBUG:Response body: {"subnet": {"network_id": "network_id_1551728885", "cidr": "192.168.0.0/24", "id": "subnet_id_1551729111", "name": "test_create_subnet_1"}}

'''

@rest(POST, SUBNETS)
def post_subnets(content, id):
    content_json = json.loads(content)
    received_subnet = content_json['subnet']
    subnet = dict()

#    # generate some new id for the subnet
#    subnet_id = 'subnet_id_' + generate_id()
#
#    # only copy the relevant keys, fail if any of them is missing
#    subnet['id'] = subnet_id
    subnet['name'] = received_subnet['name']
#    subnet['network_id'] = received_subnet['network_id']
#    subnet['cidr'] = received_subnet['cidr']
#
#    #update_field_if_present(subnet, received_subnet, 'ip_version')
#    #update_field_if_present(subnet, received_subnet, 'gateway_ip')
#    #update_field_if_present(subnet, received_subnet, 'dns_nameservers')

    print "UPDATE SUBNET:" + str(subnet)
    obj = vnc_api.Subnet(subnet['name'])
    subnet['id'] = vnc().subnet_create(obj)
    return json.dumps({'subnet': subnet})


@rest(PUT, PORTS)
def put_ports(content, id):
    if not id:
        raise Exception('No port id in PUT request')

    content_json = json.loads(content)

    received_port = content_json['port']

    port_id = get_id_from_path(path)
    port = ports[port_id]

    # only copy the relevant keys, fail if any of them is missing
    #update_field_if_present(port, received_port, 'name')
    #update_field_if_present(port, received_port, 'network_id')
    #update_field_if_present(port, received_port, 'device_id')
    #update_field_if_present(port, received_port, 'mac_address')
    #update_field_if_present(port, received_port, 'device_owner')
    #update_field_if_present(port, received_port, 'admin_state_up')
    #update_field_if_present(port, received_port, 'binding:host_id')

    print "PUT PORT:" + str(port)
    # ports[port_id] = port
    return json.dumps({'port': port})


#@rest(GET, 'tech')
#def get_debug(content, id):
#    result = 'DEBUG DUMP\n\n\n'
#
#    result += 'NETWORKS:\n\n'
#    result += json.dumps(networks)
#
#    result += '\n\n'
#    result += 'SUBNETS:\n\n'
#    result += json.dumps(subnets)
#
#    result += '\n\n'
#    result += 'PORTS:\n\n'
#    result += json.dumps(ports)
#
#    return result


def responses():
    return _responses
