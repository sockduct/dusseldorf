from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .models import UserType

# Create your tests here.
class UserTypeTests(TestCase):
    # User type attributes:
    testname = 'SiteUsers'
    testdescr = 'General site user - no special privileges'

    def test_create_usertype(self):
        usertype = UserType.objects.create(name=self.testname, description=self.testdescr)

        self.assertEqual(usertype.name, self.testname)
        self.assertEqual(usertype.description, self.testdescr)

class CustomUserTests(TestCase):
    # User attributes:
    testuser = 'testuser1'
    testuser_name = 'Test User'
    testuser_nickname = 'Testy'
    testuser_email = 'testuser1@localhost'
    testuser_pass = 'testpass123'

    # Superuser attributes:
    testadmin = 'testadmin1'
    testadmin_email = 'testadmin1@localhost'
    testadmin_pass = 'testpass456'

    def setUp(self):
        # UserTypes:
        self.usertype_name = 'SiteUsers'
        self.usertype_descr = 'General site user - no special privileges'
        self.usertype = UserType.objects.create(
            name=self.usertype_name,
            description=self.usertype_descr
        )

        self.admintype_name = 'Administrators'
        self.admintype_descr = 'Site administrators - all privileges'
        self.admintype = UserType.objects.create(
            name=self.admintype_name,
            description=self.admintype_descr
        )

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username=self.testuser,
            email=self.testuser_email,
            password=self.testuser_pass,
            name=self.testuser_name,
            nickname=self.testuser_nickname,
            type=self.usertype
        )

        self.assertEqual(user.username, self.testuser)
        self.assertEqual(user.email, self.testuser_email)
        self.assertEqual(user.name, self.testuser_name)
        self.assertEqual(user.nickname, self.testuser_nickname)
        self.assertEqual(user.type, self.usertype)
        self.assertEqual(user.type.name, self.usertype_name)
        self.assertEqual(user.type.description, self.usertype_descr)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username=self.testadmin,
            email=self.testadmin_email,
            password=self.testadmin_pass,
            type=self.admintype
        )

        self.assertEqual(user.username, self.testadmin)
        self.assertEqual(user.email, self.testadmin_email)
        self.assertEqual(user.type, self.admintype)
        self.assertEqual(user.type.name, self.admintype_name)
        self.assertEqual(user.type.description, self.admintype_descr)
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

class SignupPageTests(TestCase):
    username = 'newuser'
    email = 'newuser@localhost'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign Up')
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_signup_template(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
