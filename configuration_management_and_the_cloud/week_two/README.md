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

Below example is the default node with two classes, the sudo class and the ntp class. For the ntp class, we're
setting an additional servers parameter that lists the servers we can use to get the network time.

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

All right, that's the default node, so it will apply to computers in the fleet by default. 

Below example shows how specific nodes in the fleet are identified by their FQDNs

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

This is another step towards helping us organize our code in a way that makes it easier to maintain

---

### Puppet's Certificate Infrastructure

In typical Puppet deployments, all managed machines and the fleet connect to a Puppet server

The client send their facts to the server, and the server then processes the manifests, generates the corresponding
catalog, and sends it back to the clients who apply it locally.

Puppet uses __public key infrastructure (PKI)__, and __secure sockets layer (SSL)__, to establish secure connections
between the server and the clients.

The clients use this infrastructure to check the server's identity, and the server uses it to check the client's
identity, and all communication is done over an encrypted channel that uses these identities so it can't be
intercepted by other parties

Each machine involved has a pair of keys related to each other, a private key and a public key. The private key is
secret, only known to that specific machine, the public key is shared with other machines involved. Machines can
then use the standardized process to validate the identity of any other machine. The sender signs a message using
the private key and the receiver validates the signature using the corresponding public key.

But how do machines know which public keys to trust? This is where a **certificate authority**, or **CA** comes in

The CA verifies the identity of the machine and then creates a certificate stating that the public key goes with that
machine. After that, other machines can rely on that certificate to know that they can trust the public key, since
it means the machine's identity has been verified.

__Puppet comes with its own certificate authority__, which can be used to create certificates for each clients.

So you can use that one, or if your company already has a CA that validates the identity of the machines in your
fleet, you can integrate it with Puppet, so you only validate the identities once

When a node checks into the Puppet master for the first time, it requests the certificate. The Puppet master looks at
this request and if it can verify the nodes identity, it creates a certificate for that node. The system
administrator can check the identity manually or use a process that does this automatically using additional
information about the machines to verify their identity. When the agent node picks up this certificate, it knows
it can trust the Puppet master, and the node can use the certificate from then on to identify itself when
requesting a catalog

Why do we care so much about the identity of the nodes? There's a bunch of reasons...

One of the reason why identity of the nodes matter is that the Puppet rules can sometimes include confidential
information

Even if none of the rules hold confidential info, you want to be sure that the machine you're setting up as your web
server really is your web server and not a rogue machine that just claims to have the same name

All sorts of things could go wrong if random computers start popping up in your network with the wrong settings

> If you're creating a test deployment to try out how Puppet rules get applied, and so you're only managing tests
> machines, you can configure Puppet to automatically sign all requests, but you should never do this for real
> computers being used by real users.

___Remember that it's better to be safe than sorry. So always take the time to authenticate your machines___

___AND___

___Automatic sign all requests feature is available in Puppet, it should be limited to test deployment and never used
for real computers being used by real users___

When starting out with Puppet, it's common to use the manual signing approach. In this case, when the node connects
to the master, it will generate a certificate request, which will go into a queue in the Puppet master machine. You
'll then need to verify that the machine's identity is correct and the baked-in CA will issue the corresponding
certificate

If your fleet is large, this manual approach won't really work. Instead, you'll want to write a script that verifies
the identity of the machines automatically for you

One way to do this is by copying a unique piece of information into the machines when they get provisioned and then
use this pre-shared data as part of the certificate request

That way, your script can verify that the machines are who they claim to be without involving any humans

---

### Setting Up Puppet Clients and Servers

We've already installed the Puppet master package on this computer, so we'll use it as the master

Since this is a test deployment to demonstrate Puppet, we'll configure it to automatically sign the certificate
requests of the nodes we add

Remember, if we were deploying this to real computers, we'd have to manually sign the requests or implement a proper
validating script

`sudo puppet config --section master set autosign true`

With that, we can connect to the client that we want to manage using Puppet. We'll connect using SSH to a machine
called web server. On this machine, we'll install the Puppet client which is shipped by the Puppet package.

`ssh webserver`

On this machine, we'll install the Puppet client which is shipped by the Puppet package.

`sudo apt install puppet`

We have the Puppet agent installed. Now we need to configure it to talk to the Puppet server that we're running on
the other machine. To do that, we'll use Puppet config like before but this time we'll tell it that we want to set
the server to **ubuntu.example.com**

`sudo puppet config set server ubuntu.example.com`

Now that we've configured the server, we can test the connection to the Puppet master by using the Puppet agent
command passing **-v** as before to get verbose output, and **--test** to do a test run

`sudo puppet agent -v --test`

As usual, Puppet tells us everything it did.

* It first created an SSL key for the machine. 

* It then read a bunch of information from the machine and used this to create a certificate request. 

* The agent shows us the fingerprint of the certificate requested. If we were using manual signing, we could use this
fingerprint to verify that the request and the server matches the one generated on the machine. 

* The certificate was then generated on our puppet master

* Once the certificate exchange completed, the agent retrieved all the information from the machine and sent it to the
master. 

* In exchange, it got back a catalog and applied it. The catalog applied almost immediately because we haven't
actually configured any rules to be applied to our clients.

We should go ahead and do that now. We'll go back to our Puppet master and create a couple of node definitions

node definitions are stored in a manifest file called site.pp, which is stored at the root of the nodes environment

So the file that we need to create will be located in **/etc/puppet/code/environments/production/manifests** and it
will be called **site.pp**.

* [**site.pp** Example](./site.pp)

We have our very basic node definition. We can now save this and run the Puppet agent on our web server machine again.

`sudo puppet agent -v --test`

This time, the Puppet agent connected to the Puppet master and got a catalog that told it to install and configure
the Apache package. This included setting up a bunch of different services

Up to now, we've been doing manual runs of the Puppet agent for testing purposes. Now that we know it's working fine
, we want to keep Puppet running automatically.

That way, if we make changes to the configuration, clients will automatically apply those changes without us having
to do any manual steps

So to do that, we'll use the **systemctl** command, which lets us control the services that are enabled when the
machine starts and those that are currently running

So we'll first tell the system CTL to enable the puppet service so that the agent gets started whenever the machine
reboots

`sudo systemctl enable puppet`

Then we'll tell system CTL to start the puppet service so that it starts running

`sudo systemctl start puppet`

Last step, we'll ask systems CTL for the status of the Puppet service to check that it's actually running

`sudo systemctl status puppet`

The Puppet agent will keep regularly checking in with the master and ask if there are any changes that need to be
applied to the machine.

We use the configuration we set in the Puppet master to manage the installation and configuration of software in our
web server, and we set up the Puppet agent in the web server to keep running so that the configuration stays up to
date

---

### Extra Resources for Deploying Puppet to Clients

* [Puppet SSL Explained](http://www.masterzen.fr/2010/11/14/puppet-ssl-explained/)

---

## Updating Deployments


### Modifying and Testing Manifests

When we change the manifest modifying a setting that's already managed by puppet. Puppet applies this change to the
nodes, the puppet agent does whatever is needed to bring the nodes to the new desired state, so you can make a small
change in your manifests and have that modify all the machines in your fleet - ___super powerful___

It's pretty common for IT specialist working on configuration management to test out new rules on their machines by
simply forcing the machine to apply the manifest they want to test.

We've done this in some of our examples where we applied the rules locally before applying them to remote machines, 
this approach can backfire though

> Say you're trying to use puppet to change the permissions of some files on the nose locking down some paths that you
> don't think that your users will need. Now imagine you try out the rules on your computer and discover you made a
> mistake and locked yourself out

What can be done?

There are few ways of test changes made on Puppet

1. `puppet parser validate` command with **noop** parameter
   
   * Checks that the syntax of the manifests is correct
   
   * **--noop** parameter which comes from no operations makes puppet simulate what it would do without actually
    doing it

You can look at the list of actions that it would take and check that they're exactly what you wanted puppet to do.
    
But if the change is complex, it's likely that we'll miss something important when looking at the planned actions

2. Separate test machines that are used only for testing out changes
    * You can apply the rules there and after a puppet has run check that everything's working correctly

But again, this is a manual process and we might forget to verify something important

3. Automated testing via **R-Spec**

We can set the facts involved different values and check that the catalog ends up stating what we wanted it to

```puppet

describe 'gksu', :type => :class do
    let (:facts) { { 'is_virtual' => 'false' } }
    it { should contain_package('gksu').with_ensure('latest') }
end

```

Test like this one can be a useful way to check that our catalog is written correctly and they can be super helpful
when a rule is used a lot of facts that interact with each other and we want to check that the result is actually
what we intended

We can write a bunch of these tests and run them automatically whenever there is a change to the rules this way we
can be sure that the rules stay valid and know that the new changes didn't break the old rules, but that's just
checks that the catalog contains the rules that we set should contain

How can we verify that these rules actually have the effects we want like enabling the corporate website or setting
up a strict firewall?
 
We need to apply the rules on the nodes and check that the result is correct

We can automate this process to, to do this we can use the set of test machines where we first apply the catalog and
then use scripts to check that the machines are behaving correctly

---

### Safely Rolling out Changes and Validating Them

Now, let's assume all your tests were successful and the change is ready to be published. How do you push it safely
to your whole fleet?

Once you've prepared and tested the changes that you want to make, it's time to roll them out

> If you host a website, the servers that deliver the website content to the users are the production servers. Inside
> your company, the servers that validate users passwords are the production authentication servers

Even if you've tested the change on your computer or on a test computer and it worked just fine, __it doesn't mean
that the change will work correctly on all machines running in production__.

In an infrastructure context, **production** is the parts of the infrastructure where a service is executed and
served to its users.

Making changes to the production servers can be tricky because if something goes wrong, the service can go down.

So how can we roll out changes safely?

The key is to always run them through a test environment first.

The test environment should have one or more machines running the exact same configuration as the production
environment. But these machines aren't actually serving any users of the service.

This way, there's a problem when deploying the changes should be able to fix it without any actual users seeing it.

Puppet has environments baked in. Each environment has its own directory with its own set of manifests and modules.

Puppet environments lets us fully isolate the configurations that the agency depending on what environment they're
running

This isn't just what nodes install which modules, it's also the whole contents of the modules

> For example, we can use this to try out a whole new version of the Apache module for the machines in the test
> environment while still using the old version for the production environments

___You can define as many environments as you need___

For example -

* You could have a development environment for IT specialists to try out new Puppet rules before they even reach the
test environment

* Or say you're developing a very tricky new feature for your system and you don't know when it'll be ready. You
could have an environment for testing just that specific feature

Now, let's assume that you have a bunch of changes ready to roll out. You'll usually push them to the machines in the
test environment first and check that everything works well there

This can include both manual verification and automated checking.

Say the changes worked fine in the test environment, how do you roll them out to the other machines in your fleet?

You might be tempted to just apply the changes to all the machines and be done with it

* But pushing changes to every machine at the same time is usually not a great idea. It's always possible that we
missed some special case when preparing the change which wasn't part of our test environment and suddenly, half our
fleet is offline.

So instead of pushing the changes to all nodes, we usually do it in batches

There's a bunch of ways you can do this depending on how your fleet is arranged

You could have some machines with the fact that marks them as early adopters or canaries. Like the canaries that coal
miners used to detect toxic gases in the mines, these nodes detect potential issues before they reach the other
computers

So you could push the changes to the canaries on one day, check that everything's working fine, and then deploy them
to the rest of the fleet on the next day.

That way, if there's an issue with the changes that wasn't caught in testing, only a subset of the users might see it.

As soon as you get notified of the problem, you can roll it back and avoid it hitting the rest of the fleet.

It's a good idea for these changes to be small and self-contained. That way, if something breaks, it's much easier to
figure out where the problem was

> Imagine you're trying to push six months worth of changes to your fleet of computers. When you push this to the
> machines in the test environment, you discover that they stop responding all together. You now need to comb through
> all the changes that were bundled together to try to find out which one is causing the problem

Instead, you could aim to roll out your changes every one or two weeks. This would mean that whenever a problem is
detected, there's only a small list of changes to go through to figure out the culprit

Of course, there's a lot more to say about testing and releasing changes safely. But you don't need to put all the
best practices in place to get started. You could start small and make improvements as you go. As your manifests get
more complex, you want to improve the automated testing of all the pieces.

As you managed with your configuration management system grows in size, you want to increase the size of your
testing environment, move some nodes to canaries and so on

---

### Extra Resources for Updating Deployments

* [R-Spec Puppet Tutorial](https://rspec-puppet.com/tutorial/)

* [Puppet Linter](http://puppet-lint.com/)
