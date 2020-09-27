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

**Managed configuration** uses a **configuration management system** to handle all of the configuration of the devices in the **nodes** which aims to solve the scaling problem.

* Typically you'll define a set of rules that have to be applied to the nodes you want to manage and then have a process that ensures that those settings are true on each of the nodes

Configuration management system allows a way to make changes to a system or group of systems in a **systematic**, **repeatable way**.

---

### What is infrastructure as code

**Infrastructure as Code** or IaC is the paradigm of storing all the configuration for the managed devices in version controlled files. This is then combined with automatic tooling to actually get the nodes provisioned and managed.

The principals of Infrastructure as Code are commonly applied in __cloud computing environments__, where machines are treated like __interchangeable resources__, instead of individual computers.

IaC allows the followings:

* Makes the deployment consistent
* Applies the benefits of the version control system to the infrastructure
* Run automated tests on the files

In a complex or large environment, treating your IT Infrastructure as Code can help you deploy a flexible scalable system. A configuration management system can help you manage that code by providing a platform to maintain and provision that infrastructure in an automated way.

Managing your Infrastructure as Code it means that the fleet of nodes are **consistent, versioned, reliable, and repeatable**.

---

## Introduction to Puppet


### What is Puppet

Puppet is the current industry standard for managing the configuration of computers in a fleet of machines. Puppet is:

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

Below example says that the package 'sudo' should be present on every computer where the rule gets applied.

```puppet

class sudo {
    package { 'sudo':
        ensure => present,
    }
}

```

Tasks Puppet can accomplish includes

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

Below examples uses a file resource to configure the contents of etc/timezone, a file, which is used in some Linux distributions to determine the time zone of the computer.

```puppet

class timezone {
    # resource type: file
    # resource title: '/etc/timezone'
    file { '/etc/timezone':
        # resource attributes
        # this will be a file instead of a directory or a symlink
        # the contents of the file will be the UTC time zone
        # the contents of the file will be replaced even if the file already exists
        ensure => file,
        content => "UTC\n",
        replace => true,
    }
}

```

When we declare a resource in our puppet rules. We're defining the desired state of that resource in the system. The puppet agent then turns the desired state into reality using providers.

---

### Puppet Classes

**Classes** in Puppets are used to collect the resources that are needed to achieve a goal in a single place.

Below example groups all of the resources related to NTP in the same class to make changes in the future easier.

```puppet

# a class with three resources related to the Network Time Protocol, or NTP
# rules make sure that the NTP package is always upgraded to the latest version
class ntp {
    package { 'ntp':
        ensure => latest,
    }
    # contents of the file will be based on the source attribute
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

---

## The Building Blocks of Configuration Management



### What are domain-specific languages

These resources are the building blocks of Puppet rules, but we can do much more complex operations using Puppet's domain specific language or DSL. 

a domain specific language is a programming language that's more limited in scope

In the case of Puppet, the DSL is limited to operations related to when and how to apply configuration management rules to our devices. 

On top of the basic resource types that we already checked out, Puppet's DSL includes variables, conditional statements, and functions.

Let's talk a bit about Puppet facts. Facts are variables that represent the characteristics of the system. When the
Puppet agent runs, it calls a program called factor which analyzes the current system, storing the information it
gathers in these facts. Once it's done, it sends the values for these facts to the server, which uses them to
calculate the rules that should be applied

Let's check out an example of a piece of Puppet code that makes use of one of the built-in facts. This piece of code
is using the is-virtual fact together with a conditional statement to decide whether the **smartmontools** package
should be installed or purged. This package is used for monitoring the state of hard drives using smart. So it's
useful to have it installed in physical machines, but it doesn't make much sense to install it in our virtual
machines. 

First, facts is a variable. All variable names are preceded by a dollar sign in Puppet's DSL. In particular, the
facts variable is what's known as a hash in the Puppet DSL, which is equivalent to a dictionary in Python. This means
that we can access the different elements in the hash using their keys. In this case, we're accessing the value
associated to the is virtual key. Second, we see how we can write a conditional statement using if else, enclosing
each block of the conditional with curly braces. Finally, each conditional block contains a package resource. We've
seen resources before, but we haven't looked at the syntax in detail. So let's do that now. Every resource starts
with the type of resource being defined. In this case, package and the contents of the resource are then enclosed
in curly braces. Inside the resource definition, the first line contains the title followed by a colon. Any lines
after that are attributes that are being set. We use equals greater than to assign values to the attributes and then
each attribute ends with a comma

```puppet

if $facts['is_virtual']{
    package{ 'smartmontools':
        ensure => purged,
    }
}
else {
    package{ 'smartmontools':
        ensure => installed,
    }
}

```
---

### The Driving Principles of Configuration Management

Unlike Python or C which are called procedural languages, Puppet is a **declarative language** because the desired state is declared rather than writing the steps to get there.

There are three important principles of configuration management

1. Idempotency
2. Test and repair paradigm
3. Stateless

In configuration management, operations should be **idempotent**. In this context, an idempotent action can be performed over and over again without changing the system after the first time the action was performed, and with no unintended side effects Idempotency is a valuable property of any piece of automation. If a script is idempotent, it means that it can fail halfway through its task and be run again without problematic consequences

* Most Puppet resources provide idempotent actions
* exec resource is NOT an idempotent actions though - exec modifies the system each time it's executed
  * This can be worked around by using the only if attribute

```puppet

exec {'move example file':
    command => 'mv /home/user/example.txt /home/user/Desktop',
    onlyif => 'test -e /home/user/example.txt',
}

```

Another important aspect of how configuration management works is the **test and repair paradigm**. This means that actions are taken only when they are necessary to achieve a goal.

Finally, another important characteristic is **stateless**, this means that there's no state being kept between runs of the agent.

---
