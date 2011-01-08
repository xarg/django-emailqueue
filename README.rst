django-emailqueue
=================

Description
-----------
A very simple email queueing module that can be used to send mails using cron.
The sent e-mails are marked as deleted for future reference.
The module now searches every app for cron.py and executes the ``emailqueue`` callable
inside it.

Example appname/cron.py
-----------------------

::

    from django_emailqueue.models import EmailQueue
    def emailqueue():
        reminder = get_reminders()
        email_queue = EmailQueue(mail_to=reminder.user.email,
                                 mail_subject="Noitification",
                                 mail_body=render_to_string(
                                    'accounts/reminder.txt',
                                    {'body': reminder.body}
                                ))
        email_queue.save()

Installation
------------

easy_install django-emailqueue

Put ``django_emailqueue`` into **INSTALLED_APPS** and make sure you set
**DEFAULT_FROM_EMAIL** and **DEFAULT_REPLYTO_EMAIL** if you want default
email addreses.

Usage
-----
Put this into a cron:
    django_emailqueue_cron /path/to/django /path/to/lockdir
