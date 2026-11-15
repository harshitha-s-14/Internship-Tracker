from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Application
from datetime import date


class ApplicationTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='user1',
            password='testpass123'
        )

        self.user2 = User.objects.create_user(
            username='user2',
            password='testpass123'
        )

        self.application = Application.objects.create(
            user=self.user1,
            company_name='Infosys',
            role='Python Developer',
            location='Bangalore',
            application_date=date.today(),
            status='A'
        )

    def test_user_login(self):
        response = self.client.login(
            username='user1',
            password='testpass123'
        )
        self.assertTrue(response)

    def test_dashboard_access(self):
        self.client.login(username='user1', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_user_sees_only_own_applications(self):
        self.client.login(username='user2', password='testpass123')
        response = self.client.get(reverse('dashboard'))
        self.assertNotContains(response, 'Infosys')

    def test_application_belongs_to_correct_user(self):
        self.assertEqual(self.application.user, self.user1)

    def test_application_creation(self):
        application = Application.objects.create(
            user=self.user2,
            company_name='TCS',
            role='Software Developer',
            location='Bangalore',
            application_date=date.today(),
            status='A'
        )

        self.assertEqual(application.company_name, 'TCS')
        self.assertEqual(application.user, self.user2)

    def test_application_deletion(self):
        application_id = self.application.id
        self.application.delete()

        self.assertFalse(
            Application.objects.filter(id=application_id).exists()
        )
    def test_application_editing(self):
        self.client.login(username='user1', password='testpass123')

        response = self.client.post(
            reverse('edit_application', args=[self.application.id]),
            {
                'company_name': 'Wipro',
                'role': 'Python Developer',
                'location': 'Bangalore',
                'application_date': date.today().isoformat(),
                'status': 'A',
                'notes': 'Updated application'
            }
        )

        self.assertEqual(response.status_code, 302)

        self.application.refresh_from_db()
        self.assertEqual(self.application.company_name, 'Wipro')

    def test_user_cannot_edit_others_application(self):
        self.client.login(username='user2', password='testpass123')

        response = self.client.get(
            reverse('edit_application', args=[self.application.id])
        )

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_delete_others_application(self):
        self.client.login(username='user2', password='testpass123')

        response = self.client.post(
            reverse('delete_application', args=[self.application.id])
        )

        self.assertEqual(response.status_code, 404)
        self.assertTrue(
            Application.objects.filter(id=self.application.id).exists()
        )

    def test_unauthenticated_user_cannot_access_dashboard(self):
        response = self.client.get(reverse('dashboard'))

        self.assertEqual(response.status_code, 302)