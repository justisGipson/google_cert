# Troubleshooting and Debugging Techniques - Week 2

Rundown of the different reasons that can make things run slowly by looking into:

* what causes slow scripts, slow computers, or slow systems

* what tools are there to help identify the most common causes of slowness, and apply solutions to improve the
 overall performance
 
---

## Understanding Slowness

### Why is my computer slow

The general strategy for addressing slowness is to **identify the bottleneck** for addressing slowness in  device, script, or system to run slowly. 

Some of the reasons could be:

* Running out of the CPU time

* Time spent reading data from disk waiting for data transmitted over the network

* Moving data from disk to RAM


Treat each part of the computer (CPU, memory, disk, network bandwidth) as **finite resources**.

Identifying the bottleneck allows us to manage the available resources more effectively. In order to find what is causing the bottleneck, **monitor** the usage of resources to know which of them are being exhausted.

We can use the following commands on Linux to monitor the usage of resources:

* **top** command on shows:
  * Which currently running processes are using the most CPU time
  * Which currently running processes are using the most memory
  * Other load information related to the current state of the computer such as how many processes are running and how the CPU time or memory is being used
  
* **iotop** command shows which processes are currently using the most disk IO usage and swap memory usage
* **iftop** command shows which processes are currently using the most network bandwidth

Therefore, steps to diagnose what's causing the computer to run slow would be:

1. Open one of above tools to check what's going on

2. Try to understand which resources the bottleneck and why

3. Plan how you're going to solve the issue


### How Computer Use Resources

When thinking about making things faster, it's important to understand the different speeds of the parts involved when accessing data/variables:

```(slowest) data from the newtok <- data from disk <- data from RAM <- data from CPU's inernal memory (fastest)```

Create a **cache** when the same files are read from disk repeatedly by putting the same information directly into the process memory and avoid loading it from disk every time. A cache stores data in a form that's faster to access than its original form.

Examples of caches in IT includes:

* Web proxy - stores websites, images, or videos that are accessed often by users behind the proxy

* DNS - implements a local cache for the websites they resolve so they don't need to query from the internet every time someone asks for their IP address

The operating system performs **swap** when there is not enough memory - the operating system will put the parts of
 the memory that aren't currently in use onto the hard drive in a space called swap. Reading and writing from disk is
  much slower than reading and writing from RAM. So when the swapped out memory is requested by an application, it
   will take a while to load it back. 
   
Swapping implementation varies between different OS, but same concept.
 
So what do you do if you find that your machine is slow because it's spending a lot of time swapping?

There are three possible reasons computer slows down due to constant swapping:

1. There are too many open applications
   * Solve by closing the ones that aren't needed
   
2. The available memory is too small for the amount that computer is using
   * Solve by add more RAM to the computer
   
3. One of the running programs may have a **memory leak**, causing it to take all the available memory
   * A memory leak means that memory which is no longer needed is not getting released


### Possible Causes for Slowness

Below are some of the possible causes for slowness:

* Too many applications are configured to start on a boot and the computer slows at start up
  * Solve by disabling applications that aren't really needed on a startup

* Computer slows after days of running and the problem solved by a reboot - an application keeps some state while running and takes the memory
  * Solve by modifying the code to frees up the memory after using it
  * If it can't be fixed, fix by scheduling a restart

* Computer slows after days of running and the problem isn't solved by a reboot - the files that an application handles grown too large
  * Solve by modifying the code to handle the large file - bug fix
  * If it can't be fixed, try to **reduce** the size of the files involved - **sharding**

* Only a subset of computer is slow
  * Check if there is any difference in configuration

* Computer slows due to a lot of reads and writes on the network-mounted file system
  * Solve by creating a cache
 
* Hardware failures

* Malicious software


### Slow Web Server

```Client complains about a web site loading slow```

First, reproduce the case and quantify the slowness with a tool called ```ab``` which stands for **Apache Benchmark** tool. ```ab``` checks if a website is behaving as expected or not by making a bunch of requests and summarize the results once it's done.

Below command gets the average timing of 500 requests, and then pass site.example.com for the measurement:

```Shell
    ab -n 500 site.example.com
```

Next, connect to the web server with ```ssh```

```Shell
    ssh SERVERNAME
```

Start by looking at the output of ```top``` and see if there's possible cause.

For this scenario:

* ```top``` output shows that the load average is around 30
  * The load average on Linux shows how much time the processor is busy at a given minute
  * For a single core processor with any number above 1 and a dual core processor with any number 2 is being **overloaded**
  * 30 means that there were more processes waiting for processor time than the processor had to give
  
* There are multiple ```ffmpeg``` processes running which uses all of the available CPU
  * ```ffmpeg``` program is used for video transcoding and a CPU intensive process

At this point, one thing we can try is to **change the processes priorities** so that the web server takes precedence which can be done with the following commands:

* ```nice``` command for starting a process with a different priority
* ```renice``` command for changing the priority of a process that's already running

Since there are multiple ffmpeg processes running, let's change priority of all of ```ffmpeg``` at once instead of
 running ```renice``` one by one with the following shell script:

```Shell
    for pid in $(pidof ffmpeg); do renice 19; $pid; done
```

Above shell script:

1. Iterates over the output of the ```pidof``` command with a for loop
   * ```pidof``` command receives the process name and returns all the process IDs that have that name
   
2. Calls ```renice``` for each of the process IDs
   * ```renice``` takes the new priority which is 19, the lowest possible priority, as the first argument, and the process ID to change as the second one

Check if the problem has been solved by running ```ab```. **For this scenario, the website is still slow.**

Transcoding processes are CPU intensive, and running them in **parallel** is overloading the computer. So one thing we could do is, modify the program to run the transcoding one at a time instead of all at the same time.

To do that, we'll need to find out how these processes got started:

1. Look at the output of the ```ps``` command to get some more information about the processes
2. Call ```ps ax``` which shows us all the running processes on the computer, and connect the output of the command to ```less``` to be able to scroll through it

```Shell
    ps ax | less

    #search for ffmpeg from the output of ps using '/' which is the search key when using less
    /ffmpeg
```

Upon search, it shows that

* There are multiple ffmpeg processes that are converting videos from the webm format to the mp4 format in static
* We don't know where these videos are on the hard drive

Use ```locate``` command to locate the file.

```Shell
    locate static/001.webm

    #locate command returns the following
    /srv/deploy_videos/static/001.webm
```

When there are multiple files, use ```grep``` command to check if any of the files contain a call to a searching term - in this case ```ffmpeg``` instead of checking them one by one.

```Shell
    grep ffmpeg *
```

The output of grep shows that ```deploy.sh``` script starts the ```ffmpeg``` processes in parallel using a tool called ```Daemonize``` that runs each program separately as if it were a daemon - address the issue.

**However, modifying the script does NOT change the processes that are already running.**

**Also we want to stop these processes but not cancel them completely**, as doing so would mean that the videos being converted right now will be incomplete.

To avoid canceling the processes, use the ```killall``` command with the ```-STOP``` flag which sends a stop signal but doesn't kill the processes completely.

```Shell
    killall -STOP ffmpeg
```

After stopping them all, we now want to run these processes **one at a time**. This can be done by sending the ```CONT``` signal one by one after each process completes the task. This can be automated with the similar for loop used earlier.

```Shell
    for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done;
```

Check if the problem has been solved by running ```ab```. **For this scenario, the problem is fixed at this point.**

___

#### Extra Reading

* [Process Monitor](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon) 
* [Linux Performance](http://www.brendangregg.com/linuxperf.html)
* [The USE Method](http://brendangregg.com/usemethod.html)
* [Activity Monitor in Mac:](https://support.apple.com/guide/activity-monitor/welcome/mac)
* [Performance Monitor on Windows](https://www.windowscentral.com/how-use-performance-monitor-windows-10)
* [How To: Windows Resource Monitor](https://www.digitalcitizen.life/how-use-resource-monitor-windows-7)
* [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)
* [CACHE](https://en.wikipedia.org/wiki/Cache_(computing))
* [Reddit: r/linux - on nice levels](https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/)

___

## Slow Code

### Writing Efficient Code

As a rule, aim first to write code that is to avoid bugs

* Readable
* Easy to maintain
* Easy to understand

If the code is not fast enough, tru to optimize by eliminating **expensive actions**, which are those that take a long time to complete.

* Trying to optimize every second out of a script is probably not worth the effort or time

The first step is to keep in mind that we can't really make our computer go faster. If we want our code to finish faster, we need to make our computer do less work, and to do this, we'll have to 

1. Avoid doing work that isn't really needed
2. Avoid calculating data repeatedly by using the right data structures and storing the data
3. Reorganize the code so that the computer can stay busy while waiting for information from slow sources like disk or over the network

Use a **profiler** tool to measure the resources that the code is using for better understanding of what's going on. It allows us to see which functions are called by our program, how many times each function was called and how much time are programs spent on each of them.

Because of how profilers work, they are specific to each programming language

* C program uses gprof to analyze
* Python uses c-Profile module to analyze

---

### Using the Right Data Structures

Using an appropriate data structures can help us avoid unnecessary expensive operations and create efficient scripts.

**Lists** are sequences of elements that can:

* Add, remove, or modify the elements in them

* Iterate through the whole list to operate on each of the elements

When adding or removing elements,

* Adding or removing elements **at the end** is fast

* Adding or removing elements in the middle can be slow because all the elements that follow need to be repositioned

When accessing or finding an element,

* Accessing an element in a specific position in the list is fast

* Accessing an element in an unknown position requires going through the whole list
  * This can be super slow if the list is long

```text
    ArrayList in Java
    Vector in C++
    Array in Ruby
    Slice in Go
```

**Dictionary** store key value pairs that can:

* Add data by associating a value to a key
* Retrieve a value by looking up a specific key

```text
    HashMap in Java
    Unordered Map in C++
    Hash in Ruby
    Map in Go
```

When accessing or finding an element,

* Looking up keys is very fast O(n)

In summary:

* If you need to access elements by position or will always iterate through all the elements, use a list

* If we need to look up the elements using a key, use a dictionary

Another thing that we might want to think twice about is creating copies of the structures that we have in **memory**.

### Expensive Loops

When using a loop, avoid doing expensive actions inside of the loop. If an expensive operation is performed inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop.

* Make sure that the list of elements that you're iterating through is only as long as you really need it to be

* Break out of the loop once the data is found **break** keyword in loops

### Keeping Local Results

For scripts that get executed regularly, it's common to create a local cache. A **cache** is a way to store data in a
 form that faster to access than it's original form. 
 
 * So if we're parsing a large file and only keeping a few key pieces of information from it, we can create a cache
  to store only that information, or if we're getting some information over the network, we can keep a local copy of the file to avoid downloading it over and over again.
  
We can add a check to validate if we need to recalculate the cache or not.

For example: 

  * if our cache is based on a file, we could store the modification date of that file when we calculated
  the cache. Then only recalculate the cache if the modification date of the file is newer than the one we had
  stored. 

### Slow Script with an Expensive Loop

* **time \<command>** - runs the command we pass to it, then tells us how long it took to execute, it returns 3
 different values:
 
  * **real** - amount of time it took to execute the command - sometimes called wall-clock time
  * **user** - amount of time spent doing operations in the user space 
  * **sys** - amount of time spent doing system level operations

The values of user and sys won't necessarily add up to the value of real because the computer might be busy with other processes.

### Extra Reading

* [Profiling](https://en.wikipedia.org/wiki/Profiling_(computer_programming))

---

## When Slowness Problems Get Complex

### Parallelization Operations

Operating in **parallel** is one way to run scripts more efficiently.

* **Concurrency** is dedicated to how we write programs that do operations in parallel

When data needs to shared while using the OS to split the work and the processes, use **threads**.

* These processes don't share any memory by default

__Threads let us run parallel tasks inside a process__. This allows threads to share some of the memory with other threads in the same process.

To handle threads, modify the code to create and handle the thread.

* In Python, use the **Threading** or **AsyncIO** modules (each programming language hsa different implementations)

These modules let us specify which parts of the code we want to run in separate threads or as separate asynchronous events, and how we want the results of each to be combined in the end

If your script is mostly just waiting on input or output, also known as **I/O bound**, it might matter if it's executed
 on one processor or eight.

---

### Slowly Growing in Complexity

__Example 1:__ Let's say you're writing a secret Santa script where each person gives a secret gift to one other
 randomly
 assigned person. The script randomly selects pairs of people and then sends an email to the gift-giver telling them who they're buying a present for. If you're doing this for the people working on your floor, you might just store the list of names and emails in a CSV file.
Play video starting at 46 seconds and follow transcript0:46
The file will be small enough that the time spent parsing it won't be significant. Now if this script grows into a larger project that handles everyone at your company and the company keeps hiring more and more people, at some point parsing the file will start taking a lot of time. This is where you might want to consider using a different technology.
Play video starting at 1 minute 8 seconds and follow transcript1:08
For example, you could decide to store your data in a SQLite file. This is a lightweight database system that lets
 you query the information stored in the file without needing to run a database server. Using SQLite for the data
  probably works just fine for assigning secret Santas at your company. But imagine that you've kept adding features to the service. So it now includes a way to create a wish list, a machine learning algorithm that suggests possible gifts and a tracker that keeps a history of each present given. And since people at your company love the program so much, you've made it an external service available to anybody. Keeping all the data in one file would be too slow. So you'll need to move to a different solution. You have to use a fully-fledged database server. Probably even running on a separate machine than the one running the secret Santa service. And there's even one more step after that. If the service becomes really really popular, you might notice that your database isn't fast enough to serve all the queries being requested. In that case, you can add a caching service like memcached which keeps the most commonly used results in RAM to avoid querying the database unnecessarily. So we've gone from hosting the data in a CSV file to having it in a SQLite file then moving it to a database server and finally using a dynamic cacher in front of the database server to make it run even faster.

__Example 2:__ A similar progression can happen on the user facing side of the same project. Initially, we set the Santa service would simply send emails to the people on the list. That's fine if it's a small group and there's one person in charge of the script. But as the project grows more complex, you'd want to have a website for the service to let people do things like check who their assigned person is and create wish lists. Initially, this could just be running on a web server on the same machine as the data. If the website gets used a lot, you might need to add a caching service like Varnish. This would speed up the load of dynamically created pages. And eventually, this still might not be enough. So you need to distribute your service across many different computers and use a load balancer to distribute the requests. You could do this in-house with separate computers hosted at your company, but this means that as the application keeps growing you need to add more and more servers. It might be easier to use virtual machines running in the cloud that can be added or removed as the load sustained by the service changes.

---

### Dealing with Complex Slow Systems

In large complex systems, we have lots of different computers involved. Each one doing a part of the work and
interacting with the others through the network. For example, think of an e-commerce site for your company. The web
 server is the part of the system that directly interacts with external users. Another component is the database
  server, which is accessed by the code that handles any requests generated from the website, and depending on how
   the whole system is built, you might have a bunch of other services involved doing different parts of the work
   . There could be a billing system that generates invoices once orders are placed. A fulfillment system used by the
    employees preparing the orders for customers. A reporting system that once a day creates a report of all the
     sales placed and possibly more. On top of this, you should probably have backup, monitoring, testing
      infrastructure, and so on. A system like this can be tricky to debug and understand. What do you do if your
       complex system is slow? As usual, what you want to do is find the bottleneck that's causing your
        infrastructure to under-perform. Is it the generation of dynamic pages on the web server? Is it the queries
         to the database? Is it doing the calculations for the fulfillment process? Figuring this out can be tricky
         . So one key piece is to have a good monitoring infrastructure that lets you know where the system is
          spending the most time. Saying notice that getting the web pages is pretty slow. But when you check the web
           server, you see that it's not overloaded. Instead, most of the time is spent waiting on network calls, and
            when looking at your database server, you find that it's spending a lot of time on Disk I/O. This shows
             that there's a problem with how the data is being accessed in the database. One thing to look at is the
              indexes present in the database. When a database server needs to find data, it can do it much faster i
                there's an index on the field that you're querying for. On the flip side, if the database has too
                 many indexes, adding or modifying entries can become really slow because all of the indexes need
                  updating. So we need to look for a good balance of having indexes for the fields that are actually
                   going to be used. If the problem is not solved by indexing and there are too many queries for the
                    server to reply to all of them on time, you might need to look into either caching the queries o
                      distributing the data to separate database servers. Now what if when you try to figure out why
                       the service is slow, you see that the CPU on the web serving machine is saturated. The first
                        step is to check if the code of the service can be improved using the techniques that we
                         explained earlier. If it's a dynamic website, we might try adding caching on top of it. But
                          if the code is fine and the cache doesn't help because the problem is that there's just to
                            many requests coming in for one machine to answer all of them, you'll need to distribute
                             the load across more computers. To make this possible, you might need to reorganize the
                              code so that it's capable of running in a distributed system instead of on a single
                               computer. This might take some work, but once you've done it, you can easily scale
                                your application to as many requests as needed by adding more computers to the system
                                , and finally, make sure that you actually need to do whatever you're doing. Lots of
                                 times, as projects evolve, we're left with a scary monster of layer after layer of
                                  complex code. If we think about what our system is doing for a few minutes, we
                                   might end up discovering that there's a whole piece that wasn't needed at all and
                                    it was making our servers do unnecessary work all along. 

---

### Using threads to make things go faster

To be able to run things in parallel, python scripts need an **Executor**. An Executor is the process that's in
 charge of distributing the work among the different workers.
 
The **Futures** module provides a couple different executors; one for using threads, another for using processes

---

### Extra Reading

* [Speed Up Your Python Program With Concurrency](https://realpython.com/python-concurrency/)
* [Threaded Async Magic](https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32)
