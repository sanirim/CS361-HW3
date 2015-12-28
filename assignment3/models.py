from django.db import models
from django.forms import ModelForm


class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    office_details = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    classroom = models.CharField(max_length=30)
    times = models.TimeField()
    teacher = models.ForeignKey(Teacher, blank=True)
    students = models.ManyToManyField('Student', blank=True)


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    courses = models.ManyToManyField('Course', through=Course.students.through, blank=True)
