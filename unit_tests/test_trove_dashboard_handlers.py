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

import unittest
from unittest import mock

import reactive.trove_dashboard_handlers as handlers

import charms_openstack.test_utils as test_utils


class TestRegisteredHooks(test_utils.TestRegisteredHooks):

    def test_hooks(self):
        defaults = [
            'charm.installed',
            'config.changed',
            'update-status',
            'upgrade-charm',
        ]
        hook_set = {
            'when': {
                'dashboard_available': (
                    'dashboard.available',),
            },
        }
        # test that the hooks were registered via the
        # reactive.barbican_handlers
        self.registered_hooks_test_helper(handlers, hook_set, defaults)


class TestTroveDashboardHandlers(unittest.TestCase):

    def setUp(self):
        super().setUp()

        self._reactive = self._patch(handlers, 'reactive')
        self._dashboard_charm = mock.Mock()

        provide_charm_inst = self._patch(handlers.charm,
                                         'provide_charm_instance')
        provide_charm_inst().__enter__.return_value = self._dashboard_charm
        provide_charm_inst().__exit__.return_value = None

    def _patch(self, thing, member):
        patcher = mock.patch.object(thing, member)
        mocked = patcher.start()
        self.addCleanup(patcher.stop)

        return mocked

    def test_dashboard_available(self):
        handlers.dashboard_available()

        self._reactive.endpoint_from_flag.assert_called_once_with(
            'dashboard.available')
        dashboard = self._reactive.endpoint_from_flag.return_value
        dashboard.publish_plugin_info.assert_called_once_with(
            "",
            None,
            conflicting_packages=[],
            install_packages=self._dashboard_charm.packages,
        )
        self._dashboard_charm.assess_status.assert_called_once_with()
