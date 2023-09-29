# Juju Trove Dashboard Charm


## Usage

Charm to deploy the Trove Dashboard Horizon plugin in a Canonical OpenStack deployment. This charm does not deploy Trove itself. For information about the Trove charm, see [here](https://github.com/cloudbase/trove-charm).


## Charm building

In order to build the Trove Dashboard charm, execute the following commands:

```bash
export CHARM_BASE="$HOME/work/charms"
export JUJU_REPOSITORY="$CHARM_BASE/builds"

mkdir -p $JUJU_REPOSITORY

# Install requirement for charm building.
sudo snap install --classic charm

# Clone the repository.
git clone https://github.com/cloudbase/trove-dashboard-charm
cd trove-dashboard-charm

# Build the charm.
charm build src
```

The charm should have been built in ``$JUJU_REPOSITORY/builds/trove-dashboard``.


## Deploy the charm

```bash
# The charm is a subordinate charm, and it requires a relation with a Horizon charm.
juju deploy $JUJU_REPOSITORY/builds/trove-dashboard trove-dashboard

# Add the necessary relations.
juju relate openstack-dashboard trove-dashboard
```

To replace the current Trove Dashboard charm with a newer revision and keeping the existing relations and configuration, run the following command:

```bash
juju refresh --path $JUJU_REPOSITORY/builds/trove-dashboard trove-dashboard
```
