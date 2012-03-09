Installing Django on Lighttpd with FastCGI
==========================================
Speaker: JR Rickerson

This was a brief lightning talk and demo of the steps necessary to get Django
running under Lighttpd and FastCGI.  The process was gleaned from information
on the Django documentation here:
https://docs.djangoproject.com/en/1.3/howto/deployment/fastcgi/

An example `lighttpd.conf` configuration file is provided here, as is a small,
simple Django "Hello World!" project to test with. Additionally, a sample
bash script for restarting the FastCGI processes is included. Please note that
you will probably have to change several file paths to match your own install.

Step 1: Installing Lighttpd
---------------------------

Use your distro's package manager.  For instance, on Ubuntu:
    apt-get install lighttpd

Lighttpd comes with the fastcgi module, so it doesn't need to be installed
separately.


Step 2: Install Django and Flup
-------------------------------

    pip install django
    pip install flup


Step 3: Configure Lighttpd
--------------------------

- Enable `mod_rewrite` and `mod_fastcgi`
- Set up a virtual host configuration for the right domain
- Point fastcgi module to the appropriate socket file or host/port
- Rewrite any urls you need to for static files
- Restart lighttpd after any configuration changes:
  `/etc/init.d/lighttpd restart` on Ubuntu


Step 4: Start the Django FastCGI process
----------------------------------------

From within the django project, use:
    python manage.py runfcgi 
and provide whatever options to match your lighttpd configuration and
needs.  See here for available options:
  https://docs.djangoproject.com/en/1.3/ref/django-admin/#django-admin-runfcgi

Note that any time you upload new python changes to the webserver, you will
need to restart the FastCGI processes.
