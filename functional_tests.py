import unittest
from selenium import webdriver


class NewVisitorTest(unittest.TestCase):  

    # setUp and tearDown are special methods which get run before and
    # after each test. I’m using them to start and stop our browser.
    def setUp(self):  
        self.browser = webdriver.Firefox()  

    def tearDown(self):  
        self.browser.quit()


    # Any method whose name starts with test_ is a test
    # in the unittest package
    def test_can_start_a_todo_list(self):  
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")  

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)  

        # self.fail just fails no matter what, producing the error
        # message given. I’m using it as a reminder to finish the
        # test.
        self.fail("Finish the test!")  

        [...]

        # Satisfied, she goes back to sleep

# We call unittest.main(), which launches the unittest test runner,
# which will automatically find test classes and methods in the file
# and run them.
if __name__ == "__main__":  
    unittest.main()  
