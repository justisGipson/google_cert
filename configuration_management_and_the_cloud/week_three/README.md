# Crash Course of Python - Week 3

## Learning Objectives

The Cloud is a super useful tool in IT for increasing productivity

Dive into the details of the different Cloud services, when it makes sense to use them, and how to get the most out
of the cloud deployments by:

* Learn how cloud deployments can help us quickly scale our services

* Learn the differences between when running IT infrastructure on-premise versus running it in the cloud

* Learn how we can use a variety of different tools to manage instances running in the cloud

---

## Cloud Computing



### Cloud Services Overview

A service is running in the Cloud means that the service is running somewhere else, either in a data center or in
other remote servers that can be __reached over via Internet__.

These data centers house a large variety of machines, different types of machines are used for different services

Some machines may have local solid-state drive or SSD, for increased performance while others may rely on virtual
drives mounted over the network to lower costs

Cloud providers typically offer different service types such as:

* **Software as a Service** or **SaaS**, is when a Cloud provider delivers an entire application or program to the
 customer

  * The Cloud provider manages everything related to the service for you including deciding where it's hosted
  , ensuring the service has enough capacity to serve your needs, performing backups frequently and reliably, and a
   lot more
   
There's a lot of software being offered as a service by many different Cloud providers or other Internet companies

* **Platform as a Service** or **PaaS**, is when a Cloud provider offers a preconfigured platform to the customer
  
  * When we say platform here, it can be a bit confusing because there are lots of different platforms that exist
   under a PaaS model

> Say you need an SQL database to store some of your applications data, you could choose to host the database in your
> own hardware. To do this, you'd need to install an operating system on that computer and then install the SQL
> software on top of the chosen OS. This requires a basic understanding of all of these different pieces just to get
> the database running.

There's a bunch of things that could go wrong and even if you can eventually solve all of them, it can take awhile.

Instead, you could decide to use a Cloud provider that offers an SQL database as a service, that way you can just
focus on writing SQL queries and using the platform, and let the Cloud provider take care of the rest

There's a bunch of different platforms offered as a service by Cloud providers, but of course they are unlikely to
cover all of your needs

* **Infrastructure as a Service** or **IaaS**, is when a Cloud provider supplies only the bare-bones computing
experience

Generally, this means a virtual machine environment and any networking components needed to connect virtual machines
, the Cloud provider won't care what you're using the VMs for

You could use them to host a web server, a mail server, your own SQL database with your own configuration settings
, or a whole lot more possibilities

Running your IT infrastructure on the Cloud provider's IaaS offering is a very popular choice. There's a lot of
different providers out there, big and small that offer a service where you can run virtual machines in their Cloud

**IaaS** products include:
  
  * ___Amazon EC2___
  
  * ___Google Compute Engine___
  
  * ___Microsoft Azure Compute___

When setting up Cloud resources, **regions** need to be considered. 

A **region** is a geographical location containing a number of data centers, regions contain **zones** and zones can
contain one or more physical **data centers**.

If one of them fails for some reason, the others are still available and services can be migrated without notably
affecting users.

Large Cloud providers usually offer their services in lots of different regions around the world

Generally, the region and zone you select should be closest to your users, the further your users are from the
physical data center the more latency they may experience

There are multiple factors that is determined based on the selected region,

* Latency

* Legal or policy factors

* Other services as dependencies, it's a good idea to host the service physically close to its dependencies

---

### Scaling in the Cloud

In a traditional IT setting, if your team needs an extra server to improve the service, you need to buy additional
hardware, install the operating system and application software and then integrate the new computer with the rest of
the infrastructure

Doing all of these takes time so it's not easy to quickly scale up or down if the service gets more or less usage.

___In other words, it takes a significant amount of time to modify the capacity of the deployment___

Capacity is how much the service can deliver.

The available capacity is tied to the number and size of servers involved. We get more capacity by adding more
servers or replacing them with bigger servers.

The way we measure the capacity of a system depends on what the system is doing

* If we're storing data, we might care about the total disk space available.

* If we have a web server responding to queries from external users we might care about **Queries per second** or
 **QPS**
 
* Or maybe the total bandwidth served in an hour.

__Our capacity needs can change over time__

> Say you're hosting an e-commerce site that needs a hundred servers to meet user demands. As the service becomes
> more popular, demand might grow and you'll need to increase the available capacity. Eventually, the system could
> need a thousand servers to meet user demands.

This capacity change is called scaling:

* **Up-scaling** when the capacity is being increased

* **Down-scaling** when the capacity is being decreased

This could happen for example if the demand for a product decreased or if the system was improved to need fewer
resources

Cloud providers typically have a lot of available capacity that can be used by their customers.

When we choose to host our infrastructure in the Cloud, we're purchasing and using some of the providers capacity to
supplement or completely replace our on-premise capacity. This lets us easily scale our service to satisfy demand.

There are a couple of different ways that we can scale our service in the Cloud:

* **Horizontal scaling** vs. **Vertical scaling**

  * Horizontally scaling scales the capacity by adding more nodes into the pool (eg. add more servers)
  
    > Say your web service is using Apache to serve web pages. By default, Apache is configured to support a 150
    > concurrent connections. If you want to be able to serve 1,500 connections at the same time, you can deploy 10
    > Apache web servers and distribute the load across them

    You add more servers to increase your capacity. If the traffic goes up you could just add more servers to keep
    up with it.
  
  * Vertically scaling scales the capacity by making the nodes bigger (eg. upgrade memories, CPU or disk space)
  
  For example, a database server with a 100 gigabytes of disk space can store more data than with only 10 gigabytes
  of space. To scale this deployment we can just add a bigger disk to the machine and the same idea works for a CPU
  and memory too.
  
    >Say you have a caching server and you notice it's using 95 percent of the available memory. You can deal with that by adding more memory to the node.

Depending on our deployment and our needs, we might need to scale both horizontally and vertically to scale the
capacity of our service. In other words, adding more and bigger nodes to our pool

This approach to scaling isn't too different from what you'd need to do if you have your servers running on-premise

Instead of sending someone to change the physical deployment, for example adding more physical RAM to a server or
adding 10 more physical machines in a server rack, we just modify our deployment by clicking some buttons in a web
UI or using a configuration management system to automate the scaling for us

The infrastructure built by the Cloud provider will deploy any additional resources we need.

When talking about scaling in the Cloud, another aspect we need to take into account is whether the scaling is done
automatically or manually

* **Automatic scaling** vs. **Manual scaling**

  * Automatic scaling uses metrics to automatically increase or decrease the capacity of the system which is
   controlled by the Cloud provider
  
  * Manual scaling are controlled by humans instead of software
  
Manual scaling has its pros and cons too. When the Cloud deployment isn't very complex, it's usually easier for
smaller organizations to use manual scaling practices.

Say your company currently has a single mail server and you know that you'll want to have another one in six months
. In that case, there's no need to overcomplicate that system with an autoscaler

You could simply add the extra server sometime along the way. The trade-off here is that without good monitoring or
alerting, a system without autoscaling technologies might suffer from unexpected increases in demand

If you're using manual scaling for a service that becomes popular and demand grows quickly, you might not be able to
increase the capacity quickly enough. This can store up lots of problems ranging from poor performance to an actual
outage.

Cloud technology offers a ton of benefits for an IT team

---

### Evaluating the Cloud

When you're running the service yourself, if something breaks, you can either physically walk up to the server to fix
it or SSH into it from inside the same network. You can apply a quick fix and have your users back to being
productive in no time.

As part of the IT team, you own the hardware, software, the network connections, and anything in between, which lets
you have a lot of control over what's going on in the whole system

In the case of cloud solutions, the IT team is giving up some of its control to the cloud provider. Therefore, it's
important to know what kind of support is available and select the one that fits the needs.

We have different levels of control depending on the service model that we choose, whether that's software, platform
, or infrastructure as a service

When choosing to use software as a service, we're basically giving the provider complete control of how the
application runs. We have a limited amount of settings that we can change, but we don't need to worry about making
the system work.

With platform as a service, we're in charge of the code, but we aren't in control of running the application. Just
the creation of the application

Or we can choose infrastructure as a service, where we can still keep a high level of control. We decide the
operating system that runs on the virtual machines, the applications that are installed on it, and so on.

We'll still depend on the vendor for other aspects of the deployment, like the network configuration or the service
availability. If something does break, you might need to get support from the vendor to fix the problem.

So when choosing a cloud provider, it's important to know what kind of support is available and select the one that
fits your needs

Treat the servers executing the workloads as a **commodity** and always use reasonable judgment to protect the
machines that we deploy, whether that's on physical server is running on-premise or on virtual machines in the Cloud.

One aspect that might make you hesitant to move to the cloud is that you don't know exactly what security measures
are being put in place.

So when selecting which provider to use, it's important that you check how they're keeping your instances and your
data secure.

There are a bunch of certifications like **SOC 1**, **ISO 27001**, and other industry recognized credentials that you
can look for to verify that your provider has invested in security

Once you're sure that your provider is taking the right security measures, it might be tempting to just leave
security to the professionals and forget about it. But as cloud users, we also have a responsibility to follow
reasonable security practices

Google, Amazon, Microsoft, and other cloud providers invest heavily in security research

But that won't matter if the root password of your cloud instance `password1` or the instance doesn't use a firewall

___In other words, we should always use reasonable judgment to protect the machines that we deploy ,whether that's on
physical server is running on-premise or on virtual machines in the Cloud___

It's also important to keep in mind that security systems can be expensive to implement correctly

Some highly sensitive deployments might warrant specialized security procedures, like multi-factor authentication
, encrypted file systems, or public key cryptography.

But these processes can also be expensive to implement. It's worth considering if using these techniques is necessary
for your specific use case

> If your application stores recent patient health records, that's super important data that needs to be protected
>. You want to apply the most stringent security practices. But if you're dealing with patient health records from
> the 1800s, you'll need less comprehensive security measures, since this data is much less sensitive, given its age

There's a bunch of other reasons why you might have doubts about cloud providers

> For example, you might be worried of where your data is going to be stored. Or you might fear that the support
> offered won't satisfy your needs.

No matter the reason, It's important that you carefully read the terms of service to understand the conditions and
figure out if the service offered will satisfy your needs

---

### Migrating to the Cloud

A lot of companies today are looking into migrating at least part of their IT infrastructure to the Cloud. 

The details of the migration will depend on what your infrastructure currently looks like, and what you're trying t
achieve by migrating to a Cloud provider

In general, we're looking at a trade-off between how much control we have over the computers providing the services
and how much work we need to do to maintain them.

When we use **Infrastructure as a Service** or **IaaS**, we deploy our services using virtual machines running on the
Cloud providers infrastructure. We have a lot of control over how the infrastructure is designed which can be super
useful

**IaaS** is especially useful to administrators using a **lift and shift strategy**.

> Say you work at a small organization that's expanding. As the company grows, physical space for employees; desks
>, ping pong tables, and printers becomes scarce. Eventually, the whole office might need to move to a larger space
>. This means moving not just the desks and printers, but also any servers running on-premise. If physical servers
> need to be moved, you might need to take a server from the old office, turn it off during a maintenance window
>, load it onto a truck, and physically drive it to the new location. This could be the new office or maybe even a
> small data center.

So you're literally lifting the server and moving it to a new location, that's where the lift in lift and shift comes
from

When migrating to the Cloud, the process is somewhat similar. But instead of moving the physical server in the back
of a truck, you migrate your physical servers running on-premise to a virtual machine running in the Cloud. In this
case, you're shifting from one way of running your servers to another. The key thing to note with both approaches, is
that **the servers core configurations stay the same**.

It's the same software that needs to be installed on the machine to provide its functionality, no matter if the
server is hosted physically on-site or virtually in the Cloud

If you've already been using configuration management to deploy and configure your physical servers, moving to a
Cloud setup can be pretty easy

You just have to apply the same configuration to the VMs that are running in the Cloud and you'll have replicated the
setup

On the flip side, using this strategy means that you still have to install and configure the applications yourself.
You need to make sure that both the OS and the software stay up to date, that no functionality breaks when they get
updated, and a bunch of other things depending on which specific application the server is running.

One alternative in this case is using **Platform as a Service** or **PaaS**

**PaaS** is well-suited for when you have a specific infrastructure requirement, but you don't want to be involved in
the day-to-day management of the platform

> We mentioned the example of an SQL database that could be used in this way

By leaving the management of the database to the Cloud provider, you don't need to worry about having the right disks
attached to the computer, configuring the database or any other task related to the machine setup

Instead, you can focus on just using the database

Another example of Platform as a Service are managed web applications. When using this service, you only have to care
about writing the code for the web app. You don't need to care about the framework for running it.

This can accelerate development because developers don't have to spend time managing the platform and can just focus
on writing code

Some popular managed web application platforms include:
  
   * Amazon Elastic Beanstalk
  
   * Microsoft App Service
  
   * Google App Engine
   
While these platforms are very similar, they aren't fully compatible. So migrating from an on-premise framework and
switching between vendors will require some code changes   

**Containers** are applications that are packaged together with their configuration and dependencies.

This allows the applications to run in the same way no matter the environment used to run them

___In other words, if you have a container running an application, you can deploy it to your on-premise server, to a
Cloud provider, or a different Cloud provider___

Whichever you choose, it will always run in the same way. This makes migrating from one platform to the other super
easy.

When talking about migrating to the Cloud, you may also hear about **Public Clouds**, **private Clouds**, **Hybrid
Clouds**, and **Multi-Clouds**

* **Public Cloud** is services provided by the third-party public Cloud providers

* **Private Cloud** is when one company owns the services and the rest of the infrastructure, on-site or remotely in
 a data center

* **Hybrid Cloud** is a mixture of both public and private Clouds. Some workloads are run on servers owned by your
 company, while others are run on servers owned by a third party.
 
  The trick to making the most of the hybrid Cloud is ensuring that everything is integrated smoothly. This way, you
  can access, migrate, and manage data seamlessly no matter where it's hosted.

* **Multi-Cloud** is a mixture of public and/or private Clouds across vendors, a multi-Cloud deployment may include
 servers hosted with Google, Amazon, Microsoft, and on-premise
 
A hybrid Cloud is simply a type of multi-Cloud, but the key difference is that multi-Clouds will use several vendors
, sometimes in addition to on-site services. Using multi-Clouds can be expensive, but it gives you extra protection

If one of your providers has a problem, your service can keep running on the infrastructure provided by a different
provider

---

## Managing Instances in the Cloud

There are different Cloud providers each with some specific advantages depending on what we are trying to achieve.
But usually Cloud service providers implement a console to manage the services.

Regardless of the service provider, following parameters needs to be set when creating a VM running in the Cloud

  * Name of the instance

  * Region and zone where the instance will be running

  * CPU, memory and boot disk options for the VM

Cloud service providers also provides the command line interface, which allows for us to specify what we want once,
and then use the same parameters many times.

__Using the command line interface lets us create, modify, and even delete virtual machines from our scripts.__

**Reference images** store the contents of a machine in a reusable format, while templating is the process of
capturing all of the system configuration to let us create VM in a repeatable way. That exact format of the reference
image will depend on the vendor. But often, the result is a file called a **disk image**. A disk image is a snapshot
of a virtual machine's disk at a given point in time.

### Extra Resources on Managing Vms in GCP

* [GCP - Linux Quickstart](https://cloud.google.com/compute/docs/quickstart-linux)

* [GCP -Create VM from Instance Template](https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template)

* [GCP SDK Docs](https://cloud.google.com/sdk/docs)

---

## Automatic Cloud Deployments


### Cloud Scale Deployments

---

### What is Orchestration?

---

### Cloud Infrastructure as Code

---

### Extra Resources on Cloud & GCP

* [Getting Started on GCP with Terraform](https://cloud.google.com/community/tutorials/getting-started-on-gcp-with-terraform)

* [Creating Groups of Unmanaged Instances](https://cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances)

* [Offical GCP Docs on Load Balancing](https://cloud.google.com/load-balancing/docs/https/)

* [GCP Load Balancer](https://geekflare.com/gcp-load-balancer/)

### Info on Hybrid Setups

* [VMware Terraform Template](https://blog.inkubate.io/create-a-centos-7-terraform-template-for-vmware-vsphere/)

* [GCP Reference Architecture - Terraform](https://www.terraform.io/docs/enterprise/before-installing/reference-architecture/gcp.html)

* [Terraform On-Premises Hybrid Cloud - Wayfair](https://www.hashicorp.com/resources/terraform-on-premises-hybri-cloud-wayfair)
