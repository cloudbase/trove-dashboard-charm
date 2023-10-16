# Juju Trove Dashboard Charm


## Usage

Charm to deploy the Trove Dashboard Horizon plugin in a Canonical OpenStack deployment. This charm does not deploy Trove itself. For information about the Trove charm, see [here](https://github.com/cloudbase/trove-charm).


## Charm building

In order to build the Trove Dashboard charm, execute the following commands:

```bash
# Install requirement for charm building.
sudo snap install charmcraft --classic

# Clone the repository.
git clone https://github.com/cloudbase/trove-dashboard-charm
cd trove-dashboard-charm

# Build the charm.
tox -e build

# Alternatively, you can install the charm snap and build the charm:
sudo snap install charm --classic
tox -e build-reactive
```

The charm should have been built in ``./trove-dashboard_ubuntu-22.04-amd64.charm``, or
in ``./build/trove-dashboard`` if the charm was built with the ``charm`` building tools
instead of ``charmcraft``. This charm path will be used to deploy or refresh the
Trove dashboard charm.


## Deploy the charm

```bash
# The charm is a subordinate charm, and it requires a relation with a Horizon charm.
juju deploy ./trove-dashboard_ubuntu-22.04-amd64.charm trove-dashboard

# Add the necessary relations.
juju relate openstack-dashboard trove-dashboard
```

To replace the current Trove Dashboard charm with a newer revision and keeping the existing relations and configuration, run the following command:

```bash
juju refresh --path ./trove-dashboard_ubuntu-22.04-amd64.charm trove-dashboard
```
