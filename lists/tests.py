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
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  # pass the request view to the controller.
        html = response.content.decode("utf8")  # extract content of the response
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.startswith("<html>"))  
        self.assertTrue(html.endswith("</html>"))  

    def test_home_page_returns_correct_html_2(self):
        response = self.client.get("/")  # simulates http request at root /
        self.assertContains(response, "<title>To-Do lists</title>") # parses the response automatically
