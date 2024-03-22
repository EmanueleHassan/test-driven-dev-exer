import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


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

        # Checks that the To-DO string is in the header 1 html cell
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text  
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, "id_new_item")  
        self.assertEqual(inputbox.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        inputbox.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1) 
        
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")  
        self.assertTrue(any(row.text == "1: Buy peacock feathers" for row in rows))
        
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
