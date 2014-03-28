============
ØMQ Examples
============

:author: Daniel J. Rocco, @drocco007
:date:   September 2013

Example code for my September 2013 PyAtl talk *Let's Talk*.


hello
=====

Illustrates a basic request-response communication mechanism. Pretty much a
straight copy from the guide example: http://zguide.zeromq.org/py:hwclient

Run with::

    python hwserver.py

and in a separate window

::

    python hwclient.py


fizzbuzz (*)
============

Very contrived publish-subscribe example.

::

    python ventilator.py

starts the publisher, which publishes the numbers 1 to 100 forever. Yes. Time
it if you don't believe me.

Start the clients with something like

::

    python fizzer.py & python buzzer.py &

Although this example is highly goofy, it does illustrate the basic principles
of publish-subscribe in ØMQ. Remember:

1. Publishers do not wait. If you want synchronization, you need to add it.

2. Subscribers *must* set a subscription, even if it's ``''`` (everything). If
   you forget this, your listeners will be surprisingly deaf (like my kids).

(*) not a real FIZZBUZZ


image_farm
==========

``image_farm`` illustrates work distribution and processing, in this case
resizing images in batch. The workers (``farmer.py``) receive source images and
generate three size of thumbnails for each image they receive. Each worker
sends a message to a listening process (``sink.py``) when finished.

To try it out, first fire up some workers::

    python farmer.py  # want >1 of these
    python farmer.py
    python farmer.py

and a sink

::

    python sink.py

Then, queue up some images::

    python cli_enqueue_images.py image1.png image2.jpg ...

You probably want to give it quite a few images: modern hardware is quite fast.
You'll need PIL installed for this to work; I suggest installing the Pillow
fork unless you enjoy debugging build problems from an archaic package::

    pip install Pillow
