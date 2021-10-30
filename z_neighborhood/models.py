from django.db import models


# Create your models here.
class Neighborhood(models.Model):
    """
    Neighborhood model
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.IntegerField()
    police = models.IntegerField()
    health = models.IntegerField()
    education = models.IntegerField()

    def __str__(self):
        return self.name

