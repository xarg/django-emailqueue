from django.contrib import admin

from models import EmailQueue

class EmailQueueAdmin(admin.ModelAdmin):
    list_display = ('mail_to', 'mail_subject', 'created_datetime',
                    'sent_datetime', 'sent', )
    date_hierarchy = 'created_datetime'
    list_filter = ('sent', )
    search_fields = ('mail_to', 'mail_subject', )

admin.site.register(EmailQueue, EmailQueueAdmin)
