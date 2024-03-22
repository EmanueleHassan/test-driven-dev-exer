"""In this module you write unit tests for the application.

You can write applications modules that you can reuse then across
different projects.
"""
from django.test import TestCase

# For testing Views - I.e. Controllers in the Model-View-Controller
# Framework.
from django.http import HttpRequest  
from lists.views import home_page

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/") 
        self.assertContains(response, "<title>To-Do lists</title>") # parses the response automatically
        self.assertContains(response, "<html>")
        self.assertContains(response, "</html>")


