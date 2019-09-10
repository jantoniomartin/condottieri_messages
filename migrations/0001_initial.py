# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('machiavelli', '__first__'),
        ('django_messages', '0002_auto_20160607_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('message_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='django_messages.Message', on_delete=models.CASCADE)),
                ('year', models.PositiveIntegerField(default=0)),
                ('season', models.PositiveIntegerField(default=1, choices=[(1, 'Spring'), (2, 'Summer'), (3, 'Fall')])),
                ('recipient_player', models.ForeignKey(related_name='received_messages', verbose_name='To country', to='machiavelli.Player', on_delete=models.CASCADE)),
                ('sender_player', models.ForeignKey(related_name='sent_messages', verbose_name='From country', to='machiavelli.Player', on_delete=models.CASCADE)),
            ],
            bases=('django_messages.message',),
        ),
    ]
