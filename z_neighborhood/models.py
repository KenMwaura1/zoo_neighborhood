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
    admin = models.ForeignKey("UserProfile", on_delete=models.CASCADE, related_name='hood', default=None)
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

    @classmethod
    def update_neighborhood(cls, id, name, location, population, description, police, health, education):
        cls.objects.filter(id=id).update(name=name, location=location, population=population, description=description,
                                         police=police, health=health, education=education)

    @classmethod
    def get_all_neighborhoods(cls):
        return cls.objects.all()

    @classmethod
    def get_neighborhood_by_name(cls, name):
        return cls.objects.filter(name=name)

    @classmethod
    def get_neighborhood_by_location(cls, location):
        return cls.objects.filter(location=location)

    @classmethod
    def get_neighborhood_by_population(cls, population):
        return cls.objects.filter(population=population)

    @classmethod
    def get_neighborhood_by_description(cls, description):
        return cls.objects.filter(description=description)

    @classmethod
    def get_neighborhood_by_police(cls, police):
        return cls.objects.filter(police=police)


class UserProfile(models.Model):
    """
    User Profile model
    """
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, default="default bio")
    location = models.CharField(max_length=30, blank=True, default="Umoja II", null=True)
    date_joined = models.DateField(auto_now_add=True, blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics', blank=True, null=True default='profile_pics/default.jpg')
    profile_pic = CloudinaryField('image',
                                  default="https://res.cloudinary.com/dd5ab8mp3/image/upload/v1634660213/image/upload/v1/images/profile/user.jpg")
    neighbourhood = models.ForeignKey(NeighborHood, on_delete=models.SET_NULL, null=True, related_name='members',
                                      blank=True)
    contact_email = models.EmailField(max_length=100, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()

    def __str__(self):
        return f'{self.user.username}: profile'

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_id(cls, id):
        return cls.objects.filter(id=id)

    @classmethod
    def get_profile_by_user(cls, user):
        return cls.objects.filter(user=user)

    @classmethod
    def get_profile_by_username(cls, username):
        return cls.objects.filter(username=username)

    @classmethod
    def get_profile_by_bio(cls, bio):
        return cls.objects.filter(bio=bio)

    @classmethod
    def get_profile_by_location(cls, location):
        return cls.objects.filter(location=location)

    @classmethod
    def get_profile_by_date_joined(cls, date_joined):
        return cls.objects.filter(date_joined=date_joined)


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, related_name='post_hood')

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    @classmethod
    def get_post_by_id(cls, id):
        return cls.objects.filter(id=id)

    @classmethod
    def get_post_by_user(cls, user):
        return cls.objects.filter(user=user)

    @classmethod
    def get_post_by_hood(cls, hood):
        return cls.objects.filter(hood=hood)

    @classmethod
    def get_post_by_title(cls, title):
        return cls.objects.filter(title=title)

    @classmethod
    def get_post_by_post(cls, post):
        return cls.objects.filter(post=post)

    @classmethod
    def get_post_by_date(cls, date):
        return cls.objects.filter(date=date)

    def delete_post(self):
        self.delete()


class Business(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(NeighborHood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='owner')
    business_logo = CloudinaryField('image')

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()

    @classmethod
    def get_business_by_id(cls, id):
        return cls.objects.filter(id=id)

    @classmethod
    def get_business_by_name(cls, name):
        return cls.objects.filter(name=name)

    @classmethod
    def get_business_by_email(cls, email):
        return cls.objects.filter(email=email)

    def __str__(self):
        return f'{self.name} Business'



