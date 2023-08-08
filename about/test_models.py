from django.test import TestCase
from django.db import models
from .models import About


class TestAboutModel(TestCase):

    def setUp(self):
        self.aboutmodel = About.objects.create(title='TestModel')
