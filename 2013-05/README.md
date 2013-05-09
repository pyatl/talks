Threading Patterns in Python
============================
JR Rickerson

Why Threading?
--------------
Sometimes, it makes sense to break a program down such that we can do little
pieces of it at a time, and some of those pieces can be done in parallel. It's
not a guarentee, but sometimes this can save us time overall, providing faster
processing of large amounts of information or faster user response time.

In this talk, we'll specifically be looking at threading.  However, many of
the same concepts apply to multi-process applications, or even applications
distributed across many machine in a cluster, or across the world.

Why Threading Patterns?
-----------------------
When we introduct threading or any kind of parallelism to an application, it
can help us solve a certain set of problems - however, it can introduce a whole
new set of problems as well.  When different threads of execution are sharing
the same resources - be it actual memory (variables, data structures),
communication channels (pipes, sockets), or stored information (files,
databases), unless we have a plan in place for coordinating access to these
resources, unintended behavior can occur.

Remember - the interpreter doesn't know what you intended, and the OS doesn't
have any concept of what order to execute statements in your threads in -
UNLESS you tell it.

Most threading libraries, including Python's, provide what are called
"synchronization" objects.  Using these, in conjuction with well-established
patterns for parallel process, can help us avoid or at least minimize many of 
the issues we could run into in the multi-threaded world.

Most of these patterns have been established because they continually crop up
as good solutions to common problems where multi-threading is useful, and
through refinement of techniques by programmers writing multi-threaded code
for years.

References
----------
- Python threading module: http://docs.python.org/2/library/threading.html
- PMOTW threading: http://pymotw.com/2/threading/
- Queue module: http://docs.python.org/2/library/queue.html

