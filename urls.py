from django.conf.urls import *
from django.views.generic.base import RedirectView

import condottieri_messages.views as views
from condottieri_messages.views import BoxListView

## urls that call the views in messages
urlpatterns = patterns('messages.views',
    url(r'^$', RedirectView.as_view(url='inbox/')),
)

## urls that call the custom views in condottieri_messages
urlpatterns += patterns('condottieri_messages.views',
	url(r'^compose/(?P<sender_id>[\d]+)/(?P<recipient_id>[\d]+)/$', 'compose', name='condottieri_messages_compose'),
    url(r'^reply/(?P<letter_id>[\d]+)/$', 'compose', name='condottieri_messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', 'view', name='condottieri_messages_detail'),
	url(r'^inbox/$', BoxListView.as_view(box='inbox'), name='messages_inbox'),
	url(r'^outbox/$', BoxListView.as_view(box='outbox'), name='messages_outbox'),
	url(r'^trash/$', BoxListView.as_view(box='trash'), name='messages_trash'),
	url(r'^inbox/(?P<slug>[-\w]+)/$', BoxListView.as_view(box='inbox') , name='condottieri_messages_inbox'),
	url(r'^outbox/(?P<slug>[-\w]+)/$', BoxListView.as_view(box='outbox') , name='condottieri_messages_outbox'),
    url(r'^delete/(?P<message_id>[\d]+)/$', 'delete', name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', 'undelete', name='messages_undelete'),
)
