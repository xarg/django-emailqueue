from datetime import datetime

from django.db import models
from django.db.models import signals
from django.conf import settings

class EmailQueue(models.Model):
	mail_to = models.CharField(max_length = 200)
	mail_from = models.CharField(max_length = 200, default=getattr(settings, 'DEFAULT_FROM_EMAIL', None))
	mail_replyto = models.CharField(max_length = 200, default=getattr(settings, 'DEFAULT_REPLYTO_EMAIL', None))
	mail_subject = models.CharField(max_length = 200)
	mail_body = models.TextField()
	created_date = models.DateTimeField(default = datetime.now())

	def __unicode__(self):
		return "[%s] %s" % (self.mail_to, self.mail_subject)
