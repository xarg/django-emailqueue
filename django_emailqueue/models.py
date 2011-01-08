from django.db import models
from django.conf import settings

class EmailQueue(models.Model):
	mail_to = models.CharField(max_length = 200)
	mail_from = models.CharField(max_length = 200, default=getattr(settings, 'DEFAULT_FROM_EMAIL', None))
	mail_replyto = models.CharField(max_length = 200, default=getattr(settings, 'DEFAULT_REPLYTO_EMAIL', None))
	mail_subject = models.CharField(max_length = 200)
	mail_body = models.TextField()

	created_datetime = models.DateTimeField(auto_now_add=True)
	sent_datetime = models.DateTimeField(blank=True, null=True)
	sent = models.BooleanField(default=False)

	def __unicode__(self):
		return "[%s] %s" % (self.mail_to, self.mail_subject)
