# Copyright 2017 Cloudbase Solutions Srl
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""This module contains fake HVN API response."""

import json
import pkg_resources


class FakeResponse(object):

    """HNV API fake responses."""

    def __init__(self):
        self._resources = "hnv_client.tests.fake.response"
        self._cache = {}

    def _load_resource(self, resource):
        """Load the json response for the required resource."""
        if resource not in self._cache:
            json_response = pkg_resources.resource_stream(
                self._resources, resource)
            self._cache[resource] = json.load(json_response)
        return self._cache[resource]

    def logical_networks(self):
        """Fake GET(all) response for logical networks."""
        return self._load_resource("logical_networks.json")

    def logical_subnets(self):
        """Fake GET(all) response for logical subnets."""
        return self._load_resource("logical_subnets.json")

    def ip_pools(self):
        """Fake GET(all) response for IP pools."""
        return self._load_resource("ip_pools.json")

    def network_interfaces(self):
        """Fake GET(all) response for network interfaces."""
        return self._load_resource("network_interfaces.json")

    def ip_configurations(self):
        """Fake GET(all) response for ip configurations."""
        return self._load_resource("ip_configurations.json")

    def virtual_networks(self):
        """Fake GET(all) response for virtual networks."""
        return self._load_resource("virtual_networks.json")

    def virtual_subnetworks(self):
        """Fake GET(all) response for virtual subnetworks."""
        return self._load_resource("virtual_subnetworks.json")

    def acl_rules(self):
        """Fake GET(all) response for ACL rules."""
        return self._load_resource("acl_rules.json")

    def acl(self):
        """Fake GET(all) response for ACL."""
        return self._load_resource("acl.json")

    def virtual_switch_manager(self):
        """Fake GET response for virtual switch manager."""
        return self._load_resource("virtual_switch_manager.json")

    def routes(self):
        """Fake GET(all) response for routes."""
        return self._load_resource("routes.json")

    def route_tables(self):
        """Fake GET(all) response for route tables."""
        return self._load_resource("route_tables.json")
