from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .models import Post, PostType, Tag
from .views import (
    AboutPageView, PostCreateView, PostDeleteView,
    PostDetailView, PostEditView, PostListView
)

# Create your tests here.
class PostModelsTests(TestCase):
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

class PostPagesTests(TestCase):
    def setUp(self):
        self.testuser = 'testuser2'
        self.testemail = f'{self.testuser}@localhost'
        self.testpass = 'testpass123'
        self.testtype = 'Blog'
        self.testtag = 'Django'
        self.testtitle = 'Example Blog Post'
        self.testbody = 'An application testing blog post...'

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

        response = self.client.post('/accounts/login/', {
            'login': self.testemail,
            'password': self.testpass
        })
        self.assertEqual(response.status_code, 302)

    # Posts list view (home page):
    def test_posts_home_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_posts_home_url_resolves(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, PostListView.as_view().__name__)

    def test_post_list_view_reverse(self):
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

    def test_post_create_view(self):
        response = self.client.get('/post/new/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Post')
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertTemplateUsed(response, 'post_new.html')

    def test_post_create_view_reverse(self):
        post_title = 'App Test Creation'
        post_body = 'This is an application test creation post...'

        response = self.client.post(reverse('post_new'), {
            'type': self.posttype.id,
            'title': post_title,
            'body': post_body,
            'tags': self.tag.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().type.name, self.posttype.name)
        self.assertEqual(Post.objects.last().title, post_title)
        self.assertEqual(Post.objects.last().body, post_body)
        self.assertEqual(Post.objects.last().author.username, self.user.username)
        self.assertEqual(Post.objects.last().tags.first().name, self.tag.name)

    def test_post_update_view(self):
        response = self.client.get('/post/1/edit/')
        no_response = self.client.get('/post/1000000/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Edit Post')
        self.assertContains(response, self.testtitle)
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertTemplateUsed(response, 'post_edit.html')

    def test_post_delete_view(self):
        response = self.client.get('/post/1/delete/')
        no_response = self.client.get('/post/1000000/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Delete Post')
        self.assertContains(response, self.testtitle)
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertTemplateUsed(response, 'post_delete.html')

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
