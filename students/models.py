from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=200)
    date_of_birth = models.DateTimeField()
    student_class = models.IntegerField('Class')
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
    
class Group(models.Model):
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.name
