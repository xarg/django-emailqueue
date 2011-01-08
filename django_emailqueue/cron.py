#!/usr/bin/python
# coding: utf-8
#
# Execute it like this:
# cron.py /path/to/django/project /path/to/lockdir
#

import sys, os
from datetime import datetime

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

def send_emails():
    """ Send mass e-mails. Mark them and update the sent date.
    If an error is encountered notify admins

    """
    try:
        mass = []
        sent_queues = []
        email_queues = EmailQueue.objects.exclude(sent=True).all()
        for queue in email_queues:
            sent_queues.append(queue.pk)
            mass.append((queue.mail_subject, queue.mail_body,
                         queue.mail_from, [queue.mail_to], ))
        send_mass_mail(tuple(mass))
        EmailQueue.objects.filter(pk__in=sent_queues).update(sent=True,
                                                sent_datetime=datetime.now())
    except Exception, e:
        mail_admins("django_emailqueue exception", str(e))

def main():
    if lock(LOCK): # Acquire lock by creating a temporary directory
        #Cycle through apps and execute app_name.cron.emailqueue
        for app in settings.INSTALLED_APPS:
            if not app.startswith('django.'):
                try:
                    module = __import__(app)
                except ImportError:
                    continue
                try:
                    cron = __import__(module.__name__ + '.cron')
                except ImportError:
                    continue
                try:
                    if hasattr(cron, 'cron') and hasattr(cron.cron, 'emailqueue'):
                        if callable(cron.cron.emailqueue):
                            cron.cron.emailqueue()
                except Exception, e:
                    mail_admins("django_emailqueue exception", str(e))
        send_emails()
        unlock(LOCK) # Release lock by deleting that directory

if __name__ == "__main__":
    main()
