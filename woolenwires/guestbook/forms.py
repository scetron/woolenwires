from django import forms
from .models import Guest, GuestBookEntry

class GuestBookEntryForm(forms.Form):

    class Meta:
        model = GuestBookEntry
