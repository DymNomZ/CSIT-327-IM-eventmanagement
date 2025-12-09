from django.db import models
from User.models import Teacher, Student

# Create your models here.

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    room_name = models.CharField(max_length=15)

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=100)
    date_of_event = models.DateField()
    max_participants = models.IntegerField(default=0)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=1)
    student = models.ManyToManyField(Student, related_name="attend", through="AttendEvent")

    def __str__(self):
        return self.event_title + '. Date of Event: ' + str(self.date_of_event)

class AttendEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date_registered = models.DateField()
