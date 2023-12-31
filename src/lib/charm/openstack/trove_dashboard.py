# Copyright 2023 Cloudbase Solutions
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import charms_openstack.adapters
import charms_openstack.charm


class TroveDashboardCharm(charms_openstack.charm.OpenStackCharm):
    # Internal name of charm
    name = 'trove-dashboard'

    # First release supported
    release = 'yoga'

    # List of packages to install for this charm
    packages = ['python3-trove-dashboard']

    required_relations = ['dashboard']

    # The base class was not updated to support only Python3. If we don't
    # specify this, python-memcache would be installed instead of
    # python3-memcache, which would result in an error in the install phase.
    python_version = 3

    adapters_class = charms_openstack.adapters.OpenStackRelationAdapters
