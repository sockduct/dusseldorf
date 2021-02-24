from django.test import TestCase
from django.urls import reverse

from .models import Area, Subject, Resource, ResourceType

# Create your tests here.
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
