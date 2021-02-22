from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import CustomUserCreationForm

# Create your tests here.
class CustomUserTests(TestCase):
    def test_create_user(self):
        testuser = 'testuser1'
        testemail = 'testuser1@localhost'
        testpass = 'testpass123'
        User = get_user_model()

        user = User.objects.create_user(username=testuser, email=testemail, password=testpass)
        self.assertEqual(user.username, testuser)
        self.assertEqual(user.email, testemail)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        testadmin = 'testadmin1'
        testemail = 'testadmin1@localhost'
        testpass = 'testpass456'
        User = get_user_model()

        user = User.objects.create_superuser(username=testadmin, email=testemail, password=testpass)
        self.assertEqual(user.username, testadmin)
        self.assertEqual(user.email, testemail)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
