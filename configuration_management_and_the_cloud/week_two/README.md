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

Checkout [tools.pp](./tools.pp) file as an example.

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

The Puppet manifests that we use to manage computers in our fleet usually include a bunch of different resources that
are related to each other.

You're not going to configure a package that's not installed and you don't want to start a service until both the
package and the configuration are in place

Puppets lets us control this with resource relationships

Checkout [ntp.pp](./ntp.pp) file as an example.

This time, on top of declaring the resources that we need to manage, we're also declaring a few relationships between
them. We see that the configuration file requires the NTP package and the service requires the configuration file.

That way, if we make additional changes to the contents of the configuration file in the future, the service will get
reloaded with the new settings

You might notice that the resource types are written in lowercase, but relationships like require or notify use
uppercase for the first letter of the resource. ___This is part of Puppet syntax.___

We write resource types in lowercase when declaring them, but capitalize them when referring to them from another
resource's attributes

At the bottom of the file, we have a call to include NTP. That's why we told Puppet that we want to apply the rules
described in a class.

---

### Organizing Your Puppet Modules

In any configuration management deployment, there's usually a lot of different things to manage.

We might want to install some packages, copy some configuration files, start some services, schedule some periodic
tasks, make sure some users and groups are created and have access to specific devices, and maybe execute a few
commands that aren't provided by existing resources

On top of that, there might be different configurations applied to the different computers in the fleet

>  For example, workstations and laptops might include resources that aren't used on servers. Each distinct type of
> server will need its own specific setup.

___There's a lot of different things to manage___

We need to organize all these resources and information in a way that helps us maintain them long-term

This means grouping related resources, giving the groups good names, and making sure that the organization will make
sense to new users.

In puppet, manifests are organized into **modules**. A module is a collection of manifests and associated data.

We can put any resource we want into a module, but to keep our configuration management organized, we'll group things
together under a sensible topic.

> For example, we could have a module for everything related to monitoring the computer's health, another one for
> setting up the network stack, and yet another one for configuring a web serving application

* Manifest directory which stores all manifests

* Files directory includes files that are copied into the client machines without any changes

* Templates directory includes files that are preprocessed before they've been copied into the client machines
    * These templates can include values that get replaced after calculating the manifests, or sections that are only
     present if certain conditions are valid
     
There's a bunch more directories that can be part of a module depending on what exactly the module does

For a simple start:

> You can start with the simple module that just has one manifest in the Manifest directory. This file should be
> called **init.pp** and it should define a class with the same name as the module that you're creating. Then any
> files that your rules use need to be stored in the files or templates directories depending on whether you copy them
> directly or need to preprocess them.

Modules like these can look pretty much the same no matter who's using them. That's why over time, system
administrators using puppet have shared the modules they've written, letting others use the same rules.


### Extra Resources About Deploying Puppet Locally

* [Puppet Style Guide](https://puppet.com/docs/puppet/latest/style_guide.html)

* [Install from Packages - Puppet-Server](https://puppet.com/docs/puppetserver/latest/install_from_packages.html)

---

## Deploying Puppet to Clients


### Puppet Nodes

When managing fleets of computers, we usually want some rules to apply to every computer, and other rules to apply
only to a subset of systems

> Let's say you're managing all your servers with Puppet. You might want to install a basic set of tools on all of
> them, but only install the packages for serving web pages in your web servers. And only install the packages for
> sending and receiving email in your mail servers

There's a bunch of different ways that we can do this:

* We could conditionally apply some rules using facts from the machines

* Another way to apply different rules to different systems is to use separate node definitions

In Puppet terminology, a **node** is any system where a Puppet agent can run. To apply different rules to different
systems is to use separate node definitions.

That could be:

* Physical Workstation

* Server

* Virtual Machine

* Network Router

...as long as it has a Puppet agent and can apply the given rules.

So we can set up Puppet to give some basic rules to all the nodes, but then apply some specific rules to the nodes
that we want to be different.

When setting up Puppet, we usually have a default node definition that lists the classes that should be included for
all the nodes.

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

When defining a node, you can include a class by just using its name if there's no additional settings, or include
the class and set additional parameters if necessary

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

We can see here that specific nodes in the fleet are identified by their **FQDN**s, or **fully qualified domain names**.

In this case, we have the node definition for a host called `webserver.example.com`

For this node, we're including the same sudo and ntp classes as before, and we're adding the apache class on top. We
're listing the same classes because the classes included in the default node definition are only applied to the
nodes that don't have an explicit entry

In other words, when a node requests which rules it should apply, Puppet will look at the node definitions, figure
out which one matches the node's FQDN, and then give only those rules

To avoid repeating the inclusion of all the common classes, we might define a base class that does the work of
including all the classes that are common to all node types

The node definitions are typically stored in a file called **site.pp**, which isn't part of any module

Instead, it just defines what classes will be included for what nodes

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
