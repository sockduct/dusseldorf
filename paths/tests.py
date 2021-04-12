from django.test import TestCase
from django.urls import resolve, reverse

from .models import Area, Subject, Resource, ResourceType
from .views import (
    AreaListView,
    AreaDetailView,
    SubjectListView,
    SubjectDetailView,
    ResourceListView,
    ResourceDetailView
)

# Create your tests here.
class AreaListTests(TestCase):
    def setUp(self):
        # First setup database with models:
        self.testareaname1 = "Test Area 1"
        self.testareadescr1 = "Test Area 1 Description"
        self.area1 = Area.objects.create(
            name=self.testareaname1,
            description=self.testareadescr1
        )

        self.testareaname2 = "Test Area 2"
        self.testareadescr2 = "Test Area 2 Description"
        self.area2 = Area.objects.create(
            name=self.testareaname2,
            description=self.testareadescr2
        )

        self.testareaname3 = "Test Area 3"
        self.testareadescr3 = "Test Area 3 Description"
        self.area3 = Area.objects.create(
            name=self.testareaname3,
            description=self.testareadescr3
        )

        self.testsubjectname1 = "Test Subject 1"
        self.testsubjectdescr1 = "Test Subject 1 Description"
        self.subject1 = Subject.objects.create(
            name=self.testsubjectname1,
            description=self.testsubjectdescr1,
            area=self.area1
        )

        self.testsubjectname2 = "Test Subject 2"
        self.testsubjectdescr2 = "Test Subject 2 Description"
        self.subject2 = Subject.objects.create(
            name=self.testsubjectname2,
            description=self.testsubjectdescr2,
            area=self.area1
        )

        self.testsubjectname3 = "Test Subject 3"
        self.testsubjectdescr3 = "Test Subject 3 Description"
        self.subject3 = Subject.objects.create(
            name=self.testsubjectname3,
            description=self.testsubjectdescr3,
            area=self.area2
        )

        self.testresource_typename = "Test Resource Type"
        self.testresource_typedescr = "Test Resource Type Description"
        self.resource_type = ResourceType.objects.create(
            name=self.testresource_typename,
            description=self.testresource_typedescr
        )

        self.testresourcename = "Test Resource"
        self.testresourcedescr = "Test Resource Description"
        self.testresourceurl = "https://www.example.com/resource"
        self.resource = Resource.objects.create(
            name=self.testresourcename,
            description=self.testresourcedescr,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl
        )

        # Then retrieve page:
        url = reverse('path_list')
        self.response = self.client.get(url)

    def test_arealist_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_arealist_template(self):
        self.assertTemplateUsed(self.response, 'path_list.html')

    def test_arealist_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Paths')
        self.assertContains(self.response, self.testareaname1)
        self.assertContains(self.response, self.testareadescr1)
        self.assertContains(self.response, '2 supporting subjects')
        self.assertContains(self.response, self.testareaname2)
        self.assertContains(self.response, self.testareadescr2)
        self.assertContains(self.response, '1 supporting subject')
        self.assertContains(self.response, self.testareaname3)
        self.assertContains(self.response, self.testareadescr3)
        self.assertContains(self.response, 'No supporting subjects')

    def test_arealist_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_arealist_url_resolves_arealistview(self):
        view = resolve('/paths/')
        self.assertEqual(view.func.__name__, AreaListView.as_view().__name__)

class AreaDetailTests(TestCase):
    def setUp(self):
        # First setup database with models:
        self.testareaname1 = "Test Area 1"
        self.testareadescr1 = "Test Area 1 Description"
        self.area1 = Area.objects.create(
            name=self.testareaname1,
            description=self.testareadescr1
        )

        self.testareaname2 = "Test Area 2"
        self.testareadescr2 = "Test Area 2 Description"
        self.area2 = Area.objects.create(
            name=self.testareaname2,
            description=self.testareadescr2
        )

        self.testareaname3 = "Test Area 3"
        self.testareadescr3 = "Test Area 3 Description"
        self.area3 = Area.objects.create(
            name=self.testareaname3,
            description=self.testareadescr3
        )

        self.testsubjectname1 = "Test Subject 1"
        self.testsubjectdescr1 = "Test Subject 1 Description"
        self.subject1 = Subject.objects.create(
            name=self.testsubjectname1,
            description=self.testsubjectdescr1,
            area=self.area1
        )

        self.testsubjectname2 = "Test Subject 2"
        self.testsubjectdescr2 = "Test Subject 2 Description"
        self.subject2 = Subject.objects.create(
            name=self.testsubjectname2,
            description=self.testsubjectdescr2,
            area=self.area1
        )

        self.testsubjectname3 = "Test Subject 3"
        self.testsubjectdescr3 = "Test Subject 3 Description"
        self.subject3 = Subject.objects.create(
            name=self.testsubjectname3,
            description=self.testsubjectdescr3,
            area=self.area2
        )

        self.testresource_typename = "Test Resource Type"
        self.testresource_typedescr = "Test Resource Type Description"
        self.resource_type = ResourceType.objects.create(
            name=self.testresource_typename,
            description=self.testresource_typedescr
        )

        self.testresourcename1 = "Test Resource 1"
        self.testresourcedescr1 = "Test Resource Description 1"
        self.testresourceurl1 = "https://www.example.com/resource1"
        self.resource = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.testresourceurl2 = "https://www.example.com/resource2"
        self.resource = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl2
        )

        self.testresourcename3 = "Test Resource 3"
        self.testresourcedescr3 = "Test Resource Description 3"
        self.testresourceurl3 = "https://www.example.com/resource3"
        self.resource = Resource.objects.create(
            name=self.testresourcename3,
            description=self.testresourcedescr3,
            subject=self.subject2,
            type=self.resource_type,
            url=self.testresourceurl3
        )

        # Then retrieve pages:
        url1 = reverse('path_detail', args=[str(self.area1.id)])
        self.response1 = self.client.get(url1)
        url2 = reverse('path_detail', args=[str(self.area2.id)])
        self.response2 = self.client.get(url2)
        url3 = reverse('path_detail', args=[str(self.area3.id)])
        self.response3 = self.client.get(url3)

    def test_areadetail_status_code(self):
        self.assertEqual(self.response1.status_code, 200)

    def test_areadetail_template(self):
        self.assertTemplateUsed(self.response1, 'path_detail.html')

    def test_area1detail_contains_html(self):
        self.assertContains(self.response1, 'The Developer Nexus - Path Detail')
        self.assertContains(self.response1, self.testareaname1)
        self.assertContains(self.response1, self.testareadescr1)
        self.assertContains(self.response1, 'Supporting Subjects')
        self.assertContains(self.response1, self.testsubjectname1)
        self.assertContains(self.response1, '2 supporting resources')
        self.assertContains(self.response1, self.testsubjectname2)
        self.assertContains(self.response1, '1 supporting resource')

    def test_area2detail_contains_html(self):
        self.assertContains(self.response2, 'The Developer Nexus - Path Detail')
        self.assertContains(self.response2, self.testareaname2)
        self.assertContains(self.response2, self.testareadescr2)
        self.assertContains(self.response2, 'Supporting Subject')
        self.assertContains(self.response2, self.testsubjectname3)
        self.assertContains(self.response2, 'No supporting resources')

    def test_area3detail_contains_html(self):
        self.assertContains(self.response3, 'The Developer Nexus - Path Detail')
        self.assertContains(self.response3, self.testareaname3)
        self.assertContains(self.response3, self.testareadescr3)
        self.assertContains(self.response3, 'No supporting subjects')

    def test_areadetail_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response1, 'Hi there! I should not be on the page.')

    def test_areadetail_url_resolves_areadetailview(self):
        view = resolve(f'/paths/area/{self.area1.id}/')
        self.assertEqual(view.func.__name__, AreaDetailView.as_view().__name__)

class SubjectListTests(TestCase):
    def setUp(self):
        # First setup database with models:
        self.testsubjectname1 = "Test Subject 1"
        self.testsubjectdescr1 = "Test Subject 1 Description"
        self.subject1 = Subject.objects.create(
            name=self.testsubjectname1,
            description=self.testsubjectdescr1,
        )

        self.testsubjectname2 = "Test Subject 2"
        self.testsubjectdescr2 = "Test Subject 2 Description"
        self.subject2 = Subject.objects.create(
            name=self.testsubjectname2,
            description=self.testsubjectdescr2,
        )

        self.testsubjectname3 = "Test Subject 3"
        self.testsubjectdescr3 = "Test Subject 3 Description"
        self.subject3 = Subject.objects.create(
            name=self.testsubjectname3,
            description=self.testsubjectdescr3,
        )

        self.testresource_typename = "Test Resource Type"
        self.testresource_typedescr = "Test Resource Type Description"
        self.resource_type = ResourceType.objects.create(
            name=self.testresource_typename,
            description=self.testresource_typedescr
        )

        self.testresourcename1 = "Test Resource 1"
        self.testresourcedescr1 = "Test Resource Description 1"
        self.testresourceurl1 = "https://www.example.com/resource1"
        self.resource = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.testresourceurl2 = "https://www.example.com/resource2"
        self.resource = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl2
        )

        self.testresourcename3 = "Test Resource 3"
        self.testresourcedescr3 = "Test Resource Description 3"
        self.testresourceurl3 = "https://www.example.com/resource3"
        self.resource = Resource.objects.create(
            name=self.testresourcename3,
            description=self.testresourcedescr3,
            subject=self.subject2,
            type=self.resource_type,
            url=self.testresourceurl3
        )

        # Then retrieve pages:
        url = reverse('subject_list')
        self.response = self.client.get(url)

    def test_subjectlist_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_subjectlist_template(self):
        self.assertTemplateUsed(self.response, 'subject_list.html')

    def test_subjectlist_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Subjects')
        self.assertContains(self.response, self.testsubjectname1)
        self.assertContains(self.response, self.testsubjectdescr1)
        self.assertContains(self.response, '2 supporting resources')
        self.assertContains(self.response, self.testsubjectname2)
        self.assertContains(self.response, self.testsubjectdescr2)
        self.assertContains(self.response, '1 supporting resource')
        self.assertContains(self.response, self.testsubjectname3)
        self.assertContains(self.response, self.testsubjectdescr3)
        self.assertContains(self.response, 'No supporting resources')

    def test_subjectlist_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_subjectlist_url_resolves_subjectlistview(self):
        view = resolve('/paths/subjects/')
        self.assertEqual(view.func.__name__, SubjectListView.as_view().__name__)

class SubjectDetailTests(TestCase):
    def setUp(self):
        # First setup database with models:
        self.testsubjectname1 = "Test Subject 1"
        self.testsubjectdescr1 = "Test Subject 1 Description"
        self.subject1 = Subject.objects.create(
            name=self.testsubjectname1,
            description=self.testsubjectdescr1,
        )

        self.testsubjectname2 = "Test Subject 2"
        self.testsubjectdescr2 = "Test Subject 2 Description"
        self.subject2 = Subject.objects.create(
            name=self.testsubjectname2,
            description=self.testsubjectdescr2,
        )

        self.testsubjectname3 = "Test Subject 3"
        self.testsubjectdescr3 = "Test Subject 3 Description"
        self.subject3 = Subject.objects.create(
            name=self.testsubjectname3,
            description=self.testsubjectdescr3,
        )

        self.testresource_typename = "Test Resource Type"
        self.testresource_typedescr = "Test Resource Type Description"
        self.resource_type = ResourceType.objects.create(
            name=self.testresource_typename,
            description=self.testresource_typedescr
        )

        self.testresourcename1 = "Test Resource 1"
        self.testresourcedescr1 = "Test Resource Description 1"
        self.testresourceurl1 = "https://www.example.com/resource1"
        self.resource = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.testresourceurl2 = "https://www.example.com/resource2"
        self.resource = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl2
        )

        self.testresourcename3 = "Test Resource 3"
        self.testresourcedescr3 = "Test Resource Description 3"
        self.resource = Resource.objects.create(
            name=self.testresourcename3,
            description=self.testresourcedescr3,
            subject=self.subject2,
            type=self.resource_type
        )

        # Then retrieve pages:
        url1 = reverse('subject_detail', args=[str(self.subject1.id)])
        self.response1 = self.client.get(url1)
        url2 = reverse('subject_detail', args=[str(self.subject2.id)])
        self.response2 = self.client.get(url2)
        url3 = reverse('subject_detail', args=[str(self.subject3.id)])
        self.response3 = self.client.get(url3)

    def test_subjectdetail_status_code(self):
        self.assertEqual(self.response1.status_code, 200)

    def test_subjectdetail_template(self):
        self.assertTemplateUsed(self.response1, 'subject_detail.html')

    def test_subject1detail_contains_html(self):
        self.assertContains(self.response1, 'The Developer Nexus - Subject Detail')
        self.assertContains(self.response1, self.testsubjectname1)
        self.assertContains(self.response1, self.testsubjectdescr1)
        self.assertContains(self.response1, 'Supporting Resources')
        self.assertContains(self.response1, self.testresourcename1)
        self.assertContains(self.response1, 'Includes external link')
        self.assertContains(self.response1, self.testresourcename2)

    def test_subject2detail_contains_html(self):
        self.assertContains(self.response2, 'The Developer Nexus - Subject Detail')
        self.assertContains(self.response2, self.testsubjectname2)
        self.assertContains(self.response2, self.testsubjectdescr2)
        self.assertContains(self.response2, 'Supporting Resource')
        self.assertContains(self.response2, self.testresourcename3)
        self.assertNotContains(self.response2, 'Includes external link')

    def test_subject3detail_contains_html(self):
        self.assertContains(self.response3, 'The Developer Nexus - Subject Detail')
        self.assertContains(self.response3, self.testsubjectname3)
        self.assertContains(self.response3, self.testsubjectdescr3)
        self.assertContains(self.response3, 'No supporting resources')

    def test_subjectdetail_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response1, 'Hi there! I should not be on the page.')

    def test_subjectdetail_url_resolves_subjectdetailview(self):
        view = resolve(f'/paths/subject/{self.subject1.id}/')
        self.assertEqual(view.func.__name__, SubjectDetailView.as_view().__name__)

class ResourceListTests(TestCase):
    def setUp(self):
        # First setup database with models:
        self.testresource_typename = "Test Resource Type"
        self.testresource_typedescr = "Test Resource Type Description"
        self.resource_type = ResourceType.objects.create(
            name=self.testresource_typename,
            description=self.testresource_typedescr
        )

        self.testresourcename1 = "Test Resource 1"
        self.testresourcedescr1 = "Test Resource Description 1"
        self.testresourceurl1 = "https://www.example.com/resource1"
        self.resource = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.resource = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            type=self.resource_type
        )

        # Then retrieve pages:
        url = reverse('resource_list')
        self.response = self.client.get(url)

    def test_resourcelist_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_resourcelist_template(self):
        self.assertTemplateUsed(self.response, 'resource_list.html')

    def test_resourcelist_contains_html(self):
        self.assertContains(self.response, 'The Developer Nexus - Resources')
        self.assertContains(self.response, self.testresourcename1)
        self.assertContains(self.response, f'Type {self.testresource_typename}')
        self.assertContains(self.response, self.testresourcedescr1)
        self.assertContains(self.response, 'Additional resource information</a> (External Site)')
        self.assertContains(self.response, self.testresourcename2)
        self.assertContains(self.response, self.testresourcedescr2)
        self.assertContains(self.response, 'No additional resource information')

    def test_resourcelist_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')

    def test_resourcelist_url_resolves_resourcelistview(self):
        view = resolve('/paths/resources/')
        self.assertEqual(view.func.__name__, ResourceListView.as_view().__name__)

# class ResourceDetailTests(TestCase):
'''
class PathTests(TestCase):
    def setUp(self):
        self.testarea = 'Software Development Fundamentals'
        self.testsubject = 'Programming'
        self.testresource = 'Introduction to Programming'
        self.testtype = 'Book'
        self.testurl = 'http://www.example.com/introtoprogramming'

        self.area = Area.objects.create(name=self.testarea)
        self.subject = Subject.objects.create(name=self.testsubject, area=self.area)
        self.restype = ResourceType.objects.create(name=self.testtype)
        self.resource = Resource.objects.create(
            name=self.testresource,
            subject=self.subject,
            type=self.restype,
            url=self.testurl
        )

    def test_string_representation(self):
        path = Area(name='Example Area')
        self.assertEqual(str(path), path.name)

    def test_path_content(self):
        self.assertEqual(f'{self.resource.url}', self.testurl)
        self.assertEqual(f'{self.resource.type}', self.testtype)
        self.assertEqual(f'{self.resource.subject}', self.testsubject)
        self.assertEqual(f'{self.resource.name}', self.testresource)

        self.assertEqual(f'{self.restype.name}', self.testtype)
        self.assertEqual(f'{self.subject.name}', self.testsubject)
        self.assertEqual(f'{self.area.name}', self.testarea)

    def test_path_list_view(self):
        response = self.client.get(reverse('path_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.testarea)
        self.assertContains(response, '1 supporting subjects')
        self.assertTemplateUsed(response, 'path_list.html')

    def test_path_detail_view(self):
        response = self.client.get('/paths/area/1/')
        no_response = self.client.get('/paths/area/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.testarea)
        self.assertTemplateUsed(response, 'path_detail.html')

    def test_subject_list_view(self):
        response = self.client.get(reverse('subject_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.testsubject)
        self.assertContains(response, '1 supporting resources')
        self.assertTemplateUsed(response, 'subject_list.html')

    def test_subject_detail_view(self):
        response = self.client.get('/paths/subject/1/')
        no_response = self.client.get('/paths/subject/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.testsubject)
        self.assertTemplateUsed(response, 'subject_detail.html')

    def test_resource_list_view(self):
        response = self.client.get(reverse('resource_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.testresource)
        self.assertContains(response, 'Additional Resource Information')
        self.assertTemplateUsed(response, 'resource_list.html')

    def test_resource_detail_view(self):
        response = self.client.get('/paths/resource/1/')
        no_response = self.client.get('/paths/resource/1000000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, self.testresource)
        self.assertTemplateUsed(response, 'resource_detail.html')
'''
