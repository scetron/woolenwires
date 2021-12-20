from django.forms import fields
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import GuestBookEntry

# Create your views here.

class GuestBookEntryView(ListView):
    
    queryset = GuestBookEntry.objects.all()

class GuestBookEntryAddView(CreateView):
    model = GuestBookEntry
    fields = ['knit_message', 'extra_message', 'email', 'name']
    