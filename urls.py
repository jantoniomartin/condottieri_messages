from django.conf.urls import url
from django.views.generic.base import RedirectView

from . import views

## urls that call the views in messages
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='inbox/')),
]

## urls that call the custom views in condottieri_messages
urlpatterns += [
	url(r'^compose/(?P<sender_id>[\d]+)/(?P<recipient_id>[\d]+)/$', views.compose, name='condottieri_messages_compose'),
    url(r'^reply/(?P<letter_id>[\d]+)/$', views.compose, name='condottieri_messages_reply'),
    url(r'^view/(?P<message_id>[\d]+)/$', views.view , name='condottieri_messages_detail'),
	url(r'^inbox/$', views.BoxListView.as_view(box='inbox'), name='messages_inbox'),
	url(r'^outbox/$', views.BoxListView.as_view(box='outbox'), name='messages_outbox'),
	url(r'^trash/$', views.BoxListView.as_view(box='trash'), name='messages_trash'),
	url(r'^inbox/(?P<slug>[-\w]+)/$', views.BoxListView.as_view(box='inbox') , name='condottieri_messages_inbox'),
	url(r'^outbox/(?P<slug>[-\w]+)/$', views.BoxListView.as_view(box='outbox') , name='condottieri_messages_outbox'),
    url(r'^delete/(?P<message_id>[\d]+)/$', views.delete, name='messages_delete'),
    url(r'^undelete/(?P<message_id>[\d]+)/$', views.undelete, name='messages_undelete'),
]
