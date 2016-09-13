from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Iris(models.Model):
    sepal_length = models.FloatField()
    sepal_width = models.FloatField()
    petal_length = models.FloatField()
    petal_width = models.FloatField()
    species = models.CharField(max_length=11)

    def __str__(self):
        return self.species +\
               " - " + self.sepal_length +\
               " " + self.sepal_width +\
               " " + self.petal_length +\
               " " + self.petal_width


