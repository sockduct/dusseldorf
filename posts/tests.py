from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .models import Post, PostType, Tag
from .views import AboutPageView, PostDetailView, PostListView

# Create your tests here.
class PostTests(TestCase):
    def setUp(self):
        self.testuser = 'testuser1'
        self.testemail = f'{self.testuser}@localhost'
        self.testpass = 'testpass123'
        self.testtype = 'Blog'
        self.testtag = 'example'
        self.testtitle = 'Test Blog Post'
        self.testbody = 'A test blog post...'

        self.user = get_user_model().objects.create_user(
            username=self.testuser,
            email=self.testemail,
            password=self.testpass
        )

        self.tag = Tag.objects.create(
            name=self.testtag
        )

        self.posttype = PostType.objects.create(
            name=self.testtype
        )

        self.post = Post.objects.create(
            type=self.posttype,
            title=self.testtitle,
            body=self.testbody,
            author=self.user
        )

        self.post.tags.add(self.tag)

    def test_string_representation(self):
        post = Post(title='Example Title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.type}', self.testtype)
        self.assertEqual(f'{self.post.title}', self.testtitle)
        self.assertEqual(f'{self.post.body}', self.testbody)
        self.assertEqual(f'{self.post.author}', self.testuser)
        self.assertEqual(f'{self.post.tags.first().name}', self.testtag)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.testbody)
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.testtitle)
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertTemplateUsed(response, 'post_detail.html')

class PostsPageTests(TestCase):
    def test_posts_home_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_posts_home_url_resolves_postlistview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, PostListView.as_view().__name__)

class AboutPageTests(TestCase):
    def setUp(self):
        url = reverse('about')
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, 'about.html')

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, 'About The Developer Nexus')

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve('/about/')
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)
