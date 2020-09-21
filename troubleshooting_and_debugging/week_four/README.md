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




---

### Dealing with Memory Leaks


---

### Extra Resources About Managing Resources

* [Python Concurrency](https://realpython.com/python-concurrency/)

* [Threaded Asynchronous Magic and How to Wield It](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)

* [How To Profile Memory Usage In Python](https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python)

* [Troubleshooting Network Problems](https://www.linuxjournal.com/content/troubleshooting-network-problems)

___

## Managing Our Time

### Getting to the Important tasks



---

### Estimating the Time Tasks Will Take



---

### Communicating Expectations



---

### Making the Most of Our Time

* [How To Prioritize](https://blog.rescuetime.com/how-to-prioritize/)

---

## Making Our Future Lives Easier

### Dealing with Hard Problems


___

### Proactive Practices


___

### Preventing Future Problems


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

* [Thinking Like an Architect - Understanding Failure Domains](https://blog.turbonomic.com/blog/on-technology/thinking-like-an-architect-understanding-failure-domains)

* [Effective Troubleshooting](https://landing.google.com/sre/sre-book/chapters/effective-troubleshooting/)

---
