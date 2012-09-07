## Copyright (c) 2010 by Jose Antonio Martin <jantonio.martin AT gmail DOT com>
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU Affero General Public License as published by the
## Free Software Foundation, either version 3 of the License, or (at your option
## any later version.
##
## This program is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
## FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
## for more details.
##
## You should have received a copy of the GNU Affero General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/agpl.txt>.
##
## This license is also included in the file COPYING
##
## AUTHOR: Jose Antonio Martin <jantonio.martin AT gmail DOT com>

import django.forms as forms
from django.utils.translation import ugettext_lazy as _

import condottieri_messages.models as messages

class PlayerMultipleChoiceField(forms.ModelMultipleChoiceField):
	def label_from_instance(self, obj):
		try:
			label = obj.contender.country.name
		except:
			return super(PlayerMultipleChoiceField, self).label_from_instance(obj)
		else:
			if obj.is_excommunicated:
				label = ' '.join([label, unicode(_("(excommunicated)"))])
			return label

def letter_form_factory(sender_player, recipient_player):
	game = sender_player.game
	bcc_qs = game.player_set.exclude(user__isnull=True).exclude(id=sender_player.id).exclude(id=recipient_player.id)
	if sender_player.is_excommunicated:
		bcc_qs = bcc_qs.filter(is_excommunicated=True)
	else:
		if sender_player.may_excommunicate:
			bcc_qs = bcc_qs.exclude(is_excommunicated=True)
	
	class LetterForm(forms.ModelForm):
		bcc = PlayerMultipleChoiceField(queryset=bcc_qs, required=False,
			label=_("Additional recipients (Bcc)"))
		
		def __init__(self, sender_player, recipient_player, **kwargs):
			super(LetterForm, self).__init__(**kwargs)
			self.instance.sender_player = sender_player
			self.instance.recipient_player = recipient_player

		class Meta:
			model = messages.Letter
			fields = ('bcc', 'subject', 'body',)

	return LetterForm
