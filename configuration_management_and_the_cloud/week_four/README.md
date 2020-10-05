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

We now know how to get your service running in the cloud. Next, let's talk about how to keep it running

Most of the time when something stops working, it's because something changed. If we want our cloud service to be
stable, we might be tempted to avoid changes altogether. But change is a fact of cloud life. If we want to fix bugs
and improve features in our services, we have to make changes

But we can make changes in a controlled and safe way

This is called **Change Management**, and it's what lets us keep innovating while our services keep running

Step one in improving the safety of our changes, we have to make sure they're well-tested. This means running unit
tests and integration tests, and then running these tests whenever there's a change

A **Continuous Integration** or **CI** system will build and test our code every time there's a change

Ideally, the CI system runs even for changes that are being reviewed. That way you can catch problems before they're
merged into the main branch. You can use a common open source CI system like **Jenkins**, or if you use **GitHub**, you can use its **Travis CI Integration**

Many cloud providers also offer continuous integration as a service. Once the change has committed, the CI system
will build and test the resulting code

Now you can use **Continuous Deployment**, or **CD**, to automatically deploy the results of the build or *build
artifacts*. Continuous deployment lets you control the deployment with rules

> For example, we usually configure our CD system to deploy new builds only when all of the tests have passed
> successfully.

On top of that, we can configure our CD to push to different environments based on some rules

We mentioned that when pushing puppet changes, we should have a test environment *separate* from the production
environment. Having them separate lets us validate that changes work correctly before they affect users.

Here environment means everything needed to run the service. It includes the machines and networks used for running
the service, the deployed code, the configuration management, the application configurations, and the customer data.

* **Production**, usually shortened to **prod**, is the *real environment*, the ones users see and interact with

* **Test** environment needs to be similar enough to prod that we can use them to check our changes work correctly

You could have your CD system configured to push new changes to the test environment. You can then check that the
service is still working correctly there, and then manually tell your deployment system to push those same changes
to production

If the service is complex and there are a bunch of different developers making changes to it, you might set up
additional environments where the developers can test their changes in different stages before releasing them

> For example, you might have your CD system push all new changes to a *development* or *dev environment*, then have a
> separate environment called *pre-prod*, which only gets specific changes after approval. And only after a thorough
> testing, these changes get pushed to prod

Say you're trying to increase the efficiency of your surface by 20%, but you don't know if the change you made might
crash part of your system

You want to deploy it to one of those testing or development environments to make sure it works correctly before you
ship it to prod

___Remember, these environments need to be as similar to prod as possible___

They should be built and deployed in the same way. And while we don't want them to be breaking all the time, it's
normal for some changes to break dev or even pre-prod.

Sometimes you might want to experiment with a new service feature. You've tested the code, you know it works, but you
want to know if it's something that's going to work well for your users

When you have something that you want to test in production with real customers, you can experiment using **A/B
testing**

* **A/B testing** some requests are served using one set of code and configuration, *A*, and other requests are served
using a different set of of code and configuration, *B*
 
This is another place where a load balancer and instance groups can help us out. You can deploy one instance group
in your A configuration and a second instance group in your B configuration. 

Then by changing the configuration of the load balancer, you can direct different percentages of inbound requests to
those two configurations

If your A configuration is today's production configuration and your B configuration is something experimental, you
might want to start by only directing 1% of your requests to B. Then you can slowly ramp up the percentage that you
check out whether the B configuration performs better than A, or not

___Make sure you have basic monitoring so that it's easy to tell if A or B is performing better or worse___

If it's hard to identify the back-end responsible for serving A requests or B requests, then much of the value of A/B
testing is lost to A/B debugging

So what happens if all the precautions we took aren't enough and we break something in production?

Remember what we discussed earlier about post-mortems. 

___We learn from failure and we build the new knowledge into our change management___

* Ask yourself, what did I have to do to catch the problem? 

* Can I have one of my change management systems look for problems like that in the future?

* Can I add a test or a rule to my unit tests, my CI/CD system, or my service health checks to prevent this kind of failure in the future?

---

### Understanding Limitations

When writing software to run on the Cloud, it's important to keep in mind how the application will be deployed

* The software that's being created needs to be fault tolerant and capable of handling unexpected events. 

* Instances might be added or removed from the pool as needed and if an individual machine crashes

* The service needs to breeze along without introducing problems

* Not every problem results in a crash, sometimes we run into quotas or limits, meaning that you can only perform a
certain number of operations within a certain time period

> For example, when using Blob Storage there might be a limit of 1,000 writes to the same blob in a given seconds

If your service performs a lot of these operations routinely, it might get blocked by these limits

In that case- you'll need to see if you can change the way you're doing the operations, for example by grouping all
of the calls into one batch. Switching to a different service is sometimes an option too.

Some API calls used in Cloud services can be expensive to perform, so most Cloud providers will enforce rate limits on
these calls to prevent one service from overloading the whole system

> For example, there might be a rate limit of one call per second for an expensive API call

On top of that, there are also utilization limits, which cap the total amount of a certain resource that you can
provision

These quotas are there to help you avoid unintentionally allocating more resources than you wanted

> Imagine you've configured your service to use auto scaling and it suddenly receives a huge spike in traffic. This
> could mean a lot of new instances getting deployed which can cost a lot of money. For some of these limits, you can
> ask for a quota increase from the Cloud provider if you want additional capacity, and you can also set a smaller
> quota in the default to avoid overspending

This can be a great idea when you're running a service on a tight budget

If your service performance expensive operations routinely, you should make sure you understand the limitations of
the solution that you choose. A lot of platform as a service and infrastructure as a service offerings have costs
directly related to how much they're used

They also have usage quotas

If the service you've built suddenly becomes very popular, you can run out of quota or run out of budget. By imposing
a quota on an auto-scaling system, the system will grow to meet user demand until it reaches the configured limit

The trick here is to have good monitoring and alerting around behavior like this. If your system runs out of quota
but there's an increased demand for content, the system may have problems, degraded performance or worse yet
an outage

So you want to be notified as soon as it happens that you can decide whether to increase your quota or not

Finally, dependencies...

When your service depends on a Platform as a Service offering like a hosted database or CICD system, you're handing
the responsibility for maintenance and upgrades of that service off to your Cloud provider, fewer things to worry
about and maintain, but it also means that you don't always get to choose what version of that software you're using

You might find yourself on either side of the upgrade cycle, either wanting to stay at a version that's working well
for you or wanting the Cloud provider to hurry up and upgrade to resolve a bug that's affecting your service

Your Cloud provider has a strong incentive to keep its service software fairly up-to-date

Keeping software as a service solutions up to date ensures that customers aren't vulnerable to security flaws, that
bugs are promptly fixed and that new features get released early

At the same time, the Cloud provider has to move carefully and test changes to keep destruction of its service to a
minimum

They will communicate proactively about changes to the services that you use and in some cases, Cloud providers might
give you access to early versions of these services

> For example, you can set up a test environment for your service that uses the beta or pre-release version of a given
> software as a service solution, letting you test it before it impacts production

---

### Extra Reading on Cloud Providers

* [Understanding VM CPU and IP-Address Quotas](https://cloud.google.com/compute/quotas#understanding_vm_cpu_and_ip_address_quotas)

* [AWS Service Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)

* [Microsoft Azure Service Specific Limits](https://docs.microsoft.com/en-us/azure/azure-subscription-service-limits#service-specific-limits)
---

## Monitoring and Alerting


### Getting Started with Monitoring

Once we have our service running in the Cloud, we want to make sure that our service keeps running, and not just that
, we want to make sure it keeps behaving as expected, returning the right results quickly and reliably

The key to ensuring all of this, is to set up good monitoring and alerting rules

To understand how our service is performing, we need to monitor it

Monitoring lets us look into the history and current status of a system

How can we know what the status is? We'll check out a bunch of different metrics. These metrics tell us if the
service is behaving as expected or not. Well, some metrics are generic, like how much memory an instance is using.
Other metrics are specific to the service we want to monitor.

> Say your company is running a website and you want to check if it's working correctly. When a web server responds
> to an HTTP request, it starts by sending a response code, followed by the content of the response.

You might know, for example, that a **404** code means that the page wasn't found, or that a **500** response means
that there was an internal server error. In general, response codes in the **500** range, like **501**. or **503**,
tells us that something bad happened on the server while generating a response. Response codes in the 400 range means
there was a client-side problem in the request

When monitoring your web service, you want to check both the count of response codes and their types to know if
everything's okay
 
> If you're running an e-commerce site, you'll care about how many purchases were made successfully and how many
> failed to complete. 
>
> If you're running a mail server, you want to know how many emails were sent and how many got stuck and so on

You'll need to think about the service you want to monitor and figure out the metrics you'll need

Now, once we've decided what metrics we care about, what do we do with them?

We'll typically store them in the monitoring system. There's a bunch of different monitoring systems out there.

Some systems like:

* ___[AWS Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)___

* ___[Google Operations(Formerly Stackdriver)](https://cloud.google.com/products/operations)___

* ___[Microsoft Azure Monitor(Formerly Metrics)](https://docs.microsoft.com/en-us/azure/azure-monitor/)___

Are offered directly by Cloud Providers

Other systems like:

* ___[Prometheus](https://prometheus.io/)___

* ___[DataDog](https://www.datadoghq.com/)___

* ___[Nagios](https://www.nagios.org/)___

Can be used across vendors of Cloud services

There's two ways of getting our metrics into the monitoring system

* Some systems use a pull model, which means that the monitoring infrastructure periodically queries our service to
get the metrics

* Other monitoring systems use a push model, which means that our service needs to periodically connect to the system
to send the metrics

No matter how we get the metrics into the system, we can create dashboards based on the collected data

These dashboards show the progression of the metrics over time. We can look at the history of one specific metric to
compare the current state to how it was last week or last month. Or we can look at the progression of two or more
metrics together to check out how the change in one metrics effects another

> Imagine it's Monday morning and you notice that your service is receiving a lot less traffic than usual. You can
> look at the data from past weeks and see if you always get less traffic on Monday mornings or if there's something
> broken causing your service to be unresponsive. 
>
> Or if you see that in the past couple days, the memory used by your instances has been going up, you can check if
> this growth follows a similar increase in another metric, like the amount of requests received or the amount of
> data being transmitted

This can help you decide if there's been a memory leak that needs to be fixed or if it's just an expected
consequences of a growth in popularity

* **Pro tip** -  you only want to store the metrics that you care about, since storing all of these metrics in the
system takes space, and storage space costs money

When we collect metrics from inside a system, like how much storage space the service is currently using or how long
it takes to process a request, this is called **Whitebox Monitoring**

* **Whitebox Monitoring** checks the behavior of the system from the inside

We know the information we want to track, and we're in charge of making it possible to track

> For example, if we want to track how many queries we're making to the database, we might need to add a variable to
> count this

* **Blackbox Monitoring** checks the behavior of the system from the outside

This is typically done by making a request to the service and then checking that the actual response matches the
expected response

We can use this to do a very simple check to know if the service is up and to verify if the service is responding
from outside your network. Or we could use it to see how long it takes for a client in a different part of the world
to get a response from the system

---

### Getting Alerts When Things Go Wrong

We expect a lot from our modern IT services. We expect them to be up and running 24-7. We want to be able to get our
work done whenever and wherever

For that, we need our services to respond day or night, workday or holiday

But even if the services are running 24-7, System Administrators can't constantly be in front of their systems

Instead, we set up our services so that they work unattended and deal with problems when they happen

Now to do this, we need to detect those problems so that we can deal with them as quickly as possible. If you have
no automated way of raising an alert, you might only find out about the issue when you get a call from a frustrated
user telling you that your service is down

It's much better to create automation that checks the health of your system and notifies you when things don't behave
as expected. This can give you advance warning that something's wrong, sometimes even before users notice a problem
at all

So how do we do that?

The most basic approach is to run a job periodically that checks the health of the system and sends out an email if
the system isn't healthy

On a Linux system, we could do this using **cron**, which is the tool to schedule periodic jobs. 

We'd pair this with a simple Python script that checks the service and sends any necessary emails. This is an
extremely simplified version of an alerting system, but it shares the same principles as all alerting systems, no
matter how complex and advanced

___We want to periodically check the state of the service and raise alerts if there's a problem___

When you use a monitoring system like the ones we described in the last lesson, the metrics you collect represent the
state of your service. 

Instead of periodically running a script that connects to the service and checks if it's responding, you can
configure the system to periodically evaluate the metrics; and based on some conditions, decide if an alert should be
raised

Raising an alert signals that something is broken and a human needs to respond

>  For example, you can set up your system to raise alerts if the application is using more than 10 gigabytes of RAM
>, or if it's responding with too many 500 errors, or if the queue of requests waiting to get processed gets too long

___Not all alerts are equally urgent___

We typically divide useful alerts into two groups, those that need immediate attention and those that need attention
in the near future

If an alert doesn't need attention, then it shouldn't have been sent at all. It's just noise. If your web service is
responding with errors to 50% of the requests, you should look at what's going on right away

Even if this means waking up in the middle of the night to address whatever is wrong, you'll definitely want to fix
this kind of critical problem ASAP

On the other hand, if the issue is that the attached storage is 80% full, you need to figure out whether to
increase the disk size or maybe clean up some of the stored data. But this isn't super urgent, so don't let it get in
the way of a good night's sleep

Since these two types of alerts are different, we typically configure our systems to raise alerts in two different ways

Those that need immediate attention are called pages, which comes from a device called a pager. Before mobile phones
became popular, pagers were the device of choice for receiving urgent messages, and they're still used in some places
around the world

Nowadays, most people receive their pages in other forms like SMS, automated phone calls, emails, or through a
mobile app, but we still call them pages

On the flip side, the non-urgent alerts are usually configured to create bugs or tickets for an IT specialist to take
care of during their workday

They can also be configured to send email to specific mailing lists or send a message to a chat channel that will be
seen by the people maintaining the service

___All alerts should be actionable___


If you get a bug or a page and there's nothing for you to do, then the alert isn't actionable and it should be
changed or it shouldn't be there at all.

Otherwise, it's just noise

> Say you're trying to check if your services database back-end is responsive. If you do this by creating a query that
> returns all rows in a large table, your request might sometimes timeout and raise an alert

That would be a noisy alert, not really actionable. You'd need to tweak the query to make the check useful

> Say you run a cron job that copies files from one location to another every 10 minutes, you want to check that this
> job runs successfully. So you configure your system to alert you if the job fails. 
>
> After putting this in production, you realize there's a bunch of unimportant reasons that can cause this job to
> temporarily fail. Maybe the destination storage is too busy and so sometimes the job times out. Maybe the origin wa
> being rebooted right when the job started, so the job couldn't connect to it. 
>
> No matter why, whenever you go to check out what caused a job to fail, you discover that the following run had
> succeeded and there's nothing for you to do

You need to rethink the problem and tweak your alert

Since the task is running frequently, you don't care if it fails once or twice, you can change the system to only
raise the alert if the job fails three times in a row

That way when you get a bug, it means that it's failing consistently and you'll actually need to take action to fix it

You need to think about which metrics you care about. Configure your monitoring system to store them, then configure
your alerting system to raise alerts when things don't behave as expected. The flip side is that once you've set
your systems to raise actionable alerts when needed, you're going to have peace of mind.

If no alerts are firing, you know the service is working fine. This lets you concentrate on other tasks without
having to worry

To set up good alerts, we need to figure out which situations should page, which ones should create bugs, and which
ones we just don't care about 

These decisions aren't always easy and might need some discussion with the rest of your team. But it can help make
sure that you spend time only on things that actually matter

---

### Service-Level Objectives



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

