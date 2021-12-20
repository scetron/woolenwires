from django.urls import path

from . import views

urlpatterns = [
    path('', views.GuestBookEntryView.as_view(), name='index'),
    path('sign-guestbook', views.GuestBookEntryAddView.as_view(), name='add_entry')
]