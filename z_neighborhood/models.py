from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class NeighborHood(models.Model):
    """
    Neighborhood model
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    population = models.IntegerField()
    admin = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name='hood')
    hood_logo = CloudinaryField('image')
    description = models.TextField()
    police = models.IntegerField()
    health = models.IntegerField()
    education = models.IntegerField()

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

