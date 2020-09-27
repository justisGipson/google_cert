# Configuration Management and the Cloud - Week 1


## Learning Objectives

Look into how automation can be applied to manage fleets of computers by:

* Learn about configuration management, which lets us manage the configuration of our computers at scale

* Learn how to use **Puppet**, the current industry standard for configuration management

* Learn how to make use of the cloud to help us scale our infrastructure

* Learn about the benefits and challenges of moving services to the Cloud

* Learn the best practices for handling hundreds of virtual machines running in the Cloud

---

## Introduction to Automation at Scale


### Intro

No matter the size of your team or the number of computers in your fleet, knowing how to apply automation techniques
will enable you to do your work much more effectively

Being able to automate the installation of new software, the provisioning of new workstations or the configuration o
a new server can make a big difference even when you're the only person in your IT department

### What is scale

Being able to **scale** means keep achieving larger impacts with the same amount of effort.

A scalable system is a **flexible**

> For example, if the web application your company provides is scalable, that it can handle an increase in the number
> of people using it by adding more servers to serve requests.

Adding more computers to the pool of servers that are serving the website can be a very simple or very hard operation
depending on how your infrastructure is set up

To figure out how scalable your current setup is, you can ask yourself questions like:  

* Will adding more servers increase the capacity of the service?

* How are new servers prepared, installed, and configured?

* How quickly can you set up new computers to get them ready to be used

* Could you deploy a hundred servers with the same IT team that you have today?

* Would all the deployed servers be configured exactly the same way?

Scaling isn't just about website serving content of course.

If your company is rapidly hiring a lot of new employees, you'll need to have an on-boarding process that can scale as
needed. And as you keep adding new computers to the network, you'll need to make sure that your system
administration process can scale to the growing needs of the company

This can include tasks like:

* applying the latest security policies and patches while making sure users' needs still get addressed

* while more and more users join the network without new support staff to back you up

**Automation** is an essential tool for keeping up with the infrastructure needs of a growing business.

By using the right automation tools, we can get a lot more done in the same amount of time.

> For example, we could deploy a whole new server by running a single command and letting the automation take care of
> the rest. We could also create a batch of user accounts with all the necessary permissions based on data already
> stored in the database, eliminating all human interaction. 

Automation is what lets us scale. It allows a small IT team to be in charge of hundreds or even thousands of computers.

---

### What is configuration management

> Imagine your team is in charge of setting up a new server. This could be a physical computer running close to you
> or a virtual machine running somewhere in the cloud. To get things moving, the team installs the operating system
>, configures some applications and services, sets up the networking stack, and when everything is ready, puts the
> server into use.

* **Configuration** everything from the current operating system and the applications installed to any necessary
configuration files or policies, including anything else that's relevant for the server to do its job

When you work in IT, you're generally in charge of the configuration of a lot of different devices, not just servers
Network routers printers and even smart home devices can have configuration that we can control.

> For example, a network switch might use a config file to set up each of its ports.

**Unmanaged configuration** manually deploys the installation and configuring a computer.

**Managed configuration** uses a **configuration management system** to handle all of the configuration of the
 devices or **nodes** which aims to solve the scaling problem.

* Typically you'll define a set of rules that have to be applied to the nodes you want to manage and then have a
process that ensures that those settings are true on each of the nodes

At a small scale, unmanaged configurations seem inexpensive. If you only manage a handful of servers, you might be
able to get away with doing that without the help of automation. You could log into each device and make changes by
hand when necessary. And when your company needs a new database server, you might just go ahead and manually
install the OS and the database software into a spare computer

But this approach doesn't always scale well. The more servers that you need to deploy, the more time it will take you
to do it manually

And when things go wrong, and they often do, it can take a lot of time to recover and have the servers back online.

Configuration management systems aim to solve this scaling problem. By managing the configuration of a fleet with a
system like this, large deployments become easier to work with because the system will deploy the configuration
automatically no matter how many devices you're managing

When you use configuration management and you need to make a change in one or more computers, you don't manually
connect to each computer to perform operations on it. Instead, you edit the configuration management rules and then
let the automation apply those rules in the affected machines.

Configuration management system allows a way to make changes to a system or group of systems in a **systematic**, **repeatable way**.

Being repeatable is important, because it means that the results will be the same on every device

A configuration management tool can take the rules you define and apply them to the systems that it manages, making
changes efficient and consistent

Configuration management systems often also have some form of automatic error correction built in so that they can
recover from certain types of errors all by themselves

> For example, say you found that some application that was being used widely in your company was configured to be
> very insecure. You can add rules to your configuration management system to improve the settings on all computers
>. And this won't just apply the more secure settings once. It will continue to monitor the configuration going
> forward. If a user changes the settings on their machine, the configuration management tooling will detect this
> change and reapply the settings you defined in code.

There are lots of configuration management systems available in the IT industry today. Some popular systems include: 

* [Puppet](https://www.puppet.com)

* [Chef](https://www.chef.io)

* [Ansible](https://www.ansible.com)

* [CFEngine](https://www.cfengine.com)

These tools can be used to manage locally hosted infrastructure. Think bare metal or virtual machines, like the
laptops or work stations that employees use at a company

Many also have some kind of Cloud integration allowing them to manage resources in Cloud environments like:

* [Amazon EC2](https://aws.amazon.com/ec2/)

* [Microsoft Azure](https://azure.microsoft.com/)

* [Google Cloud Platform](https://cloud.google.com)

There are some platform specific tools like:

* [SCCM](https://docs.microsoft.com/en-us/mem/configmgr/core/understand/introduction)

* [Group Policy for Windows](https://en.wikipedia.org/wiki/Group_Policy)

Keep in mind though that selecting a configuration management system is a lot like deciding on a programming language
or version control system. You should pick the one that best fits your needs and adapt accordingly, if necessary.

Each has its own strengths and weaknesses. So a little research beforehand can help you decide which system is best
suited for your particular infrastructure needs

---

### What is infrastructure as code

When we use a configuration management system, we write rules that describe how the computers in our fleet should be
configured

These rules are then executed by the automation, to make the computers match our desired state.

This means that we can model the behavior of our IT infrastructure in files that can be processed by automatic tools.

These files can then be tracked in a version control system. Remember, version control systems help us keep track of
all changes done to the files, helping answer questions like who, when, and why... 

**Infrastructure as Code** or **IaC** is the paradigm of storing all the configuration for the managed devices in
version controlled files. This is then combined with automatic tooling to actually get the nodes provisioned and
managed.

**IaC** - When all the configurations necessary to deploy and manage a node in the infrastructure is stored in
version control. This is then combined with automatic tooling to actually get the nodes provisioned and managed.

The principals of Infrastructure as Code are commonly applied in __cloud computing environments__, where machines are
treated like __interchangeable resources__, instead of individual computers.

This principle is also known as treating your computers as cattle instead of pets because you care for them as a
group rather than individually

This concept isn't just for managing computers in huge data centers or globe spanning infrastructures, it can work
for anything; from servers to laptops, or even workstations in a small IT department

    Even if your company only has a single computer working as the mail server, 
    you can still benefit from storing all the configuration needed to set it 
    up in a configuration management system

One valuable benefit of this process is that the configuration applied to the device doesn't depend on a human
remembering to follow all the necessary steps

IaC allows the followings:

* Makes the deployment consistent

* Applies the benefits of the version control system to the infrastructure

* Run automated tests on the files

It gives us an audit trail of changes, it lets us quickly rollback if a change was wrong, it lets others reviewed our
code to catch errors and distribute knowledge, it improves collaboration with the rest of the team, and it lets us
easily check out the state of our infrastructure by looking at the rules that are committed

The ability to easily see what configuration changes were made and roll back to a known good state is super important
. It can make a big difference in quickly recovering from an outage, especially since changing the contents of the
configuration file can be as dangerous as updating the version of an application

In a complex or large environment, treating your IT Infrastructure as Code can help you deploy a flexible scalable
system. 

A configuration management system can help you manage that code by providing a platform to maintain and
provision that infrastructure in an automated way.

Having your infrastructure stored as code means that you can automatically deploy your infrastructure with very
little overhead.

If you need to move it to a different location, it can be deployed, de-provisioned, and redeployed at scale in a
different locale with minimal code level changes

Managing your Infrastructure as Code it means that the fleet of nodes are **consistent, versioned, reliable, and repeatable**.

Instead of being seen as precious or unique, machines are treated as replaceable resources that can be deployed on
-demand through the automation

Any infrastructure that claims to be scalable must be able to handle the capacity requirements of growth

Performing an action like adding more servers to handle an increase in requests is just a possible first step. There
are other things that we might need to take into account, such as the amount of traffic that network can handle or
the load on the back-end servers like databases

Viewing your infrastructure in this way helps your IT team adapt and stay flexible. The technology industry is
constantly changing and evolving. Automation and configuration management can help you embrace that change instead
of avoiding it

---

## Introduction to Puppet


### What is Puppet

[Puppet](https://www.puppet.com) is the current industry standard for managing the configuration of computers in a
fleet of machines. 

Puppet is:

* Cross-platform

* Open source project

Puppet is typically deploy using a client-server architecture.

* The client is known as the Puppet agent

* Te service is known as the Puppet master

When using this model,

1. The agent connects to the master and sends a bunch of facts that describe the computer to the master

2. The master then processes this information, generates the list of rules that need to be applied on the device

3. The master sends this list back to the agent

4. The agent is then in charge of making any necessary changes on the computer

Puppet is a cross-platform application available for all Linux distributions, Windows, and Mac OS. This means that
you can use the same puppet rules for managing a range of different computers.

Example block below says that the package 'sudo' should be present on every computer where the rule gets applied.

```puppet

class sudo {
    package { 'sudo':
        ensure => present,
    }
}

```

There are various installation tools available depending on the type of operating system. Puppet will determine the
type of operating system being used and select the right tool to perform the package installation

Linux - **APT**, **Yum**, **DNF**

Puppet will also determine which package manager should be used to install the package

On Mac OS, there's a few different available providers depending on where the package is coming from. The Apple
Provider is used for packages that are part of the OS, while the MacPorts provider is used for packages that come
from the MacPorts Project

For Windows, we'll need to add an extra attribute to our rule, stating where the installer file is located on the
local disk or a network mounted resource. Puppet will then execute the installer and make sure that it finishes
successfully

If you use Chocolatey to manage your windows packages, you can add an extra Chocolatey provider to Puppet to support
that

Using rules like this one, we can get puppet to do a lot more than just install packages for us

Tasks Puppet can accomplish includes:

* Install packages

* Add, remove, or modify configuration files stored in the system

* Change registry entries on Windows

* Enable, disable, start, or stop the services

* Configure crone jobs

* Schedule tasks

* Add, remove, or modify Users and Groups

* Execute external commands

---

### Puppet Resources


**Resources** are the basic unit for modeling the configuration that we want to manage in Puppet.

* Each resource specifies one configuration that we're trying to manage, like a service, a package, or a file

Below example is s a simple rule that ensures that etc/sysctl.d exists and is a directory.

```puppet

class sysctl {
    # resource type: file
    # resource title: '/etc/sysctl.d'
    file { '/etc/sysctl.d':
        # resource attributes
        ensure => directory,
    }
}

```

Syntax - write them in a block that starts with the resource type ,in this case File. The configuration of the
resource is then written inside a block of curly braces. Right after the opening curly brace, we have the title of
the resource, followed by a colon. After the colon come the attributes that we want to set for the resource

Below examples uses a file resource to configure the contents of etc/timezone, a file, which is used in some Linux
distributions to determine the time zone of the computer.

```puppet

class timezone {
    # resource type: file
    # resource title: '/etc/timezone'
    file { '/etc/timezone':
        # resource attributes
        # this will be a file instead of a directory or a symlink
        ensure => file,

        # the contents of the file will be the UTC time zone
        content => "UTC\n",

        # the contents of the file will be replaced even if the file already exists
        replace => true,
    }
}

```

There are a lot more attributes that we could set, like file permissions the file owner, or the file modification time.

How do these rules turn into changes in our computers?

When we declare a resource in our puppet rules. We're defining the desired state of that resource in the system. The
puppet agent then turns the desired state into reality using providers.

The provider used will depend on the resource defined and the environment where the agent is running. Puppet will
normally detect this automatically without us having to do anything special

When the puppet agent processes a resource, it first decides which provider it needs to use, then passes along the
attributes that we configured in the resource to that provider.

The code of each provider is in charge of making our computer reflect the state requested in the resource.

---

### Puppet Classes


**Classes** in Puppets are used to collect the resources that are needed to achieve a goal in a single place.

> For example, you could have a class that installs a package, sets the contents of a configuration file, and starts
> the service provided by that package



Below example groups all of the resources related to NTP in the same class to make changes in the future easier.

```puppet

# a class with three resources related to the Network Time Protocol, or NTP
# rules make sure that the NTP package is always upgraded to the latest version
class ntp {
    package { 'ntp':
        ensure => latest,
    }
    # contents of the file will be based on the source attribute
    # agent will read the requiured contents from the specified location
    file { '/etc/ntp.conf':
        source => 'puppet:///modules/ntp/ntp.conf',
        replace => true,
    }
    # enable and run the NTP service
    service { 'ntp':
        enable => true,
        ensure => running,
    }
}

```

* **NTP** is the mechanism computers use to synchronize their clocks

By grouping all of the resources related to NTP in the same class, we only need a quick glance to understand how the
service is configured and how it's supposed to work

This would make it easier to make changes in the future since we have all the related resources together. It makes
sense to use this technique whenever we want to group related resources

> For example, you could have a class grouping all resources related to managing log files, or configuring the time
> zone, or handling temporary files and directories. 
>
> You could also have classes that group all the settings related to your web serving software, your email
> infrastructure, or even your company's firewall 

---

### Extra Puppet Resources

* [Resources](https://puppet.com/docs/puppet/latest/lang_resources.html)

* [Deploy Packages Across Your Windows Estate with Bolt and Chocolatey](https://puppet.com/blog/deploy-packages-across-your-windows-estate-with-bolt-and-chocolatey/)

---

## The Building Blocks of Configuration Management


### What are domain-specific languages

These resources are the building blocks of Puppet rules, but we can do much more complex operations using Puppet's
**Domain Specific Language** or **DSL**. 

Typical programming languages like **Python**, **Ruby**, **Java** or **Go** are general purpose languages that can be
used to write lots of different applications with different goals and use cases

A **Domain Specific Language** is a programming language that's more limited in scope

Learning a domain-specific language is usually much faster and easier than learning a general purpose programming
language because there's a lot less to cover

You don't need to learn as much syntax or understand as many keywords or taking to account a lot of overhead in general

In the case of Puppet, the DSL is limited to operations related to when and how to apply configuration management
rules to our devices. 

> For example, we can use the mechanisms provided by the DSL to set different values on laptops or desktop computers
> or to install some specific packages only on the company's web servers

On top of the basic resource types that we already checked out, Puppet's DSL includes variables, conditional
statements, and functions.

Using them, we can apply different resources or set attributes to different values depending on some conditions

Let's talk a bit about Puppet facts. Facts are variables that represent the characteristics of the system. When the
Puppet agent runs, it calls a program called factor which analyzes the current system, storing the information it
gathers in these facts. Once it's done, it sends the values for these facts to the server, which uses them to
calculate the rules that should be applied

Puppet comes with a bunch of baked-in core facts that store useful information about the system like what the current
OS is, how much memory the computer has whether it's a virtual machine or not or what the current IP address is

If the information we need to make a decision isn't available through one of these facts, we can also write a script
that checks for the information and turns it into our own custom fact.

Let's check out an example of a piece of Puppet code that makes use of one of the built-in facts. This piece of code
is using the is-virtual fact together with a conditional statement to decide whether the **smartmontools** package
should be installed or purged. 

The **smartmontools** package is used for monitoring the state of hard drives using smart. So it's useful to have it
installed in physical machines, but it doesn't make much sense to install it in our virtual machines. 

First, facts is a variable. All variable names are preceded by a **$** in Puppet's DSL. In particular, the
facts variable is what's known as a **hash** in the Puppet DSL, which is equivalent to a dictionary in Python. This
means that we can access the different elements in the hash using their keys. 

In this case, we're accessing the value associated to the is virtual key. Second, we see how we can write a
conditional statement using if else, enclosing each block of the conditional with curly braces. Finally, each
conditional block contains a package resource. 

We've seen resources before, but we haven't looked at the syntax in detail. So let's do that now. Every resource starts
with the type of resource being defined. 

In this case, **package** and the contents of the resource are then enclosed in curly braces. Inside the resource
definition, the first line contains the title followed by a colon. Any lines after that are attributes that are being
set. We use **=>** to assign values to the attributes and then each attribute ends with a comma

```puppet

if $facts['is_virtual']{
    package {'smartmontools':
        ensure => purged,
    }
}
else {
    package {'smartmontools':
        ensure => installed,
    }
}

```

While each tool uses their own DSL, they're usually very simple and can be learned very quickly

---

### The Driving Principles of Configuration Management

The providers that we mentioned earlier lake **apt** and **yum** are the ones in charge of turning our goals into
whatever actions are necessary

Unlike Python or C which are called **procedural languages**, because we write out the procedure that the computer
needs to follow to reach our desired goal, Puppet is a **declarative language** because the desired state is declared
rather than writing the steps to get there.

___Remember that when it comes to configuration management, it makes sense to simply state what the configuration
should be, not what the computer should do to get there___

There are three important principles of configuration management

1. Idempotency

2. Test and repair paradigm

3. Stateless

In configuration management, operations should be **idempotent**. 

In this context, an **idempotent** action can be performed over and over again without changing the system after the
first time the action was performed, and with no unintended side effects 

* **Idempotency** is a valuable property of any piece of automation. If a script is idempotency , it means that it can
fail halfway through its task and be run again without problematic consequences

```puppet

file { 'etc/issue':
    mode    => '6604'
    content => "Internal system \l \n,
}

```

This resource ensures that the **/etc/issue** file has a set of permissions and a specific line in it. Fulfilling this
requirement is an idempotent operation. If the file already exists and has the desired content, then Puppet will
understand that no action has to be taken

If the file doesn't exist, then puppet will create it. If the contents or permissions don't match, Puppet will fix
them. No matter how many times the agent applies the rule, the end result is that this file will have the requested
contents and permissions

Idempotency is a valuable property of any piece of automation. If a script is idempotent, it means that it can fail
halfway through its task and be run again without problematic consequences

> Say you're running your configuration management system to setup a new server. Unfortunately, the setup fails
> because you forgot to add a second disk to the computer and the configuration required two disks. If your
> automation is idempotent, you can add the missing disk and then have the system pick up from where it left off

* Most Puppet resources provide idempotent actions

* exec resource is NOT an idempotent actions though - exec modifies the system each time it's executed

> To understand this, let's check out what happens when we execute a command that moves a file on our computer. First
>, we'll check that the example.txt file is here, and then we'll move it to the desktop directory.

```puppet

exec {'move example file':
    command => 'mv /home/user/example.txt /home/user/Desktop',
    onlyif => 'test -e /home/user/example.txt',
}

```

This works fine now, but what happens if we run the exact same command again after it's been executed once? We
receive an error because the file is no longer in the same place. In other words, this was not an idempotent action
, as executing the same action twice produced a different result and the unintended side effect of an error. If we
were running this inside Puppet, this would cause our Puppet run to finish with an error

* This can be worked around by using the **onlyif** attribute

By adding this conditional, we've taken an action that's not idempotent and turned it into an idempotent one

Another important aspect of how configuration management works is the **test and repair paradigm**. This means that
actions are taken only when they are necessary to achieve a goal.

Puppet will first test to see if the resource being managed like a file or a package, actually needs to be modified
. If the file exists in the place we want it to, no action needs to be taken. If a package is already installed
, there's no need to install it again

Finally, another important characteristic is **stateless**, this means that there's no state being kept between runs
of the agent.

Each Puppet run is independent of the previous one, and the next one

Each time the puppet agent runs, it collects the current facts

The Puppet master generates the rules based just on those facts, and then the agent applies them as necessary

### Extra Resources on Configuration Management

* [Domain Specific Language](https://en.wikipedia.org/wiki/Domain-specific_language)

* [Puppet Design Philosophy](http://radar.oreilly.com/2015/04/the-puppet-design-philosophy.html)

---
