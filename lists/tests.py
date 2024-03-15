"""In this module you write unit tests for the application.

You can write applications modules that you can reuse then across
different projects.
"""
from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
