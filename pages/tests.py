from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from .views import (
    AboutPageView,
    ContactPageView,
    ErrorPageView,
    LeaderboardPageView,
    SuccessPageView
)

# Create your tests here.
# Use SimpleTestCase if no database access required
class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'The Developer Nexus - About')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)

# Use TestCase here as database access required:
class ContactPageView(TestCase):
    def setUp(self):
        url = reverse('contact')
        self.response = self.client.get(url)

        self.testuser = 'testuser'
        self.testemail = f'{self.testuser}@localhost'
        self.testpass = 'testpass123'

        self.user = get_user_model().objects.create_user(
            username=self.testuser,
            email=self.testemail,
            password=self.testpass
        )

    def test_contactpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_contactpage_template(self):
        self.assertTemplateUsed(self.response, 'contact.html')

    def test_contactpage_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Contact Us')

    def test_contactpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_contactpage_url_resolves_contactpageview(self):
        view = resolve('/contact/')
        self.assertEqual(view.func.__name__, ContactPageView.__name__)

    def test_contactpage_form_submission(self):
        self.client.login(email=self.testemail, password=self.testpass)
        response = self.client.post(reverse('contact'), {
            'subject': 'Test Form Submission',
            'message': 'This is a test form submission...'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('success'))

    def test_contactpage_form_submission_noauth(self):
        response = self.client.post(reverse('contact'), {
            'subject': 'Test Form Submission',
            'message': 'This is a test form submission...'
        })
        self.assertEqual(response.status_code, 401)

class ErrorPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('error')
        self.response = self.client.get(url)

    def test_errorpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_errorpage_template(self):
        self.assertTemplateUsed(self.response, 'error.html')

    def test_errorpage_contains_correct_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Error')

    def test_errorpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_errorpage_url_resolves_errorpageview(self):
        view = resolve('/error/')
        self.assertEqual(view.func.__name__, ErrorPageView.as_view().__name__)

class LeaderboardPageView(TestCase):
    def setUp(self):
        # First create users:
        self.username1 = 'gamma1'
        self.username2 = 'theta2'
        self.username3 = 'beta3'

        self.user1 = get_user_model().objects.create_user(
            username=self.username1,
            email='gamma1@localhost',
            password='testpass123'
        )
        self.user2 = get_user_model().objects.create_user(
            username=self.username2,
            email='theta2@localhost',
            password='testpass123'
        )
        self.user3 = get_user_model().objects.create_user(
            username=self.username3,
            email='beta3@localhost',
            password='testpass123'
        )

        # Then get web page:
        url = reverse('leaderboard')
        self.response = self.client.get(url)

        # Ideally would do test posts/comments too to check scoring functionality,
        # but I don't want to link to a separate application from this tests
        # module...

    def test_leaderboardpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_leaderboardpage_template(self):
        self.assertTemplateUsed(self.response, 'leaderboard.html')

    def test_leaderboardpage_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Leaderboard')
        # Ideally would also confirm entries are sorted correctly:
        self.assertContains(self.response, self.username1)
        self.assertContains(self.response, self.username2)
        self.assertContains(self.response, self.username3)

    def test_leaderboardpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_leaderboardpage_url_resolves_leaderboardpageview(self):
        view = resolve('/leaderboard/')
        self.assertEqual(view.func.__name__, LeaderboardPageView.__name__)

class SuccessPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse('success')
        self.response = self.client.get(url)

    def test_successpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_successpage_template(self):
        self.assertTemplateUsed(self.response, 'success.html')

    def test_successpage_contains_correct_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Success')

    def test_successpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_successpage_url_resolves_successpageview(self):
        view = resolve('/success/')
        self.assertEqual(view.func.__name__, SuccessPageView.as_view().__name__)
