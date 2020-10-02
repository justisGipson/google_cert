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
  
   * ___Amazon Elastic Beanstalk___
  
   * ___Microsoft App Service___
  
   * ___Google App Engine___
   
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

And while some terms used by one provider might not exactly match the ones used by other providers, the concepts are
the same.

But usually Cloud service providers implement a console to manage the services. This console includes pointers to a
lot of different services that the providers offer

So it's a good idea to start just by familiarizing yourself with the platform before you try to do something with it.

This can mean, for example, looking at the available menus and options, and figuring out where the sections that let
you use infrastructure-as-a-service are located

No matter the exact menu entries, when you want to create a VM running in the Cloud, there are a bunch of parameters
that you need to set

These parameters are used by the Cloud infrastructure to spin up the machine with the settings that we want

  * ___Name of the instance___ - This name will later let you identify the instance if you want to connect to it
  , modify it, or even delete it.

  * ___Region and zone where the instance will be running___ - you'll generally want to choose a region that's clos
   to your users so that you provide better performance.

  * ___Machine type for the VM___ - Cloud providers allow users to configure the characteristics of their virtual
   machines to fit their needs. This means selecting how many processing units, or virtual CPUs, and how much memory
   the virtual machine will be allocated
   
You might be tempted to select the most powerful VM available, but of course the more powerful the VM, the more money
it will cost to run it

As a sysadmin, you may need to decide between costs and processing power to fit the needs of your organization.

When setting up instances like these, it's a good idea to start small and scale as needed

On top of the CPU and memory available, you'll also need to select the boot disk that the VM will use

Each virtual machine running in the Cloud has an associated disk that contains the operating system it runs and some
extra disk space. When you create the VM, you select both how much space you want to allocate for the virtual disk
and what operating system you want the machine to run

To create these resources, we can use the web interface or the command line interface. The web UI can be very useful
for quickly inspecting the parameters that we need to set

he UI will let us compare the different options available and even show us an estimation of how much money our
selected VM would cost per month. This is great for experimenting, but it doesn't scale well if we need to quickly
create a bunch of machines or if we want to automate the creation

In those cases, Cloud service providers also provides the command line interface, which allows for us to specify what
we want once, and then use the same parameters many times

__Using the command line interface lets us create, modify, and even delete virtual machines from our scripts.__

This is a great step towards automation, but it doesn't stop there. We can also automate the preparation of the
contents of those virtual machines

> Imagine spending an afternoon installing and configuring your new web server. You can do this on one machine, and
> the process is fairly straightforward. You install any necessary software, you modify any configuration settings,
> and then make sure that it's working correctly. But it would be hard to reproduce this exactly on another machine
> and impossible to do it on thousands of machines.

This is where **reference images** and **templating** come into play

**Reference images** store the contents of a machine in a reusable format, 

**templating** is the process of capturing all of the system configuration to let us create VM in a repeatable way
. 
That exact format of the reference image will depend on the vendor. But often, the result is a file called a **disk
image** 

A **disk image** is a snapshot of a virtual machine's disk at a given point in time

Good templating software lets you copy an entire virtual machine and use that copy to generate new ones

Depending on the software, the disk image might not be an _exact_ copy of the original machine because some machine
data changes, like the hostname and IP address. But it will have the data that we need to make it reusable on lots
of virtual machines

This can be super helpful if we want to build a cluster of 10,000 machines which all have identical software

---

### Creating a New VM Using the GCP Web UI

####[Google Cloud Platform Console](https://console.cloud.google.com)

Here, the first step is to create a project so that our VMs are associated to that project

`First Cloud Steps`

Takes a couple of seconds to create the project

Now that we have a project, our dashboard has a lot more info. Next, we want to go to the menu entry that lets us
create virtual machines. To do that, we'll go into the Compute Engine menu, and select the VM instances entry.

This screen is pretty empty because we don't have any VMs yet. We can create a VM by pressing the Create button.

Here we're showing the many different options that we can set for this VM that we're creating. We can set the name
, the region and zone, the machine type, the boot disk, and so on.

`linux-instance`

Now it's time to select the region and zone. If we click on the region drop-down, we can see all the regions that are
currently available to create new VMs.

For this example, we'll just keep the default regions.

* If you're deploying a service, you should select something that's close to your users

Example below is to create up the identical VM that was created via the GCP Web UI from the steps above
```bash

gcloud beta compute --project=first-cloud-steps-291215 instances create linux-machine-instance --zone=us-central1-a --machine-type=e2-medium --subnet=default --network-tier=PREMIUM --maintenance-policy=MIGRATE --service-account=97071662855-compute@developer.gserviceaccount.com --scopes=https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write,https://www.googleapis.com/auth/servicecontrol,https://www.googleapis.com/auth/service.management.readonly,https://www.googleapis.com/auth/trace.append --tags=http-server --image=ubuntu-1804-bionic-v20200923 --image-project=ubuntu-os-cloud --boot-disk-size=10GB --boot-disk-type=pd-standard --boot-disk-device-name=linux-machine-instance --no-shielded-secure-boot --shielded-vtpm --shielded-integrity-monitoring --reservation-affinity=any

gcloud compute --project=first-cloud-steps-291215 firewall-rules create default-allow-http --direction=INGRESS --priority=1000 --network=default --action=ALLOW --rules=tcp:80 --source-ranges=0.0.0.0/0 --target-tags=http-server

```

___# TODO - grab info for walk through and make notes out of it___

---

### Extra Resources on Managing Vms in GCP

* [GCP - Linux Quickstart](https://cloud.google.com/compute/docs/quickstart-linux)

* [GCP -Create VM from Instance Template](https://cloud.google.com/compute/docs/instances/create-vm-from-instance-template)

* [GCP SDK Docs](https://cloud.google.com/sdk/docs)

---

## Automatic Cloud Deployments


### Cloud Scale Deployments

The biggest advantage of using Cloud services is how easily we can scale our services up and down

Now, to make the most out of this advantage, we need to do some preparation

We'll set up our services so that we can easily increase their capacity by adding more nodes to the pool

These nodes could be virtual machines, containers, or even specific applications providing one service. Whenever we
have a service with a bunch of different instances serving the same purpose, we'll use a **load balancer**

A **load balancer** ensures that each node receives a balanced number of requests

When a request comes in, the load balancer picks a node to serve the response. There's a bunch of different
strategies load balancer uses to select the node

The simplest one is just to give each node one request called round robin

More complex strategies include always selecting the same node for requests coming from the same origin, selecting
the node that's closest to the requester, and selecting the one with the least current load

Instance groups like these are usually configured to spin up more nodes when there's more demand, and to shut some
nodes down when the demand falls

This capability is called **autoscaling**

* **Autoscaling** allows the service to increase or reduce capacity as needed while the service owner only pays for
the cost of the machines that are in use at any given time

Since some nodes will shut down when demand is lower, their local disks will also disappear and should be considered
ephemeral or short-lived

If you need data persistence, you'll have to create separate storage resources to hold that data and connect that
storage to the nodes. That's why the services that we run in the Cloud are usually connected to a database which is
also running in the Cloud

This database will also be served by multiple nodes behind a load balancer, but this is typically managed by the Cloud
provider using the platform as a service model

> To check out how this works in practice, let's look at an example of a web application with a lot of users. 

When you connect to a site through the Internet, your web browser first retrieves an IP address for the website that
you want to visit. This IP address identifies a specific computer, the entry point for the sites

Commonly there will be a bunch of different entry points for a single website. This allows the service to stay up
even if one of them fails

On top of that, it's possible to select an entry point that's closer to the user to reduce latency. In a small-scale
application, this entry point could be the web server that serves the pages, and that would be it. 

For large applications where speed and availability matter, there will be a couple of layers in between the entry
point and the actual web service

The first layer will be a pool of web caching servers with a load balancer to distribute the requests among them. 

One of the most popular applications for this caching is called **Varnish**, but of course it's not the only one. The
**Nginx** web server and software also includes this caching functionality

There's a bunch of providers that do web caching as a service like Cloudflare and Fastly. No matter the software used
, the result is basically the same

When a request is made, the caching servers first check if the content is already stored in their memory. If it's
there, they respond with the contents, if it's not, they ask their configured backend for the content and then store
it so that it's present for future requests

This configured backend is the actual web service that generates the webpages for the site, and it will also normally
be a pool of nodes running under a load balancer

To get any necessary data, this service will connect to a database. But because getting data from a database can be
slow, there's usually an extra layer of caching, specific for the database contents. The most popular application for
this level of caching are **Memcached** and **Redis**.

Once you've done your homework and prepared your setup, you can rely on the capabilities offered by the Cloud
provider to automatically scale the system up and down as necessary. The infrastructure will take care of adding and
removing instances, distributing the load, making sure that each geographical region has the right capacity, and
bunch more things

---

### What is Orchestration?

___Automation is the process of replacing a manual step with one that happens automatically___

We've mentioned a few ways that let us automate the creation of Cloud instances:

* We can use templating to create new virtual machines

* We can run a command line tool that automatically creates new instances for us

* We can choose to enable auto-scaling and let the infrastructure tools take care of that depending on the demand

But all of this automatic creation of new instances needs to be coordinated so that the instances correctly interact
with each other and that's where **orchestration** comes into play

* **Orchestration** is the automated configuration and coordination of complex IT systems and services

___In other words, orchestration means automating a lot of different things that need to talk to each other___

This will always include a lot of different automated tasks and will generally involve configuring a bunch of
different systems

> Now, say you wanted to deploy a new copy of the system in a separate data center where you have no instances yet
>, you'll need to also automate the whole configuration of the system, the different instance types involved, how
> will each instance finesse the others, what the internal network looks like, and so on

So how does this work?

The key here is that the configuration of the overall system needs to be automatically repeatable

There's a bunch of different tools that we can use to do that. These tools typically don't communicate with the Cloud
systems through the web interface or the command line

They normally use an **Application Programming Interface** or **API** that lets us interact with the Cloud
infrastructure directly from our scripts

In the case of Cloud provider APIs, they typically let you handle the configuration that you want to sit directly
from your scripts or programs without having to call a separate command

This combines the power of programming with all of the available Cloud resources. The APIs offered by the Cloud
providers let us perform all the tasks that we mentioned earlier like creating, modifying, and deleting instances
and also deploying complex configurations for how these instances will talk to each other

All of these actions can also be completed through the web interface or the command line. But doing them from our
programs gives us extra flexibility which can be key when automating complex setups

> Say you wanted to deploy a system that combines some services running on a Cloud provider and some services running
> on-premise, this is known as a **Hybrid Cloud** setup, or only part of the services are in the Cloud

The setup is super common in the industry right now

Orchestration tools can be a pretty useful tool to make sure that both the on-premise services and the Cloud services
know how to talk to each other and are configured with the right settings

To ensure the service is running smoothly, we should set up a monitoring and alerting 

This lets us detect and correct any problems with our service before users even notice. This is a critical piece of
infrastructure but setting it up correctly can take quite some time

By using orchestration tools, we can automate the configuration of any monitoring rules that we need to set, which
metrics we want to look for, when we want to be alerted, and so on, and automatically apply these to a complete
deployment no matter which datacenter the services are running in

---

### Cloud Infrastructure as Code

We've talked about how we need to orchestrate complex Cloud setups

This includes handling a bunch of different nodes with different workloads, managing the complexity of deploying a
hybrid setup, or modifying deployments across several Data centers.

We also talked about **Infrastructure as Code**, and we called out that storing our infrastructure in a code like
format, lets us create repeatable infrastructure, and that using **Version Control** for the storage, means that we ca
keep a history of what we've done and easily rollback mistakes 

These principles also apply to Cloud infrastructure

The way we store it might be a little different depending on the tools that we use, but we'll still be storing this
configuration in a code like format using Version control to keep track of the changes

This lets us manage large-scale solutions with a small team. We can very quickly have an idea of what the deployment
looks like, by looking at the configuration. We can try new things out and roll back if anything goes wrong. We can
look at the history of changes to figure out why a specific change was made, and much more

Most Cloud providers offer their own tool for managing resources as code

* ___Amazon Cloud Formation___

* ___Google Cloud Deployment Manager___

* ___Microsoft Azure Resource Manager___

* ___OpenStack Heat Orchestration Templates___

These tools are specific to the Cloud provider, which means it can be complex and cumbersome to move to a different
provider or combine a Cloud deployment with an on-premise deployments

An option that's becoming really popular in the Orchestration field, is called **Terraform**

Similar to Puppet, Terraform uses its own Domain-specific language which lets us specify what we want our Cloud
infrastructure to look like

The cool thing about Terraform is that it knows how to interact with a lot of different Cloud providers and
automation vendors. So you can write your Terraform rules to deploy something on one Cloud provider, and then use
very similar rules to deploy the service to a different Cloud provider

Terraform uses each Cloud provider's API to accomplish this. This keeps you from having to learn a new API when
moving to a different Cloud provider, and lets you focus on the infrastructure design

We've seen how we can have a puppet rule that specifies that a computer should install a given package
, and that the local puppet agent analyzes the computer and decides which installation mechanism to use depending on
the operating system, the specific Linux distro and so on

A similar thing happens with Terraform. The rules that define the resources like the VMs or containers to use, will
use specific values related to the Cloud provider like selecting which machine type to use or in what region to
deploy it.

But a lot of the overall configuration is independent of the provider, and can be reused if we decide to move our
configuration to a different provider or we want to use a hybrid setup

Of course Terraform isn't the only option

Puppet itself also ships with a bunch of plug-ins that can be used to interact with the different Cloud providers to
create and modify the desired Cloud infrastructure

On the contents of the nodes or instances managed by the Orchestration tools - 

When dealing with nodes in the Cloud, there are basically two options:

* They're long-lived and their contents need to be periodically updated

* They are short-lived and updates are made by deleting the old instances and deploying new ones

Long-lived instances are typically servers that are not expected to go away. Things like your company's internal mail
server or internal document sharing servers, will manage these instances using a configuration management system
like Puppet, which can deploy any necessary changes to the machines while they're running. This keeps them updated
to the latest state

Short-lived instances come and go very quickly. For these cases, it makes less sense to apply changes while they're
running. Instead, we normally apply the configuration that we want the instances to have when they start, and we
deploy any future changes by replacing the instances with new ones. We can still use Puppet for the initial setup
but we don't need to run the agent periodically, only at the start

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

---

### Wrap-up

We've learned how to use the different Cloud resources available to us

We've gone through a bunch of different concepts like software or infrastructure-as-a-service, public or hybrid
clouds, up-scaling and down-scaling, and a lot more

We've also demonstrated how to deploy single virtual machines and then turn them into a customized VM template

Creating a single VM can be useful for small to medium-sized organizations with lower technical requirements. But as
the technical requirements for the organization grows, it's often necessary to deploy more and larger Cloud solutions

This is where using the template to create large system clusters becomes very handy. Using reference images and
templating lets us clone a VM 100, 1,000, or more times, and this makes scaling our Cloud deployments super easy

We checked out a bunch of different ways to interact with the platform

We've seen how we can use both the web interface and the command line tool to create virtual machines in the Cloud

Using these tools we can control which machines are online or offline, modify their configuration, and a bunch of
other things. At a small or medium scale, using these tools can be really effective. At a larger scale, we have to
automate these deployments even further and that's where orchestration comes into play

Tools like Terraform let us define our Cloud infrastructure as code, allowing us to have a lot of control over how
the infrastructure is managed, how the changes are applied, and so on

This lets us combine the power of using infrastructure as code with the flexibility of using Cloud resources.

---
