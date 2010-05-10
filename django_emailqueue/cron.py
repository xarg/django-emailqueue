#!/usr/bin/python
# coding: utf-8
#
# Execute it like this:
# cron.py /path/to/django/project /path/to/lockdir
#

import sys, os

try:
    sys.path.append(sys.argv[1])
except IndexError:
    print "Error: Provide a path to your django project as the first argument"
    sys.exit(1)
try:
    import settings
except ImportError:
    print "Error: No settings.py can be found in this path"
    sys.exit(1)

from django.core.management import setup_environ
setup_environ(settings)

from django.core.mail import send_mass_mail, mail_admins
from django_emailqueue.models import EmailQueue

try:
    LOCK=sys.argv[2]
except IndexError:
    LOCK='tmp.lock'

def lock(dir):
    try:
        os.mkdir(dir)
        return True
    except:
        return False

def unlock(dir):
    os.rmdir(dir)

def main():
    if lock(LOCK): # Acquire lock by creating a temporary directory
        try:
            mass = []
            delete_queues = []
            email_queues = EmailQueue.objects.all()
            for queue in email_queues:
                delete_queues.append(queue.pk)
                mass.append((queue.mail_subject, queue.mail_body, queue.mail_from, [queue.mail_to]))
            import pdb; pdb.set_trace()
            send_mass_mail(tuple(mass))
            EmailQueue.objects.filter(pk__in=delete_queues).delete()
        except Exception, e:
            mail_admins("django_emailqueue exception", str(e))
        unlock(LOCK) # Release lock by deleting that directory

if __name__ == "__main__":
    main()
