## Managing Cloud Instance at Scale

In this module, you’ll learn all about storing data in the cloud. You’ll rundown the different types of storage
available, like-

* block storage 

* object storage

* and how they differ. 

You’ll explore load balancing further and dive into some load balancing techniques, like-

* **round-robin**

* **DNS**

* **sticky sessions** 

Next, you’ll dive into change management, including the different ways to test your changes and how to push
them. You’ll explore different testing methods, like-

* **unit tests**

* **integration tests**

You’ll also cover **continuous integration**, the use of **continuous deployment**, and how to apply **A/B testing**.
 
Next up, you’ll look at some errors you might encounter along the way, like **quotas** or **limits**, and how best to
avoid or prepare for these. 

In the next lesson, you’ll get an understanding of monitoring and altering, and review some
systems that offer it. You’ll then dive into the concept of **SLA**’s and how to set achievable ones. 

Next, you’ll look at basic monitoring in GCP, and create altering policies, set up conditions, and choose aggregators
to manage the data. 

Finally, will explore troubleshooting and debugging our systems. You’ll learn how to troubleshoot and debug remotely,
understand. Techniques for how to identify where the failure is coming from, and how to recover from a failure when
it strikes.

### Key Concepts

* Understand and explain the different types of storage available

* Explain the difference between round robin DNS and sticky sessions

* List the different types of integration testing that are available

* Understand and explain the concept of SLAs

* Troubleshoot and debug a system without being physically present

* Understand what a rollback is and how they can help in a system failure

* Understand how primary and secondary instances can help in a disaster recovery situation

---

## Building Software for the Cloud


### Storing Data in the Cloud

Almost all IT systems need to store some data. Sometimes, it's a lot of data, sometimes, it's only bits and pieces of
information. Cloud providers give us a lot of storage options

Picking the right solution for data storage will depend on what service you're building

You'll need to consider a bunch of factors, like;

* How much data you want to store

* What kind of data that is

* What geographical locations you'll be using it in

* Whether you're mostly writing or reading the data

* How often the data changes

* How big your budget is

When choosing a storage solution in the Cloud, you might opt to go with the traditional storage technologies, like
**block storage**, or you can choose newer technologies, like **object** or **blob storage**

When we create a VM running in the Cloud, it has a local disk attached to it

These local disks are an example of block storage

This type of storage closely resembles the physical storage that you have on physical machines using physical hard
drives. Block storage in the Cloud acts almost exactly like a hard drive. The operating system of the virtual
machine will create and manage a file system on top of the block storage just as if it were a physical drive

There's a pretty cool difference though. These are virtual disks, so we can easily move the data around

> For example, we can migrate the information on the disk to a different location, attach the same disk image to other
> machines, or create snapshots of the current state. All of this without having to ship a physical device from place
> to place

Our block storage can be either **persistent** or **ephemeral**

* **Persistent storage** is used for instances that are long lived, and need to keep data across reboots and upgrades

* **Ephemeral storage** is used for instances that are only temporary, and only need to keep local data while they're
running.

Ephemeral storage is great for temporary files that your service needs to create while it's running, but you don't
need to keep

This type of storage is especially common when using containers, but it can also be useful when dealing with virtual
machines that only need to store data while they're running

In typical Cloud setups, each VM has one or more disks attached to the machine. The data on these disks is managed by
the OS and can't be easily shared with other VMs

If you're looking to share data across instances, you might want to look into some shared file system solutions, that
Cloud providers offer using the platform as a service model.

When using these solutions, the data can be accessed through network file system protocols like NFS or CIFS. This
lets you connect many different instances or containers to the same file system with no programming required.

**Block storage** and shared file systems work fine when you're managing servers that need to access files. But if
you're trying to deploy a Cloud app that needs to store application data, you'll probably need to look into other
solutions like **Object Storage**, which is also known as **Blob Storage**

Object storage lets you place and retrieve objects in a storage bucket. These objects are just generic files like
photos or cat videos, encoded and stored on disk as binary data. These files are commonly called blobs, which comes
from **binary large object**

These blobs are stored in locations known as **buckets**

Everything that you put into a storage bucket has a unique name. There's no file system. You place an object into
storage with a name, and if you want that object back, you simply ask for it by name

To interact with an object store, you need to use an API or special utilities that can interact with the specific
object store that you're using. On top of this, most Cloud providers offer databases as a service

These come in two basic flavors, **SQL** and **NoSQL**.

* **SQL Databases**, also known as **Relational Databases**, use the traditional database format and query language.
Data is stored in tables with columns and rows that can be indexed, and we retrieve the data by writing SQL queries.
A lot of existing applications already use this model, so it's typically chosen when migrating an existing
application to the Cloud.

* **NoSQL Databases** offer a lot of advantages related to scale. They're designed to be distributed across tons of
machines and are super fast when retrieving results. But instead of a unified query language, we need to use a
specific API provided by the database. This means that we might need to rewrite the portion of the application that
accesses the DB

When deciding how to store your data, you'll also have to choose a **storage class**. Cloud providers typically offer
different classes of storage at different prices. Variables that could affect the monthly price could be:

* Performance

* Availability

* How often the data is accessed

The performance of a storage solution is influenced by a number of factors, including **throughput**, **IOPS**, and
**latency**

**Throughput** is the amount of data that you can read and write in a given amount of time. The throughput for reading
and writing can be pretty different.

> For example, you could have a throughput of one gigabyte per second for reading and 100 megabytes per second for
> writing

* **IOPS** or **Input/Output Operations Per Second** measures how many reads or writes you can do in one second, no
matter how much data you're accessing.

Each read or write operation has some overhead. So there's a limit on how many you can do in a given second

* **Latency** is the amount of time it takes to complete a read or write operation

This will take into account the impact of IOPS, throughput and the particulars of the specific service

* **Read Latency** is sometimes reported as the time it takes a storage system to start delivering data after a read
request has been made, also known as **Time To First Byte** or **TTFB**

* **Write Latency** is typically measured as the amount of time it takes for a write operation to complete

When choosing the storage class to use, you might come across terms like **hot** and **cold**

* **Hot Data** is accessed frequently and stored in hot storage

* **Cold Data** is accessed infrequently, and stored in cold storage

These two storage types have different performance characteristics

> For example, hot storage back ends are usually built using solid state disks, which are generally faster than the
> traditional spinning hard disks.

So how do you choose between one and the other?

Say you want to keep all the data you're service produces for five years, but you don't expect to regularly access
data older than one year. You might choose to keep the last one year of data in hot storage so you have fast access
to it, and after a year, you can move your data to cold storage where you can still get to it, but it will be slower
and possibly costs more to access

---

### Load Balancing

We've seen a bunch of different reasons why we might want more than one machine or container running our service

> For example, we might want to horizontally scale our service to handle more work, distribute instances
> geographically to get closer to our users. Or have backup instances to keep the service running if one or more of
> the instances fail

No matter the reason, we use orchestration tools and techniques to make sure that the instances are repeatable. And
once we've set up replicated machines, we'll want to distribute the requests across instances

This is where load balancing comes into play

A pretty common load balancing technique is **Round Robin DNS**. Round robin is a really common method for
distributing tasks

If we want to translate a URL like my service.example.com into an IP address, we use the DNS protocol or domain name
system

In the simplest configuration, the URL always gets translated into exactly the same IP address. But when we configure
our DNS to use round robin, it'll give each client asking for the translation a group of IP addresses in a different
order. The clients will then pick one of the addresses to try to reach the service. If an attempt fails, the client
will jump to another address on the list

This load balancing method is super easy to set up. You just need to make sure that the IPs of all machines in the
pool are configured in your DNS server, but it has some limitations

First, you can't control which addresses get picked by the clients. Even if a server is overloaded, you can't stop
the clients from reaching out to it

Secondly, DNS records are cached by the clients and other servers. So if you need to change the list of addresses for
the instances, you'll have to wait until all of the DNS records that were cached by the clients expire

To have more control over how the load's distributed and to make faster changes, we can set up a server as a
dedicated load balancer

This is a machine that acts as a proxy between the clients and the servers. It receives the requests and based on the
rules that we provide, it directs them to the selected back-end server

Load balances can be super simple or super complex depending on the service needs

Say your service needs to keep track of the actions that a user has taken up till now. In this case, you'll want your
load balancer to use **sticky sessions**

* **Sticky sessions** means all requests from the same client always go to the same back end server

This can be really useful for services than need it but can also cause headaches when migrating or maintaining your
service. So you need to use it only if you really need it

Another cool feature of load balancers is that you can configure them to check the health of the backend servers

Typically, we do this by making a simple query to the servers and checking that the reply matches the expected reply.
If a back-end server is unhealthy, the load balancer will stop sending new requests to it to keep only healthy
servers in the pool.

A cool feature of cloud infrastructure is how easily we can add or remove machines from a pool of servers providing a
service. If we have a load balancer controlling the load of the machines, adding a new machine to the pool is as
easy as creating the instance, and then letting the load balancer know that it can now route traffic to it

We can do this by manually creating and adding the instance or when our services under heavy load, we can just let
the auto-scaling feature do it

Okay, so imagine that you've built out your service with load balancers and you're receiving requests from all over
the world

How do you make sure that clients connect to the servers that are closest to them? You can use **Geo DNS** and
**geoip**

These are DNS configurations that will direct your clients to the closest geographical load balancer. The mechanism
used to route the traffic relies on how the DNS servers respond to requests

> For example, from machines hosted in North America, a DNS server in North America might be configured to respond
> with the IPs in, you guessed it, North America

It can be tricky to set this up on your own but most Cloud providers offer it as part of their services making it
much easier to have a geographically distributed service

Let's take this one step further. There are some providers dedicated to bringing the contents of your services as
close to the user as possible. These are the **Content Delivery Networks** or **CDN**s. They make up a network of
physical hosts that are geographically located as close to the end-user as possible.

This means that CDN servers are often in the same data center as the users Internet service provider

* **CDN**s work by caching content super close to the user. When a user requests a video, it's stored in
the closest CDN server. That way, when a second user in the same region requests the same video, it's already
cached in a server that's pretty close and it can be downloaded extra fast

---

### Change Management



---

### Understanding Limitations



---

### Extra Reading on Cloud Providers

* [Understanding VM CPU and IP-Address Quotas](https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas)

* [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)

* [Microsoft Azure Service Specific Limits](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits)
---

## Monitoring and Alerting


### Getting Started with Monitoring



---

### Getting Alerts When Things Go Wrong



---

### Basic Monitoring in GCP



---

### Extra Resources on Monitoring and Alerting

* [DataDog - Monitoring 101: Collecting Data](https://www.datadoghq.com/blog/monitoring-101-collecting-data/)

* [DigitalOcean - Intro to Metrics Monitoring and Alerting](https://www.digitalocean.com/community/tutorials/an-introduction-to-metrics-monitoring-and-alerting)

* [Wikipedia - High Availability](https://en.wikipedia.org/wiki/High_availability)

* [Google SRE Books](https://landing.google.com/sre/books/)

---

## Troubleshooting and Debugging


### What To Do When You Can't Physically Be There

---

### Identifying Where The Failure is Coming From

---

### Recovering From Failure

---

### Extra Resources on Debugging in The Cloud

* [Google - Troubleshooting Instances](https://cloud.google.com/compute/docs/troubleshooting/troubleshooting-instances)

* [Microsoft Azure VM Troubleshooting](https://docs.microsoft.com/en-us/azure/virtual-machines/troubleshooting/)

* [AWS - EC2 Instance Troubleshooting](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-troubleshoot.html)

---

