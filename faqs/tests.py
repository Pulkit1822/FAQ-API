from django.test import TestCase
from .models import FAQ
from rest_framework.test import APIClient
from rest_framework import status

class FAQModelTest(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is your name?",
            answer="My name is John Doe."
        )

    def test_faq_creation(self):
        self.assertEqual(self.faq.question, "What is your name?")
        self.assertEqual(self.faq.answer, "My name is John Doe.")

    def test_faq_translation(self):
        question_hi, answer_hi = self.faq.get_translated_text(lang='hi')
        question_bn, answer_bn = self.faq.get_translated_text(lang='bn')
        self.assertIsNotNone(question_hi)
        self.assertIsNotNone(answer_hi)
        self.assertIsNotNone(question_bn)
        self.assertIsNotNone(answer_bn)

class FAQAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="What is your name?",
            answer="My name is John Doe."
        )

    def test_get_faqs_default_language(self):
        response = self.client.get('/api/faqs/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['question'], "What is your name?")
        self.assertEqual(response.data[0]['answer'], "My name is John Doe.")

    def test_get_faqs_hindi(self):
        response = self.client.get('/api/faqs/?lang=hi')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data[0]['question'])
        self.assertIsNotNone(response.data[0]['answer'])

    def test_get_faqs_bengali(self):
        response = self.client.get('/api/faqs/?lang=bn')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data[0]['question'])
        self.assertIsNotNone(response.data[0]['answer'])
