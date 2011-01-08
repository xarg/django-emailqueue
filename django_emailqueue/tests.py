# -*- coding: utf-8 -*-
from django.test import TestCase
from models import EmailQueue
from cron import send_emails
from django.core import mail

class EmailQueueTest(TestCase):
    def test_send_emails(self):
        email_queue = EmailQueue(mail_to='test@email.com',
                                 mail_subject="Notification",
                                 mail_body="mail body")
        email_queue.save()
        send_emails()
        email_queue = EmailQueue.objects.all()
        assert len(email_queue) == 1
        assert email_queue[0].sent is True
        assert email_queue[0].sent_datetime is not None

        assert len(mail.outbox) == 1
        assert mail.outbox[0].subject == 'Notification'
