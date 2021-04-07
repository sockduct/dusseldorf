from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from .views import AboutPageView, ContactPageView

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
