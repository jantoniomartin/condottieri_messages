from django.conf import settings
from django.utils.translation import ugettext_noop as _

def create_notice_types(sender, **kwargs):
    if "pinax.notifications" in settings.INSTALLED_APPS:
        from pinax.notifications.models import NoticeType 
        print "Creating notices for condottieri_messages"
        NoticeType.create("condottieri_messages_received", _("Letter Received"), _("you have received a letter"), default=2)
    else:
        print "condottieri_messages: Skipping creation of NoticeTypes"
