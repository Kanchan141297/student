from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=50)
    school = models.TextField()
    marks = models.DecimalField(max_digits=5,decimal_places=2)