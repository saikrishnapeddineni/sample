from django.db import models

class student(models.Model):
    name=models.CharField(max_length=500)
    fathername=models.CharField(max_length=500)
    contactnum=models.IntegerField()
    classname=models.CharField(max_length=500)
