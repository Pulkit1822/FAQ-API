from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(null=True, blank=True)
    answer_hi = RichTextField(null=True, blank=True)
    question_bn = models.TextField(null=True, blank=True)
    answer_bn = RichTextField(null=True, blank=True)

    def get_translated_text(self, lang='en'):
        if lang == 'hi':
            return self.question_hi, self.answer_hi
        elif lang == 'bn':
            return self.question_bn, self.answer_bn
        else:
            return self.question, self.answer

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)
