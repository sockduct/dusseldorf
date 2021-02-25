from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .forms import CustomUserCreationForm
from .views import SignupPageView

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

class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'registration/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_signup_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_signup_view(self):
        view = resolve('/accounts/signup/')
        self.assertEqual(view.func.__name__, SignupPageView.as_view().__name__)
