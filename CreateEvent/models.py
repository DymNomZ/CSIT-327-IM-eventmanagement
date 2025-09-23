from django.db import models
from User.models import Teacher, Student

# Create your models here.

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=15)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=50)
    date_of_event = models.DateField()
    max_participants = models.IntegerField()

    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)

    student = models.ManyToManyField(Student, through="AttendEvent")

class AttendEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.RESTRICT)
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    status = models.BooleanField(default=False)
    date_registered = models.DateField()
