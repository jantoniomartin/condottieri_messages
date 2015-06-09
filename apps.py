from django.apps import AppConfig
from django.db.models.signals import post_migrate

from condottieri_messages.signals import handlers

class CondottieriMessagesConfig(AppConfig):
    name = 'condottieri_messages'
    verbose_name = 'Condottieri Messages'

    def ready(self):
        post_migrate.connect(handlers.create_notice_types, sender=self)
