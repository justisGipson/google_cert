# Configuration Management and the Cloud - Week 2


## Learning Objectives


Dive deeper into basic configuration management concepts and Puppet by:

* Learn how to install Puppet on your computer and how to use a simple test setup to check your rules work as expected

* Learn how to configure the typical client-server set-up with Puppet clients connecting and authenticating to the
Puppet server to get the rules that they should apply

* Learn how to use testing techniques and releasing best practices to safely deploy changes to clients of our
configuration management system

* Learn more ways of using the basic resources and Puppet's DSL

* Learn how you can apply different sets of rules to different nodes in your fleet

* Learn how you can organize your rules so that they're easier to maintain

---

## Deploying Puppet Locally


### Applying Rules Locally

Puppet is usually deployed in a client-server architecture

We can also use it as a stand-alone application run from the command line

This is common when testing new configurations. It can be the preferred configuration for complex setups where
connecting to a master is no longer the best approach.

When using a stand-alone Puppet, the same computer processes the facts, calculates the rules that need to be applied
, and makes any necessary changes locally

Puppet is available on a number of different platforms. We can either install it from the package management system
available in the OS or download it from the official website

The **-v** flag tells Puppet that we want to get verbose output which will tell us what's going on while Puppet is
applying the rules in the file that we pass to it.

The **manifest** is a file with .pp extension where we'll store the rules that we want to apply.

Checkout tools.pp file as an example.

The **catalog** is the list of rules that are generated for one specific computer once the server has evaluated all
variables, conditionals, and functions.

> For example, if a packet should only be installed when a certain condition is met, this condition is evaluated on
> the server side based on the gathered facts. The catalog is the list of rules that are generated for one specific
> computer once the server has evaluated all variables, conditionals, and functions.

In this example, the catalog will be exactly the same as our code because the code didn't include any variables
, functions, or conditionals.

More complex sets of rules can lead to different catalogs depending on fact values

---

### Managing Resource Relationships

Checkout ntp.pp file as an example.


---

### Organizing Your Puppet Modules

In puppet, manifests are organized into **modules**. A module is a collection of manifests and associated data.

* Manifest directory which stores manifest and init.pp where it defines a class with the same name as the created  module

* Templates directory which stores any files that stores rules to be used

---

## Deploying Puppet to Clients


### Puppet Nodes

In Puppet terminology, a **node** is any system where a Puppet agent can run. To apply different rules to different
systems is to use separate node definitions.

Below example is the default node with two classes, the sudo class and the ntp class.

```puppet

node default {
    class { 'sudo': }
    # sets an additional servers parameter which can be used to get the network time
    class { 'ntp':
            servers => [ 'ntp1.example.com', 'ntp2.example.com' ]
    }
}

```

Below example shows how to apply some settings to only some specific nodes by adding more node definitions.

```puppet

node default {
    class { 'sudo': }
    # sets an additional servers parameter which can be used to get the network time
    class { 'ntp':
            servers => [ 'ntp1.example.com', 'ntp2.example.com' ]
    }
    class { 'apache': }
}

```

Below example shows how specific nodes in the fleet are identified by their FQDNs, or fully qualified domain names.

```puppet

node webserver.example.com {
    class { 'sudo': }
    # sets an additional servers parameter which can be used to get the network time
    class { 'ntp':
            servers => [ 'ntp1.example.com', 'ntp2.example.com' ]
    }
    class { 'apache': }
}

```

---

### Puppet's Certificate Infrastructure

Puppet uses __public key infrastructure (PKI)__, __secure sockets layer (SSL)__, to establish secure connections
between the server and the clients.

__Puppet comes with its own certificate authority__, which can be used to create certificates for each clients.

Why do we care so much about the identity of the nodes? There's a bunch of reasons.

One of the reason why identity of the nodes matter is that the Puppet rules can sometimes include confidential
information.

* Automatic sign all requests feature is available in Puppet, it should be limited to test deployment and never used
for real computers being used by real users

---

## Updating Deployments


### Modifying and Testing Manifests

There are few ways of test changes made on Puppet

1. puppet parser validate command with noop parameter
   
   * Checks that the syntax of the manifests is correct
   
   * noop parameter which comes from no operations makes puppet simulate what it would do without actually doing it

2. Separate test machines that are used only for testing out changes

3. Automated testing via **R-Spec**

Below example sets the facts involved different values and checks that the catalog ends up stating the expected 

```puppet

describe 'gksu', :type => :class do
    let (:facts) { { 'is_virtual' => 'false' } }
    it { should contain_package('gksu').with_ensure('latest') }
end

```
---

### Safely Rolling out Changes and Validating Them

Even if you've tested the change on your computer or on a test computer and it worked just fine, __it doesn't mean
that the change will work correctly on all machines running in production__.

In an infrastructure context, **production** is the parts of the infrastructure where a service is executed and
served to its users.

In order to roll out changes safely,

1. Always run them through a test environment first

2. Push changes in in batches

3. Make the change to be small and self-contained

---
