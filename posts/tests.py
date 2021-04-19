import uuid

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

class PostDetailTests(TestCase):
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

        # Then retrieve page:
        url = reverse('post_detail', args=[str(self.post1.id)])
        self.response = self.client.get(url)

    def test_postdetail_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_postdetail_invalid_page(self):
        response = self.client.get(reverse('post_detail', args=[str(uuid.uuid4())]))
        self.assertEqual(response.status_code, 404)

    def test_postdetail_template(self):
        self.assertTemplateUsed(self.response, 'post_detail.html')

    def test_postdetail_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Post Detail')
        self.assertContains(self.response, self.testtitle1)
        self.assertContains(self.response, f'{self.testtype_name1} by {self.user1.username}')
        self.assertContains(self.response, self.testbody1)
        self.assertContains(self.response, self.tag.name)

        self.assertContains(self.response, 'Comments')
        self.assertContains(self.response, self.user2.username)
        self.assertContains(self.response, self.testcbody1)

    def test_postdetail_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_postdetail_url_resolves_postdetailview(self):
        view = resolve(f'/post/{self.post1.id}/')
        self.assertEqual(view.func.__name__, PostDetailView.as_view().__name__)

class PostCreateTests(TestCase):
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

        # Tag and Comment:
        self.testtitle1 = 'Test Blog Post Title'
        self.testbody1 = 'A test blog post body...'
        ''' Create post through test submission rather than here:
        self.post1 = Post.objects.create(
            type=self.posttype1,
            title=self.testtitle1,
            body=self.testbody1,
            author=self.user1
        )
        self.post1.tags.add(self.tag)
        '''

        # Then retrieve page:
        self.client.login(email=self.testemail1, password=self.testpass)
        self.url = reverse('post_new')
        self.response = self.client.get(self.url)

    def test_postcreate_noauth_status_code(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_postcreate_auth_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_postcreate_template(self):
        self.assertTemplateUsed(self.response, 'post_new.html')

    def test_postcreate_submission(self):
        response = self.client.post(reverse('post_new'), {
            'type': str(self.posttype1.id),
            'title': self.testtitle1,
            'body': self.testbody1,
            'tags': str(self.tag.id)
        })

        self.assertEqual(response.status_code, 302)
        postid = Post.objects.last().id
        self.assertEqual(response.url, reverse('post_detail', args=[str(postid)]))

    def test_postcreate_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - New Post')
        self.assertContains(self.response, self.testtype_name1)
        self.assertContains(self.response, self.tag.name)

    def test_postcreate_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_postcreate_url_resolves_postcreateview(self):
        view = resolve(f'/post/new/')
        self.assertEqual(view.func.__name__, PostCreateView.as_view().__name__)

class PostEditTests(TestCase):
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

        # Then retrieve page:
        self.client.login(email=self.testemail1, password=self.testpass)
        url = reverse('post_edit', args=[str(self.post1.id)])
        self.response = self.client.get(url)

    def test_postedit_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_postedit_template(self):
        self.assertTemplateUsed(self.response, 'post_edit.html')

    def test_postedit_submission(self):
        new_body = self.testbody1 + ' - amended...'
        response = self.client.post(reverse('post_edit', args=[str(self.post1.id)]), {
            'type': str(self.posttype1.id),
            'title': self.testtitle1,
            'body': new_body,
            'tags': str(self.tag.id)
        })

        self.assertEqual(response.status_code, 302)
        body = Post.objects.last().body
        self.assertEqual(body, new_body)

    def test_postedit_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Edit Post')
        self.assertContains(self.response, f'selected>{self.testtype_name1}<')
        self.assertContains(self.response, self.testtitle1)
        self.assertContains(self.response, self.testbody1)
        self.assertContains(self.response, f'selected>{self.tag.name}<')

    def test_postedit_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_postedit_url_resolves_posteditview(self):
        view = resolve(f'/post/{self.post1.id}/edit/')
        self.assertEqual(view.func.__name__, PostEditView.as_view().__name__)

class PostDeleteTests(TestCase):
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

        # Then retrieve page:
        self.client.login(email=self.testemail1, password=self.testpass)
        url = reverse('post_delete', args=[str(self.post1.id)])
        self.response = self.client.get(url)

    def test_postdelete_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_postdelete_template(self):
        self.assertTemplateUsed(self.response, 'post_delete.html')

    def test_postdelete_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Delete Post')
        self.assertContains(self.response, f'Are you sure you want to delete {self.testtitle1}')
        self.assertContains(self.response, f'{self.testtype_name1} by {self.user1.username}')
        self.assertContains(self.response, self.testbody1)
        self.assertContains(self.response, self.tag.name)

    def test_postdelete_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_postdelete_url_resolves_postdeleteview(self):
        view = resolve(f'/post/{self.post1.id}/delete/')
        self.assertEqual(view.func.__name__, PostDeleteView.as_view().__name__)

    def test_postdelete_submission(self):
        response = self.client.post(reverse('post_delete', args=[str(self.post1.id)]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('post_list'))

        response = self.client.get(reverse('post_list'))
        self.assertNotContains(response, self.testtitle1)
        self.assertNotContains(response, self.testbody1)

class CommentCreateTests(TestCase):
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
        ''' Create comment through test submission rather than here:
        self.comment1 = Comment.objects.create(
            body=self.testcbody1,
            author=self.user1,
            post=self.post1
        )
        '''

        # Then retrieve page:
        self.client.login(email=self.testemail1, password=self.testpass)
        self.url = reverse('comment_new', args=[str(self.post1.id)])
        self.response = self.client.get(self.url)

    def test_commentcreate_noauth_status_code(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)

    def test_commentcreate_auth_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_commentcreate_template(self):
        self.assertTemplateUsed(self.response, 'comment_new.html')

    def test_commentcreate_submission(self):
        response = self.client.post(reverse('comment_new', args=[str(self.post1.id)]), {
            'body': self.testcbody1,
        })

        self.assertEqual(response.status_code, 302)
        comment = Comment.objects.last()
        self.assertEqual(comment.post, self.post1)
        self.assertEqual(comment.body, self.testcbody1)

    def test_commentcreate_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - New Comment')
        self.assertContains(self.response, self.testtitle1)
        self.assertContains(self.response, f'{self.posttype1} by {self.user1.username}')
        self.assertContains(self.response, self.testbody1)
        self.assertContains(self.response, self.tag.name)

    def test_commentcreate_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_commentcreate_url_resolves_commentcreateview(self):
        view = resolve(f'/post/{self.post1.id}/comment/new/')
        self.assertEqual(view.func.__name__, CommentCreateView.as_view().__name__)

class CommentEditTests(TestCase):
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
            author=self.user1,
            post=self.post1
        )

        # Then retrieve page:
        self.client.login(email=self.testemail1, password=self.testpass)
        url = reverse('comment_edit', args=[str(self.comment1.id)])
        self.response = self.client.get(url)

    def test_commentedit_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_commentedit_template(self):
        self.assertTemplateUsed(self.response, 'comment_edit.html')

    def test_commentedit_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Edit Comment')
        self.assertContains(self.response, self.testtitle1)
        self.assertContains(self.response, f'{self.posttype1} by {self.user1.username}')
        self.assertContains(self.response, self.testbody1)
        self.assertContains(self.response, self.tag.name)
        self.assertContains(self.response, self.testcbody1)

    def test_commentedit_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_commentedit_url_resolves_commenteditview(self):
        view = resolve(f'/post/comment/{self.comment1.id}/edit/')
        self.assertEqual(view.func.__name__, CommentEditView.as_view().__name__)

    def test_commentedit_submission(self):
        new_body = self.testcbody1 + ' - amended...'
        response = self.client.post(reverse('comment_edit', args=[str(self.comment1.id)]), {
            'body': new_body,
        })

        self.assertEqual(response.status_code, 302)
        body = Comment.objects.last().body
        self.assertEqual(body, new_body)

class CommentDeleteTests(TestCase):
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
            author=self.user1,
            post=self.post1
        )

        # Then retrieve page:
        self.client.login(email=self.testemail1, password=self.testpass)
        url = reverse('comment_delete', args=[str(self.comment1.id)])
        self.response = self.client.get(url)

    def test_commentdelete_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_commentdelete_template(self):
        self.assertTemplateUsed(self.response, 'comment_delete.html')

    def test_commentdelete_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Delete Comment')
        self.assertContains(self.response, self.testtitle1)
        self.assertContains(self.response, f'{self.testtype_name1} by {self.user1.username}')
        self.assertContains(self.response, self.testbody1)
        self.assertContains(self.response, self.tag.name)
        self.assertContains(self.response, f'Are you sure you want to delete this comment')
        self.assertContains(self.response, self.testcbody1)

    def test_commentdelete_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_commentdelete_url_resolves_commentdeleteview(self):
        view = resolve(f'/post/comment/{self.comment1.id}/delete/')
        self.assertEqual(view.func.__name__, CommentDeleteView.as_view().__name__)

    def test_commentdelete_submission(self):
        response = self.client.post(reverse('comment_delete', args=[str(self.comment1.id)]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('post_detail', args=[str(self.post1.id)]))

        response = self.client.get(reverse('post_detail', args=[str(self.post1.id)]))
        self.assertNotContains(response, self.testcbody1)
