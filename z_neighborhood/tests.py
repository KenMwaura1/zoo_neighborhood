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


class BusinessTestCase(TestCase):
    def setUp(self):
        self.user = User(username='zoo', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=17, user=self.user, )
        # self.profile.save()
        self.neighborhood = NeighborHood(name='Test Neighborhood', location='Test Location', population=0,
                                         description='Test Description', hood_logo='Test Image',
                                         police=254, health=254, education=254, )
        self.neighborhood.save()
        self.business = Business(name='Test Business', email="zootest@test.com", description='Test Description',
                                 neighbourhood=self.neighborhood,
                                 business_logo='Test Image', user=self.profile, )
        self.business.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        NeighborHood.objects.all().delete()
        Business.objects.all().delete()
        self.user.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save()
        after = Business.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_business(self):
        self.business.save()
        self.business.delete()
        after = Business.objects.all()
        self.assertTrue(len(after) == 0)

    def test_business_name(self):
        self.assertEqual(self.business.name, 'Test Business')

    def test_business_email(self):
        self.assertEqual(self.business.email, 'zootest@test.com')

    def test_business_description(self):
        self.assertEqual(self.business.description, 'Test Description')

    def test_business_logo(self):
        self.assertEqual(self.business.business_logo, 'Test Image')

    def test_business_neighborhood(self):
        self.assertEqual(self.business.neighbourhood, self.neighborhood)

    def test_business_user(self):
        self.assertEqual(self.business.user, self.profile)


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User(username='zoo', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=17, user=self.user, )
        self.neighborhood = NeighborHood(name='Test Neighborhood', location='Test Location', population=0,
                                         description='Test Description', hood_logo='Test Image',
                                         police=254, health=254, education=254, )
        self.neighborhood.save()
        self.post = Post(title='Test Post', post='Test Content', user=self.profile, hood=self.neighborhood, )
        self.post.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        Post.objects.all().delete()
        self.user.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save()

    def test_delete_post(self):
        self.post.save()

    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_content(self):
        self.assertEqual(self.post.post, 'Test Content')

    def test_post_user(self):
        self.assertEqual(self.post.user, self.profile)

    def test_post_hood(self):
        self.assertEqual(self.post.hood, self.neighborhood)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username='zoo', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=17, user=self.user, )
        self.profile_pic = "https://res.cloudinary.com/dd5ab8mp3/image/upload/v1634660213/image/upload/v1/images/profile/user.jpg"
        self.bio = "default bio"
        self.neighborhood = NeighborHood(name='Test Neighborhood', location='Test Location', population=0,
                                         description='Test Description', hood_logo='Test Image',
                                         police=254, health=254, education=254, )
        self.neighborhood.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        NeighborHood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))

    def test_save_profile(self):
        self.profile.create_profile()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile.create_profile()
        self.user.delete()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) == 0)

    def test_profile_user(self):
        self.assertEqual(self.profile.user, self.user)

    def test_profile_neighborhood(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood, self.neighborhood)

    def test_profile_image(self):
        self.assertEqual(self.profile.profile_pic, self.profile_pic)

    def test_profile_bio(self):
        self.assertEqual(self.profile.bio, self.bio)

    def test_profile_hood(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood, self.neighborhood)

    def test_profile_hood_name(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.name, self.neighborhood.name)

    def test_profile_hood_location(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.location, self.neighborhood.location)

    def test_profile_hood_population(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.population, self.neighborhood.population)

    def test_profile_hood_description(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.description, self.neighborhood.description)

    def test_profile_hood_logo(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.hood_logo, self.neighborhood.hood_logo)

    def test_profile_hood_police(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.police, self.neighborhood.police)

    def test_profile_hood_health(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.health, self.neighborhood.health)

    def test_profile_hood_education(self):
        self.profile.neighbourhood = self.neighborhood
        self.assertEqual(self.profile.neighbourhood.education, self.neighborhood.education)









