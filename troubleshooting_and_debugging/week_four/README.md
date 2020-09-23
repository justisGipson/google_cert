# Troubleshooting and Debugging Techniques - Week 4

## Managing Computer Resources


### Memory Leaks and How to Prevent Them

Most applications need to store data in memory to run successfully.

Processes interact with the OS to request chunks of memory, and then release them when they're no longer needed

When writing programs in languages like C, or C++, the programmer is in charge of deciding how much memory to
request, and when to give it back. Since we're human, we might sometimes forget to free memory that isn't in use
anymore, this is what we call a **Memory leak**

* **Memory Leak** is a chunk of memory that's no longer needed is not released.

If the memory leak is small, we might not even notice it, and it probably won't cause any problems. But, when the
memory that's leaked becomes larger and larger over time, it can cause the whole system to start misbehaving

When a program uses a lot of RAM, other programs will need to be swapped out and everything will run slowly. If the
program uses all of the available memory, then no processes will be able to request more memory, and things will
start failing in weird ways

When this happens, the OS might terminate processes to free up some of the memory, causing unrelated programs to crash

**Python**, **Java**, and **Go** will manage memory for us

To understand how this works, let's look into what these languages do

First, they request the necessary memory when we create variables, and then they run a tool called Garbage collector
, that's in charge of freeing the memory that's no longer in use

To detect when that's the case, the garbage collector looks at the variables in use and the memory assigned to them
and then checks if there any portions of the memory that aren't being referenced by any variables.

When our code keeps variables pointing to the data in memory, like a variable in the code itself, or an element in a
list or a dictionary, the garbage collector won't release that memory

Even when the language takes care of requesting and releasing the memory for us, we could still see the same effects
of a memory leak

The OS will normally release any memory assigned to a process once the process finishes. So memory leaks are less of
an issue for programs that are short lived, but can become especially problematic for processes that keep running in
the background

Even worse than these, are memory leaks caused by a device driver, or the OS itself. In these cases, only a full
restart of the system releases the memory

What can we do if we suspect a program has a memory leak? We can use a **memory profiler** to figure out how the
memory is being used.

As with debuggers will have to use the right profiler for the language of the application.

* For profiling C and C plus plus programs, we'll use **Valgrind**

* For profiling a Python, there are bunch of different tools that are disposal, depending on what exactly we want to
profile

We can be as detailed as profiling the memory usage of a single function, or as big picture as monitoring the total
memory consumption over time.

Using profilers, we can see what structures are using the most memory at one in time or take snapshots at different
points in time and compare them. The goal of these tools is to help us identify which information we're keeping in
memory that we don't actually need

It's important that we measure the use of memory first before we try to change anything, otherwise we might be
optimizing the wrong piece of code. Sometimes we need to keep data in memory, and that's fine, but you want to make
sure that you're only keeping the data that you actually need, and that you've let go of anything you won't be
using, that way the garbage collector can give that memory back to the OS

---

### Managing Disk Space

Another resource that might need our attention is the disk usage of our computer.

Programs may need disk space for lots of different reasons. Installed binaries and libraries, data stored by
the applications, cached information, logs, temporary files or even backups

If our computers running out of space, it's possible that we're trying to store too much data in too little space

Maybe we have too many applications installed, or we're trying to store too many large files in the drive

It's also possible that programs are misusing the space allotted to them, like by keeping temporary files or caching
information that doesn't get cleaned up quickly enough or at all

It's common for the overall performance of the system to decrease as the available disk space gets smaller

Data starts getting fragmented across the disk, and operations become slower

When a hard drive is full, programs may suddenly crash, while trying to write something into disk and finding out
that they can't. A full hard drive might even lead to data loss, as some programs might truncate a file before
writing an updated version of it, and then fail to write the new content, losing all the data that was stored in it
before.

If it gets to this point, we'll probably see some error, like no space left on device when running our applications
or in the logs

So what do you do if a computer runs out of disk space?

*  If it's a user machine, it might be easily fixed by uninstalling applications that aren't used, or cleaning up old data that isn't needed anymore

* But if it's a server, you might need to look more closely at what's going on

Is the issue that you need to add an extra drive to the server to have more available space, or is it that some
application is misbehaving and filling the disk with useless data?

To figure this out, you want to look at how the space is being used and what directories are taking up the most
space, then drill down until you find out whether large chunks of space are taken by valid information or by file
that should be purged

For example, on a database server, it's expected that the bulk of the disc space is going to be used by the data
stored in the database. A mail server, it's going to be the mailboxes of the users of that service. But if you find
that most of the data is stored in logs or in temporary files, something has gone wrong

One common pattern of misbehavior is a program that keeps logging error messages to the system log over and over
. This can happen for lots of different reasons. For example, the OS might keep trying to start a program that fails
because of a configuration problem. This will generate a new log entry with every retry, and can take up a lot of
space if there are several retries per second, or it could be that the server has a lot of activity and the logs
are real

In that case, you might want to look into tweaking the configuration of the tools that rotate the logs more
frequently, to make sure that you're keeping only what you need

In other cases, the disk might get full due to a program generating large temporary files, and then failing to clean
those up.

For example, an application might clean up temporary files when shutting down cleanly, but leave them behind if it
crashes. Or it could simply be a programming error of creating temporary files and never cleaning them up

In a case like this, you'll ideally have some housekeeping to fix the program, and delete those files correctly. But
if that's not possible, you might need to write your own script that gets rid of them

There are all kinds of other reasons why the disk may be getting too full. Just remember that whenever this happens
, your process will remain the same. You'll need to spend some time looking into what's using the disk. Check to see
if it's expected or an anomaly, figure out how to solve it, and most important of all, how to prevent it from
happening again

---

### Network Saturation

The two most important factors that determine the time it takes to get the data over the network are the latency and
the bandwidth of the connection.

* **Latency** is the delay between sending a byte of data from one point and receiving it on the other. 

This value is directly affected by the physical distance between the two points and how many intermediate devices
there are between them.

* **Bandwidth** is how much data can be sent or received in a second. 

This is effectively the data capacity of the connection. Internet connections are usually sold by the amount of
bandwidth the customer will see. But it's important to know that the usable bandwidth to transmit data to and from a
network service will be determined by the available bandwidth at each endpoint and every hop between them.

To understand how latency and bandwidth interact, think about what happens when you try to visit a website over the
Internet. 

If the web server is hosted somewhere across the ocean, the latency might be a 100 milliseconds or so. That's the
time it takes for your request to reach the server. 

The server will then generate a response and send it back to you. The first bytes of the response will again take a
100 milliseconds to zap across the pond to your computer. 

Once the response is on its way, the time it takes for the rest of the data to arrive is determined by the bandwidth
. If the available bandwidth between the two points is 10 megabits per second, you'll be able to receive 1.25
megabytes every second

So for a website of about one megabyte of content, that large initial latency will be noticeable, since it's an extra
20 percent on top of the total time to download it. But if the content is 10 megabytes or more, the initial latency
will be less than five percent of the total time to download it

If you're transmitting a lot of small pieces of data, you care more about latency than bandwidth. In this case, you
want to make sure that the server is as close as possible to the users of the service, aiming for a latency of less
than 50 milliseconds if possible, and up to a 100 milliseconds in the worst-case.

On the flip side, if you're transmitting large chunks of data, you care more about the bandwidth than the latency. In
this case, you want to have as much bandwidth available as possible regardless of where the server is hosted

Computers can transmit data to and from many different points of the Internet at the same time, but all those
separate connections share the same bandwidth. Each connection will get a portion of the bandwidth, but the split
isn't necessarily even.

If one connection is transmitting a lot of data, there may be no bandwidth left for the other connections

When these traffic jams happen, the latency can increase a lot because packets might get held back until there's
enough bandwidth to send them

You can check out which processes are using the network connection by running a program like **iftop**. This shows
how much data each active connection is sending over the network

__No matter how much bandwidth you have, it's a limited resource.__

If some applications are using so much bandwidth that others can't transmit anymore data, it's possible to restrict
how much each connection takes by using **traffic shaping**. This is a way of marking the data packets sent over the
network with different priorities

To avoid having huge chunks of data use all the bandwidth, by prioritizing accordingly, processes that send and
receive small packets can keep working fine, while processes that need the most bandwidth can use the rest. There's
also a limit to how many network connections can be established on a single computer

---

### Dealing with Memory Leaks

There's a ton of reasons why an application may request a lot of memory. Sometimes, it's what we need for the program
to complete it's task. Sometimes, it's caused by a part of the software misbehaving

* **Scroll Buffer** Feature that let's us scroll up and see the things we've executed and their output

Contents of the buffer are kept in memory. So if it's really long and manage to fill it, the machine will run out of
memory. 

* **top**: shows the processes currently using the most CPU time (press "q" to quit)

There's a bunch of different columns with data about each process.

* **RES** is the dynamic memory that's preserved for a specific process

* **SHR** is the memory that's shared across processes

* **VIRT** is the virtual memory allocated for each process
    
    - This includes; process specific memory, shared memory, and other shared resources that are stored on disk but
     maps into the memory of the process
    
It's usually fine for a process to have a high value in the **VIRT** column. The one that usually indicates a problem
is the **RES** column

It can usually take a long while until we notice that a program is taking more memory than it should, and it might be
hard to tell the difference between memory that's actually needed and memory that's being wasted

But looking at the output of **top** and comparing it to what it used to be a while back is usually how and
investigation into a memory leak starts

* **Decorator** Used in Python to add extra behavior to functions without having to modify the code.  

---

### Extra Resources About Managing Resources

* [Python Concurrency](https://realpython.com/python-concurrency/)

* [Threaded Asynchronous Magic and How to Wield It](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)

* [How To Profile Memory Usage In Python](https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python)

* [Troubleshooting Network Problems](https://www.linuxjournal.com/content/troubleshooting-network-problems)

___

## Managing Our Time


### Getting to the Important tasks

We've discussed how to make better use of the resources available on our computers and systems, like the CPU, the
memory, the disk, the network, and so on

But, there's another resource that's even more valuable in our day to day, our **time**

As humans, we want to make sure that we spend our time doing meaningful activities, like work that we enjoy, and
earning the satisfaction of a job well done

When working, we need to optimize the time we spend to bring the most value to the company. Finding the right balance
is hard, but that's what we're here for. From updated calendars, to social media detoxes, there's lots of different
ways to optimize our time.

One that's super effective when working in IT is the **Eisenhower Decision Matrix**

When using this method, we split tasks into two different categories: **urgent** and **important**.

There are tasks that are important and urgent. These need to be done right away

Some tasks are important, but not urgent, so they need to get done at some point even if it takes a while to complete
them

Other tasks might seem urgent, but aren't really important. A lot of the interruptions that we need to deal with are
in this category; Answering email, phone calls, texts, or instant messages feel like something that we need to do
right away. But most of the time are not really the best use of our time.

Finally, there's a whole category of tasks that are neither important nor urgent. These are distractions and time
wasters, they shouldn't be done at all.
    - meetings where nothing useful is being discussed, email threads that lead to nowhere, office gossip, and any
     other tasks that eat up our time without giving anything valuable in return
     
In general, to make the most of our time, we need to make sure that we're spending the majority of it on tasks that
are important. Of course we'll want to get to the urgent tasks as soon as possible, but we need to block some tim
for long-term planning and execution. Spending time on long-term tasks might not bear fruit right away, but it can be
critical when dealing with a large incident.

But investing in the future can save you even more time and user frustration when responding to a problem. Researching new technologies is another task in this category

___IT is always evolving and it's important to have time set aside to stay up to date.___

Another important task that might not necessarily be urgent is solving **technical debt**. When you work in IT, you
waste time a lot...

* **Technical Debt** is the pending work that accumulates when we choose a quick-and-easy solution instead of
applying a sustainable long-term one.

Technical debt can also be generated by external parties.

---

### Prioritizing Tasks

What can you do to figure out how to spend the limited time that you have? 

There's a lot to say about this, and everyone works a little differently. So you'll need to find the system that
works best for you. But let's cover the basic structure that can help us get organized and prioritize our tasks

The first step is to make a list of all of the tasks that need to get done.

You can make this list on a piece of paper, a text file in your computer, a bug tracking system, or a ticket
management system. Whatever works for you. 

The point is to have all the tasks listed in one place to avoid depending memory later. Once you have the list, you
can check the real urgency of the tasks. 

Ask yourself, if any items don't get done today will something bad happen? If yes, then those should be worked on
first. Once you're done with the most critically urgent tasks, you can look at the rest of the list and assess the
importance of each issue.

Even when it looks like everything is important, you should be able to tell that some things are more important than
others

___A task that will benefit more people is more important than a task that will benefit less people___

If there are a bunch of different tasks that depend on you completing one, that roadblock is more important to clear
than the rest

You can try dividing the tasks into groups of most important, important, and not so important. And then sort the
tasks inside each group, but don't spend too much time doing this sorting. In the end, the exact order isn't what
matters. What matters is that you spend most of your time working on the most important tasks

And if you work with a team of people, it's a good idea to share both the list of tasks and the standard of
prioritization among team members. This helps you avoid having to do the work multiple times and coming out with
different priorities

Once you have a list of the most important tasks to work on, you'll want to have a rough idea of how much effort they
'll take.

This isn't about exact timing, it's about assigning rough sizes. One common technique is to use small, medium, and
large. And when the range of sizes is big enough, include extra small or extra large if needed. Once you identify
the most important tasks and how big they are, you can start working on them

If possible, try to start with the larger, most important tasks to get those out of the way first

When our work involves IT support, we know that we'll have to deal with interruptions. And working on complex tasks
while getting interrupted can be very frustrating.

One strategy that can help us with that is saving the most complex tasks for the moments when we're less likely to
get interrupted. If you know that you get busiest in the morning, and you tend to have more quiet time during the
afternoon, it makes sense to work on easy and quick tasks early in the day. Save the most complex tasks for later, when you'll have more time to concentrate on them

But when your focused time starts, you should make sure that you work on those large complex tasks and not on the
easy ones. Otherwise, the complex tasks will never get done. 

__The key here is to always work on important tasks__

If a task is not important, it shouldn't be done at all.

Select which task you're going to deal with depending on urgency and how much time you can devote to it, starting
with the biggest tasks that you can fit in the time you have available

But keep in mind, this shouldn't stop you from taking a break or working on experimental projects. Taking breaks is
important because it allows our creative minds to stay fresh, and working on a fun side project can help us research
emerging technologies and come up with new ideas

What can we do if after all of this prioritizing, sizing, and ordering there's just too much work to be done and too
few hours in the day? The first thing to know is this is normal, most people working in IT have too much to do and
can't get all the things they want done.

Which means there are basically two options, either you get extra help from other team members or you decide that
some tasks weren't really that important, and they won't get done. For both of these options, you'll need to involve
other people, like your manager, and make sure that expectations get clearly communicated.

---

### Estimating the Time Tasks Will Take

When deciding whether a manual task needs to be automated, we should consider two things; how many times we'll do the
task over a period of time and how long it takes to do it manually

From there, we can figure out if that number is larger than the time it will take us to write the automation

This sounds great in theory, but the problem is that we don't know how long it'll take us to write the automation
until we've actually written it. 

All we can do is estimate it, and most of us are really bad at estimating how long tasks will take.

We tend to be too optimistic about the amount of time that a certain piece of code will take us to write or a certain
infrastructure will take us to set up

Usually, our first instinct is to consider how much we can get done with an ideal amount of focus on the work and a
full grasp of the problem we're trying to solve.

We forget to take into account the many obstacles that we might face like finding a bug that we don't know how to fix
, being interrupted by a problem that needs more urgent attention, or discovering that a new tool doesn't work well
with the rest of the tools we have in place

If you're trying to estimate how long it will take you to complete a project, big or small, you need to be
realistic. Avoid being overly optimistic with your time estimates

The best way to do this is to compare the task that you're trying to do with similar tasks that you've done before
. This way, you're not estimating based on how long you would like the project to take but on how long other similar
projects actually took in the past

If the task at hand is large, it might be hard to find something similar enough to use for comparison. So to make a
better estimate of a bigger than average project, you'll want to chop it up. Split the task into smaller steps
. Compare each step to a similar task that you've done in the past and assign an estimated amount of time to each
step based on that. 

If one smaller step is still too large, then split it into even smaller pieces until you can compare each piece of
the puzzle was something that you've done before

Once you've got all those estimated times, just add them up and you'll have a rough estimate of how long the whole
task will take. But even that's going to be optimistic since putting all the pieces together will take additional time.

So once you have a rough estimate of the total time of all the steps, you want to factor in some extra time for
integration.

This should also come from prior experience. Think about how long it took you to integrate the pieces of a project
before, and you'll have a rough idea of how much to add to the previous value. 

Knowing how optimistic humans are, even after basing those estimations on previous experience, the number you come up
with is going to be very close to the best possible scenario.

Even if you're prepared for something to go wrong, it's impossible to anticipate new unknown bumps in the road, so
take this estimation and multiply it by a factor.

Once again, this factor works best when it's based on previous experience

You want to have a grounded estimate of how long it will take you to complete the task

That means taking into account the obstacles that you'll certainly run into but haven't come across yet. No matter
how detailed we are, the final estimation won't ever exactly match the time it takes, but it will give us a rough
idea of whether we can complete the task in a few hours, days, weeks, or months.

Once you've made your estimation, you want to note it down somewhere so that you can check later to see how close
you were to the original number. You can adjust future estimations based on that.

---

### Communicating Expectations

When you're dealing with an issue that's affecting one or more users, you might feel rushed to meet expectations, set
by the people you're helping

Everyone's got their own ideas of how long it will take you to solve the problem and when they can expect a solution

If the issue is that the users spilled coffee on their keyboard and needs a new one, the expectation is that
replacing the keyboard will be a very small task that will take almost no time. If the issue is that there's a new
employee starting soon and they need a new computer setup for them, the expectation is that it will take much
longer than replacing a keyboard

Even if we have an automated process for setting up new computers, which means there's very little manual work, to
have successful interactions with our users, it's important to understand these implicit expectations and let users
know if fixing the problem will take longer than they expect

Users will be happy if the issue is resolved within their expectations, but will become frustrated if it takes much
longer than they thought

But as long as we communicate with them early about the circumstances, they will be able to understand this and
manage their time accordingly

It's also important to let users know if there are any conflicting priorities that might delay the response to
whatever they need.

__Communication is key__ 

Try to be clear and upfront about when you expect the issue will be resolved, and if for any reason the issue isn't
solved by then, explain why and what the new expectation should be.

When the issue you're trying to solve involves troubleshooting and debugging, it's usually very hard to give an
accurate estimate of how long it will take you to fix the problem.

A lot of your time will be spent investigating looking into what's going on and figuring out what should be happening.

Make sure to let users know when they can expect an update on their issue and give them timely updates, if possible
it's a really good idea to have users filed the requests through a **ticket tracking system**

Using a system like this has a ton of advantages. Having all the work you need to do in one place lets you organize
your tasks by priority as discussed before.

Receiving reports of issues through a system instead of a phone or chat, lets you make better use of your time.

You can now decide when you'll look at the list of issues instead of getting interrupted in the middle of a task, and
when you have an update for an issue that you've been working on, you can easily update the ticket with news
without having to track down users to let them know what's up with their request.

Try out some practical shortcuts when dealing with users.

It makes sense to take some time to think about the work you do and figure out ways to avoid interruptions and save
time.

Sometimes spending time on improving your infrastructure can help you get more done in less time. 

Automating processes like installing new computers, setting up new user accounts, deploying virtual machines, or
rolling back changes to previous versions can help save you a lot of time when you're responding to an incident.

---

### Making the Most of Our Time

* [How To Prioritize](https://blog.rescuetime.com/how-to-prioritize/)

---

## Making Our Future Lives Easier

### Dealing with Hard Problems

Brian Kernighan, one of the first contributors to the Unix operating system and co-author of the famous C programming
language book, among many other things, once said:

>*Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as you can be
 when you write it, how will you ever debug it?*

This is a warning against writing complicated programs. If the code is *clear* and *simple*, it will be much easier
to debug than if it's clever but obscure.

The same applies to IT systems.

* If the system is engineered very cleverly, it will be extremely hard to understand what's going on with it when
 something fails. 

* It's important to focus on building systems and applications that are simple and easy to understand. So that when
 something goes wrong, we can figure out how to fix them quickly.
 
Something that's really valuable is to develop code in small, digestible chunks. Every so often, stop
and test what I've written. 

The hardest thing to do is to try to debug something when running it for the first time only after it's completed
. There are so many places things could have gone wrong.

If you're writing code, try writing the tests for the program before the actual code to help you keep focus on your
goal. 

If you're building a system or deploying an application, having documentation that states what the end goal
should be, and the steps you took to get there can be really helpful.

If the problem you're trying to solve is complex and affects a lot of people, it can get really stressful to try to
fully debug it with everyone waiting on you. That's why it's better to focus first on the short-term solution, and
then look for the long-term remediation once those affected are able to get back to work.

__And don't be afraid to ask for help__

There's a technique called **rubber duck debugging**, which is simply explaining the problem to a rubber duck

When you ask a colleague for their help with debugging a problem, be careful not to tell them what you think the root
cause of the issue might be. Instead, tell them about the symptoms, and see what questions they ask and what
possibilities they probe. They might come up with completely different paths to explore

___

### Proactive Practices

We'll come across lots of bugs that trigger lots of different failures in our programs. There's a bunch of strategies
we can adopt to make our lives easier, by catching issues before they affect our users or making troubleshooting
simpler by having better information

To avoid having to scramble to fix things when there's an outage, it's really helpful to have infrastructure that
lets us test changes in advance so that we can check that things are working as expected before they reach our users

If we're the ones writing the code, one thing we can do is to make sure that our code has good unit tests and
integration tests. If our tests have good coverage of the code, we can rely on them to catch a wide array of bugs
whenever there's a change that may break things

For these tests to be really meaningful, we need to run them often, and make sure we know as soon as they fail.

Setting up continuous integration can help

Another step in this direction is to have a test environment, where we can deploy new code before shipping it to the
rest of our users. This serves two purposes; First, we can do a thorough check of the software as it will be seen by
the users. Depending on the software and how often we update it, we can do both automated and manual tests in this
environment. Second, we can use this test environment to troubleshoot problems whenever they happen. We can try p
possible solutions and new features without affecting the production environment.

Another recommended practice when managing a fleet of computers is to deploy software in **phases** or **canaries**

What this means is that instead of upgrading all computers at the same time and possibly breaking all of them at the
same time, you upgrade some computers first and check how they behave. If everything goes fine, you can upgrade a
few more, and so on until you're confident enough to upgrade the remaining part of the fleet.

To make the best use of this practice, we'll need to be able to easily roll back to the previous version. Depending
on the software, this might require more or less infrastructure. ___THIS IS WORTH THE TIME___

We can make our troubleshooting easier by including good debug logging in the code.

That way, whenever we have to figure out an issue, we can look at the logs and get a pretty good idea of what's
going on.

Another method that can help us is having centralized logs collection. This means there's a special server that
gathers all the logs from all the servers or even all the computers in the network 

That way, when we have to look at those logs, we don't need to connect to each machine individually, we can comb
through all the logs together in a centralized server

Similarly, having a good monitoring system can be super helpful. We can use it to catch issues early before they
affect too many users. During a debugging session, we can look at the collected data to try to determine if there's
anything out of the ordinary going on

Making good use of a ticketing system can help us save a lot of time when trying to get to the bottom of a problem
. If we ask users to provide the needed information up front, we don't have to waste time and go back and forth

___Even here, we can look at opportunities for automation___

Say you almost always want some specific info from the users computers, you can automate getting it by creating a
script that gathers all the data you want and have the users attach it to the ticket.

Finally, remember to spend time writing documentation. Just as importantly, store the documentation in a well-known
location. Even if writing documentation isn't especially fun, having good instructions on how to solve a specific
problem, knowing how to diagnose what's going on with the server, or tracking the known issues in a system can be
real time savers

At Google, they have a bunch of docs called Playbooks where they detail what a person who's on call can do to
diagnose and mitigate a ton of different problems. By keeping this information updated, they make sure that no matter
who the person on call is, everybody has access to the knowledge base accumulated by the whole team. 

If we're dealing with systems that change and grow, we can proactively plan for the additional capacity that we'll
need in the future

___

### Planning Future Resource Usage

Sometimes, it's not a question of misusing resources, but rather missing resources

A database server is expected to use more disk storage as more data gets stored. Or a web server is expected to use
more network bandwidth as the service grows in popularity.

If you're dealing with a service that's expected to grow and will acquire more resources in the future, it makes
sense to spend some time thinking about what that might look like

Planning ahead will prepare you for when you need additional resources, instead of having to scramble for them at the
last minute

> Lets say the database growth is expected to be one megabyte per day, and you have 500 megabytes of free-space. You
> can use that storage for almost two years. But if the growth is expected to be 10 megabytes per day and you only
> have those 500 megabytes available, then you need to start figuring out a plan that will allow your database to
> keep growing at that pace. Otherwise, you run out of space in a couple of months

Once you've figured out the current usage and the expected growth, don't forget to write this down so you can refer
to it in the future and check if anything has changed

If you find that you'll soon be running out of space, what you'll do next will depend on what the system does, and
the importance of the data

You might decide that you don't really want to store all that data, and instead clean up anything that's not really
necessary, or you might decide that you really need to have a lot more storage available. In that case, you might
opt for buying a network attached storage or **NAS** that can be attached to your server for additional disk space

__Migrating to a different type of storage takes time, and can be tricky to do right under pressure__

It's important to do this kind of planning in advance and not wait until the disk is completely full. This means
monitoring the usage growth of the computer to see if there are any trends that need attention. 

Our monitoring system should trigger an automatic alert when daily growth increases to unexpected levels

An interesting strategy for making the best possible use of resources, is to mix and match the processes that run
on the computers, so they make use of all the available resources

> If you have a process that's CPU intensive and takes almost all the available CPU on a computer, you can still run
> processes that are IO intensive, reading and writing a lot of data to the hard drive. Or if you have a service that
> requires a lot of RAM, you can pair it with another one that uses very little memory, and mostly sends and receives
> data over the network

An alternative for having to deal with all these resources like figuring out when to buy more and how to distribute
them, is to migrate those systems to the Cloud.

Setting up your service to run on the cloud will require some initial setup time, as well as an ongoing cost for th
Cloud resources you're using

But while this is more expensive than what you'd pay when running the service on premise, you're basically delegating
all your capacity planning needs to your Cloud provider

That way, if the initial setup doesn't have enough space, you can simply attach a bigger hard drive. Or if the
program needs more RAM, you can just deploy the service in a virtual machine with more memory assigned

If you decide that moving to the Cloud is a good way to go for your company, remember that you'll also need to plan
for that. Migrating your services to run fully or even partially in the Cloud, requires work on your side. So you'll
need to decide if and when to make the leap, to avoid your service having an outage because it ran out of resources

___

### Preventing Future Problems

Whenever we're faced with an issue, it's usually best to find a quick workaround. So that those affected can get back
to work as soon as possible

Say your database server crashed because it ran out of space. You can solve it quickly by adding an extra hard drive
and starting the service back up. But remember, our work doesn't finish there

Once the affected users are happily doing their job, we need to look for a long-term solution that will prevent the
problem from happening again in the future

In the database server scenario, that would be detecting that the disk is running out of space before it happens

___One key strategy is to make good use of monitoring___

You want the computers you care about to send their data to a centralized location that aggregates all this
information. And then you want to be able to look at both the information yourself, and trigger alerts when the
values are not within acceptable range

When you first set up a monitoring system, you might not be sure what information to prioritize, so start with the
basics: **CPU**, **disk**, **memory**, and **network usage**. As time passes and you have to deal with more incidents
, you'll probably discover other metrics that you'd like to include in your monitoring system

You'll also want to include information related to the specific service running on the computer. If it's a web server
, you'll want to know the ratio between successful web responses and errors.

If it's a database server, you'll want to know how many queries that are being served over time

Whenever you have to deal with an incident that wasn't caught by the monitoring system, remember to set up new
monitoring and alerting rules that will notify you about the problem if it ever happens again
 
___An important capability of monitoring is to include the measurements taken along a period of time___

That way, we can keep track of how we're using our resources, and catch changes in tendencies early on to help us
with planning.

If you have to work around an issue in an application developed by someone else, it's important that you report a bug
to the relevant developers. That way, those in charge of the code can take your case into account and make it work
correctly in the future

If you don't do this, it's possible that the workaround you figured out for the current version is not sufficient for
the next version, and you'll have to figure out a whole new workaround

When reporting a bug to someone else, let them know what you were trying to achieve, what you did, what the expected
result was, and what the actual result was. Include your reproduction case and workarounds for the issue. If you
have access to the source code of the project, providing a patch that fixes the issue increases the chance of that
code getting fixed

On the flip side, if you have to work around an issue in the software that you own, make sure that you write a test
that catches the problem

That way, you can be sure that you won't ever make a change to the code that will trigger that same issue again. And
even if you're not in charge of the development of the software, you can still run automatic tests whenever there's a
new version, just to check if it still works as expected.

So make sure you perform these tests whenever a new version of the application comes around.

Finally, regardless of whether the bug came from software that you wrote or someone else wrote, make sure that you
document the key pieces of what you did, how you diagnosed the issue, and how you squashed it.

___

### Extra Reading on Preventing Future Breakage

Preventing future breakage is a bit of a dynamic subject. Probably the most useful techniques here are identifying, isolating, and managing problem domains and failure domains. 

**Problem Domains** just describe the complexity of a given problem that one is trying to solve. Let’s look at an
 example below:

For example: counting the number of occurrences of a specific word in one of Shakespeare’s plays, like Hamlet. This is an indexing problem. And its problem domain is fairly limited in scope. It’s a single word, and a single play. A bit of BASH could easily solve this problem. So the problem domain is small, and the technical solution is fairly simple.

However, if the scope is widened slightly to include all of Shakespeare’s plays, the problem domain becomes larger. Any software solution used to try and solve this indexing problem has to now handle various logic that it did not have to handle before, like consolidating word occurrences in various plays. I.e. the word ‘Brevity’ may occur at least once in Hamlet, and N number of times in various other plays. Managing N occurrences of ‘Brevity’ over M works of Shakespeare is an order of magnitude more complex in terms of describing the problem domain. A bit of BASH could solve this problem, but it might be difficult.

If the problem becomes slightly more complex, such as finding the occurrences of various synonyms to a given word, then the problem domain becomes equally large. Managing original words, their synonyms, and their hit-count across multiple works of Shakespeare is even MORE complex.

So why is any of this useful? Well, if one can easily describe and reason about a problem in a lot of detail, they understand the Problem Domain fairly well. Producing a software solution for a given problem becomes easier when the Software Engineer understands the problem domain fairly well. Of course, building a good understanding of the Problem Domain often requires a lot of experimentation, and iteration. This is why it’s good to make a few initial attempts at testing a design before building an entire Production system to solve a problem like indexing Shakespeare.

##### Failure Domains

Like problem domains, failure domains just describe the complexity of a system. Except, instead of describing the various problems a system tries to solve, failure domains describe various sub-systems which may fail. Using the Shakespeare example again, if one of your systems is responsible for managing the full text of the works of Shakespeare (a content server), that might be a single failure domain. If another system is responsible for actually searching that content and counting the words (an indexer), that is a separate failure domain. Some failure domains can be within other failure domains. For example, if an indexer fails, the content server may not fail. But if a content server fails, the indexer will probably also fail.

So why do we care about any of this? Well, Problem Domains drive system complexity. Complex systems often have many failure domains. The key to preventing future breakage is to identify, and manage the scope and severity of a failure domain. This may mean redesigning the system in a way that has many smaller failure domains, instead of few large ones. 

As another example It’s better to have a video streaming service slow down instead of failing entirely. This kind of graceful degradation is can be attributed to isolated failure domains.

This topic can be a bit complex, but there are several community articles on the idea of identifying and managing failure domains. Consolidating and completely eliminating possible failure domains is the key to preventing future breakage. If anything, managing failure domains should keep the scope of a break as small as possible. 

___

### Extra Resources on Preventing Future Breakage

* [Understanding the Problem Domain is the Hardest Part of Programming](https://simpleprogrammer.com/understanding-the-problem-domain-is-the-hardest-part-of-programming/)

* [Thinking Like an Architect: Understanding Failure Domains](https://blog.turbonomic.com/blog/on-technology/thinking-like-an-architect-understanding-failure-domains)

* [Effective Troubleshooting](https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/)

---
