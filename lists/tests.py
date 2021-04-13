from django.test import TestCase    ## This it’s an augmented version
                                    ## of the standard
                                    ## unittest.TestCase, with some
                                    ## additional Django-specific
                                    ## features, which we’ll discover
                                    ## over the next few chapters.

from django.urls import resolve
from lists.views import home_page 

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 2)

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')   ## check internally what view function
                               ## is associated with such route and
                               ## triggers view
        self.assertEqual(found.func, home_page)  ## check that resolve
                                                 ## finds a view
                                                 ## function called
                                                 ## home_page

