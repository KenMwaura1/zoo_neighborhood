from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import NeighborHood, UserProfile, Business, Post


# Create your tests here.

def test_home_page_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEquals(response.status_code, 200)


class NeighborhoodTestCase(TestCase):
    def setUp(self):
        self.user = User(username='zoo', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=15, user=self.user, )
        # self.profile.create_profile()
        self.neighborhood = NeighborHood(name='Test Neighborhood', location='Test Location', population=0,
                                         description='Test Description', hood_logo='Test Image', admin=self.profile,
                                         police=254, health=254, education=254, )
        # self.neighborhood.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        NeighborHood.objects.all().delete()
        self.user.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))

    def test_save_profile(self):
        self.profile.create_profile()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_save_neighborhood(self):
        self.neighborhood.save()
        after = NeighborHood.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_neighborhood(self):
        self.neighborhood.save()
        self.neighborhood.delete()
        after = NeighborHood.objects.all()
        self.assertTrue(len(after) == 0)

    def test_neighborhood_name(self):
        self.assertEqual(self.neighborhood.name, 'Test Neighborhood')

    def test_neighborhood_location(self):
        self.assertEqual(self.neighborhood.location, 'Test Location')

    def test_neighborhood_population(self):
        self.assertEqual(self.neighborhood.population, 0)

    def test_neighborhood_population_increment(self):
        self.neighborhood.population = 1

        self.neighborhood.save()
        self.assertEqual(self.neighborhood.population, 1)

    def test_neighborhood_population_decrement(self):
        self.neighborhood.population = 1
        self.neighborhood.save()
        self.neighborhood.population = 0
        self.neighborhood.save()
        self.assertEqual(self.neighborhood.population, 0)

    def test_neighborhood_description(self):
        self.assertEqual(self.neighborhood.description, 'Test Description')

    def test_neighborhood_logo(self):
        self.assertEqual(self.neighborhood.hood_logo, 'Test Image')

    def test_neighborhood_police(self):
        self.assertEqual(self.neighborhood.police, 254)

    def test_neighborhood_health(self):
        self.assertEqual(self.neighborhood.health, 254)












