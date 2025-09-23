from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=15, primary_key=True)
    password = models.CharField(max_length=15)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=50, null=True)
    lastname = models.CharField(max_length=50)
    type_user = (("S", "Student"), ("T", "Teacher"))
    type = models.CharField(max_length=1, choices=type_user, default="S")

    def __str__(self):
        return self.username + ' ' + self.firstname + ' ' + self.middlename + ' ' + self.lastname

class Student(Account):
    course = models.CharField(max_length=15)
    year = models.IntegerField(default=1)
    department = models.CharField(max_length=15)

class Teacher(Account):
    age = models.IntegerField(default=0)