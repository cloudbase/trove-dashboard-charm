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

import charmhelpers.core.hookenv as hookenv
import charms_openstack.bus
import charms_openstack.charm as charm
import charms.reactive as reactive


charms_openstack.bus.discover()

charm.use_defaults(
    'charm.installed',
    'config.changed',
    'update-status',
    'upgrade-charm',
)


@reactive.when('dashboard.available')
def dashboard_available():
    """Relation to OpenStack Dashboard principal charm complete."""

    with charm.provide_charm_instance() as dashboard_charm:
        dashboard = reactive.endpoint_from_flag('dashboard.available')
        hookenv.log(f'DEBUG: dashboard_available "{dashboard.release}" '
                    f'"{dashboard.bin_path}" "{dashboard.openstack_dir}"')
        dashboard.publish_plugin_info(
            "",
            None,
            conflicting_packages=[],
            install_packages=dashboard_charm.packages,
        )
        dashboard_charm.assess_status()
