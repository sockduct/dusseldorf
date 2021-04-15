import uuid

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

    def test_area_str(self):
        area = Area(name='Example Area')
        self.assertEqual(str(area), area.name)

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
        self.resource1 = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.testresourceurl2 = "https://www.example.com/resource2"
        self.resource2 = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl2
        )

        self.testresourcename3 = "Test Resource 3"
        self.testresourcedescr3 = "Test Resource Description 3"
        self.testresourceurl3 = "https://www.example.com/resource3"
        self.resource3 = Resource.objects.create(
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
        url4 = reverse('path_detail', args=[str(uuid.uuid4())])
        self.response4 = self.client.get(url4)
        self.response5 = self.client.get('/paths/area/1/')

    def test_areadetail_status_code1(self):
        self.assertEqual(self.response1.status_code, 200)

    def test_areadetail_status_code2(self):
        self.assertEqual(self.response4.status_code, 404)

    def test_areadetail_status_code3(self):
        self.assertEqual(self.response5.status_code, 404)

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
        self.resource1 = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.testresourceurl2 = "https://www.example.com/resource2"
        self.resource2 = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl2
        )

        self.testresourcename3 = "Test Resource 3"
        self.testresourcedescr3 = "Test Resource Description 3"
        self.testresourceurl3 = "https://www.example.com/resource3"
        self.resource3 = Resource.objects.create(
            name=self.testresourcename3,
            description=self.testresourcedescr3,
            subject=self.subject2,
            type=self.resource_type,
            url=self.testresourceurl3
        )

        # Then retrieve pages:
        url = reverse('subject_list')
        self.response = self.client.get(url)

    def test_subject_str(self):
        subject = Subject(name='Example Subject')
        self.assertEqual(str(subject), subject.name)

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
        self.resource1 = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.testresourceurl2 = "https://www.example.com/resource2"
        self.resource2 = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            subject=self.subject1,
            type=self.resource_type,
            url=self.testresourceurl2
        )

        self.testresourcename3 = "Test Resource 3"
        self.testresourcedescr3 = "Test Resource Description 3"
        self.resource3 = Resource.objects.create(
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
        url4 = reverse('subject_detail', args=[str(uuid.uuid4())])
        self.response4 = self.client.get(url4)
        self.response5 = self.client.get('/paths/subject/1/')

    def test_subjectdetail_status_code1(self):
        self.assertEqual(self.response1.status_code, 200)

    def test_subjectdetail_status_code2(self):
        self.assertEqual(self.response4.status_code, 404)

    def test_subjectdetail_status_code3(self):
        self.assertEqual(self.response5.status_code, 404)

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
        self.resource1 = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.resource2 = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            type=self.resource_type
        )

        # Then retrieve pages:
        url = reverse('resource_list')
        self.response = self.client.get(url)

    def test_resource_str(self):
        resource = Resource(name='Example Resource')
        self.assertEqual(str(resource), resource.name)

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

class ResourceDetailTests(TestCase):
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
        self.resource1 = Resource.objects.create(
            name=self.testresourcename1,
            description=self.testresourcedescr1,
            type=self.resource_type,
            url=self.testresourceurl1
        )

        self.testresourcename2 = "Test Resource 2"
        self.testresourcedescr2 = "Test Resource Description 2"
        self.resource2 = Resource.objects.create(
            name=self.testresourcename2,
            description=self.testresourcedescr2,
            type=self.resource_type
        )

        # Then retrieve pages:
        url1 = reverse('resource_detail', args=[str(self.resource1.id)])
        self.response1 = self.client.get(url1)
        url2 = reverse('resource_detail', args=[str(self.resource2.id)])
        self.response2 = self.client.get(url2)
        url3 = reverse('subject_detail', args=[str(uuid.uuid4())])
        self.response3 = self.client.get(url3)
        self.response4 = self.client.get('/paths/subject/1/')

    def test_resourcedetail_status_code1(self):
        self.assertEqual(self.response1.status_code, 200)

    def test_resourcedetail_status_code2(self):
        self.assertEqual(self.response3.status_code, 404)

    def test_resourcedetail_status_code3(self):
        self.assertEqual(self.response4.status_code, 404)

    def test_resourcedetail_template(self):
        self.assertTemplateUsed(self.response1, 'resource_detail.html')

    def test_resource1detail_contains_html(self):
        self.assertContains(self.response1, 'The Developer Nexus - Resource Detail')
        self.assertContains(self.response1, self.testresourcename1)
        self.assertContains(self.response1, f'Type {self.testresource_typename}')
        self.assertContains(self.response1, self.testresourcedescr1)
        self.assertContains(self.response1, f'<a href="{self.testresourceurl1}">Additional '
                                             'resource information</a> (External Site)')

    def test_resource2detail_contains_html(self):
        self.assertContains(self.response2, 'The Developer Nexus - Resource Detail')
        self.assertContains(self.response2, self.testresourcename2)
        self.assertContains(self.response2, f'Type {self.testresource_typename}')
        self.assertContains(self.response2, self.testresourcedescr2)
        self.assertNotContains(self.response2, 'Additional resource information')

    def test_resourcedetail_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response1, 'Hi there! I should not be on the page.')

    def test_resourcedetail_url_resolves_resourcedetailview(self):
        view = resolve(f'/paths/resource/{self.resource1.id}/')
        self.assertEqual(view.func.__name__, ResourceDetailView.as_view().__name__)
