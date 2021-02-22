from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post, PostType, Tag

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
        self.assertEqual(f'{self.post.title}', self.testtitle)
        self.assertEqual(f'{self.post.author}', self.testuser)
        self.assertEqual(f'{self.post.body}', self.testbody)

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.testbody)
        self.assertTemplateUsed(response, 'post_list.html')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.testtitle)
        self.assertTemplateUsed(response, 'post_detail.html')
