from django.test import TestCase
from django.urls import reverse
from jobs.models import Job

# Create your tests here.

class TestTemplates(TestCase):

    def test_portfolio_homepage(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'jobs/homepage.html')

    def test_joblist(self):
        response = self.client.get('/job/')
        self.assertTemplateUsed(response, 'jobs/home.html')

    def test_jobdetail(self):
        job = Job(image='pence.jpg', summary='This is a test')
        job.save()
        response = self.client.get(
            reverse('job:detail', args=(job.pk,))
        )
        self.assertTemplateUsed(response, 'jobs/detail.html')


class TestModel(TestCase):
    def test_job_model(self):
        job = Job()
        job.image = 'pence.jpg'
        job.summary = 'This is a test'
        job.save()
        saved_job = Job.objects.get(summary = 'This is a test')
        self.assertEqual(saved_job.image, 'pence.jpg')
