from django.db import models


# Create your models here.

class Grade(models.Model):
    grade = models.CharField(max_length=50)
    point = models.FloatField()

    def __str__(self):
        return str(self.item)
