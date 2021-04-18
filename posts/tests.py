from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from .models import Comment, Post, PostType, Tag
from .views import (
    CommentCreateView,
    CommentDeleteView,
    CommentEditView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostEditView,
    PostListView
)

# Create your tests here.
class PostListTests(TestCase):
    def setUp(self):
        # First setup database with models:
        self.testuser1 = 'testuser1'
        self.testemail1 = f'{self.testuser1}@localhost'
        self.testpass = 'testpass123'
        self.user1 = get_user_model().objects.create_user(
            username=self.testuser1,
            email=self.testemail1,
            password=self.testpass
        )

        self.testuser2 = 'testuser2'
        self.testemail2 = f'{self.testuser2}@localhost'
        self.testpass = 'testpass123'
        self.user2 = get_user_model().objects.create_user(
            username=self.testuser2,
            email=self.testemail2,
            password=self.testpass
        )

        self.testtag_name = 'example tag name'
        self.testtag_descr = 'example tag description'
        self.tag = Tag.objects.create(
            name=self.testtag_name,
            description=self.testtag_descr
        )

        self.testtype_name1 = 'Blog'
        self.testtype_descr1 = 'Blog description type'
        self.posttype1 = PostType.objects.create(
            name=self.testtype_name1,
            description=self.testtype_descr1
        )

        self.testtype_name2 = 'Article'
        self.testtype_descr2 = 'Article description type'
        self.posttype2 = PostType.objects.create(
            name=self.testtype_name2,
            description=self.testtype_descr2
        )

        # Tag and Comment:
        self.testtitle1 = 'Test Blog Post Title'
        self.testbody1 = 'A test blog post body...'
        self.post1 = Post.objects.create(
            type=self.posttype1,
            title=self.testtitle1,
            body=self.testbody1,
            author=self.user1
        )
        self.post1.tags.add(self.tag)

        self.testcbody1 = 'A test blog comment body...'
        self.comment1 = Comment.objects.create(
            body=self.testcbody1,
            author=self.user2,
            post=self.post1
        )

        # Comments only:
        self.testtitle2 = '2nd Test Blog Post Title'
        self.testbody2 = 'Second test blog post body...'
        self.post2 = Post.objects.create(
            type=self.posttype2,
            title=self.testtitle2,
            body=self.testbody2,
            author=self.user2
        )

        self.testcbody2 = '2nd test blog comment body...'
        self.comment2 = Comment.objects.create(
            body=self.testcbody2,
            author=self.user1,
            post=self.post2
        )

        self.testcbody3 = '3rd test blog comment body...'
        self.comment3 = Comment.objects.create(
            body=self.testcbody3,
            author=self.user1,
            post=self.post2
        )

        # Neither tag nor comment:
        self.testtitle3 = '3rd Test Blog Post Title'
        self.testbody3 = 'Third test blog post body...'
        self.post3 = Post.objects.create(
            # Check default type works - doesn't work in test framework
            # Seems to work fine outside of it...
            type=self.posttype1,
            title=self.testtitle3,
            body=self.testbody3,
            author=self.user1
        )

         # Then retrieve page:
        url = reverse('post_list')
        self.response = self.client.get(url)

    def test_post_str(self):
        post = Post(title='Example Post')
        self.assertEqual(str(post), post.title)

    def test_postlist_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_postlist_template(self):
        self.assertTemplateUsed(self.response, 'post_list.html')

    def test_postlist_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Posts')
        self.assertContains(self.response, self.testtitle1)
        self.assertContains(self.response, f'{self.testtype_name1} by {self.user1.username}')
        self.assertContains(self.response, self.testbody1)
        self.assertContains(self.response, self.tag.name)
        self.assertContains(self.response, '1 comment')

        self.assertContains(self.response, self.testtitle2)
        self.assertContains(self.response, f'{self.testtype_name2} by {self.user2.username}')
        self.assertContains(self.response, self.testbody2)
        self.assertContains(self.response, '2 comments')

        self.assertContains(self.response, self.testtitle3)
        self.assertContains(self.response, f'{self.testtype_name1} by {self.user1.username}')
        self.assertContains(self.response, self.testbody3)

    def test_postlist_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_postlist_url_resolves_postlistview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, PostListView.as_view().__name__)

'''
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

        # This should probably be a separate method
        # Some of the tests require a logged in user...
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

    def test_post_update_view_reverse(self):
        post_title = 'App Test Creation - Updated'
        post_body = 'This is an updated application test creation post...'

        response = self.client.post(reverse('post_edit', args='1'), {
            'type': self.posttype.id,
            'title': post_title,
            'body': post_body,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, post_title)
        self.assertEqual(Post.objects.last().body, post_body)

    def test_post_delete_view(self):
        response = self.client.get('/post/1/delete/')
        no_response = self.client.get('/post/1000000/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Delete Post')
        self.assertContains(response, self.testtitle)
        self.assertNotContains(response, 'Hi there! I should not be on the page.')
        self.assertTemplateUsed(response, 'post_delete.html')

    def test_post_delete_view_reverse(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)
'''
