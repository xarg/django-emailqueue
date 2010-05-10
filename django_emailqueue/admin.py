from django.contrib import admin

from models import EmailQueue

class EmailQueueAdmin(admin.ModelAdmin):
    """ """
    
admin.site.register(EmailQueue, EmailQueueAdmin)
