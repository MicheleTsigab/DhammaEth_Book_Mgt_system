from gettext import install
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from core.models import Author,Language,Book,Instance, Member
import datetime

class TestModels(TestCase):
    """Tests for the models"""
class TestView(TestCase):
    def test_anonymous_cannot_add_book(self):
        """test that unauthenticated user can't add books"""
        response = self.client.get(reverse("add-book"))
        self.assertRedirects(response, f"/accounts/login/?next={reverse('add-book')}")
    def test_instance_creation(self):
        """assert that book instances can be created by num_copies in add-book view"""
        user = User.objects.create_user("username", "example@gmail.com", "some_pass")
        self.client.force_login(user=user)
        data = {
            "title": "the art of living{datetime.date}",
            "copies": "3",
        }
        response = self.client.post(reverse("add-book"), data=data)
        book=Book.objects.get(title='the art of living{datetime.date}')
        num_instance=book.instance_set.count()
        self.assertEqual(num_instance, 3)
    def test_boook_lend(self):
        """book lending view working?"""
        user = User.objects.create_user("username", "example@gmail.com", "some_pass")
        self.client.force_login(user=user)
        book=Book.objects.create(title='test-title')
        instance=Instance.objects.create(book=book)
        borrower=Member.objects.create(first_name='test-bf',last_name='test-bl')
        date=datetime.datetime.now().date()
        data={

            "book":book.pk,
            "borrower":borrower.pk,
            "returned_date":date,
            "borrowed_date":date,
        }
        response=self.client.post(reverse('lend-instance', args=[instance.pk]),data=data)
        instance.refresh_from_db()
        borrowed_date_from_db=instance.borrowed_date
        print(instance.borrower)
        self.assertEqual(borrowed_date_from_db,date)
        self.assertEqual(response.status_code,302)