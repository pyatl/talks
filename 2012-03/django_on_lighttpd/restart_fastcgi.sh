#!/bin/bash

SCRIPTNAME="restart_fastcgi.sh"

# Setup variables for the project
PROJECTDIR="/home/reddog/code/pyatl/django_lighttpd"
PROJECTPID="$PROJECTDIR/fcgi.pid"
PROJECTSOCK="$PROJECTDIR/fcgi.sock"

if [ -f $PROJECTPID ]; then
     /bin/kill `/bin/cat $PROJECTPID`
     /bin/rm -f $PROJECTPID
fi

$PROJECTDIR/manage.py runfcgi method=threaded socket=$PROJECTSOCK pidfile=$PROJECTPID maxchildren=3

# This assumes the user lighttpd is running under and the user the FastCGI
# process is running under are in the same group
/bin/chmod 770 $PROJECTSOCK
