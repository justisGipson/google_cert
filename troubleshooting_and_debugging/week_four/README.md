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



---

### Network Saturation



---

### Dealing with Memory Leaks



---

## Managing Our Time

---

## Making Our Future Lives Easier

---
