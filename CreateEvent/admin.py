from django.contrib import admin

from CreateEvent.models import Event, Room, AttendEvent

# Register your models here.
admin.site.register(Room)
admin.site.register(Event)
admin.site.register(AttendEvent)