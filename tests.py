import os
import pathlib
import unittest

from selenium import webdriver

def file_uri(filename):
    return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome('C:\\Users\\mykeltuz\\Downloads\\Programs\\chromedriver') # change this path to run this test on your device.

class WebpageTests(unittest.TestCase):

    def test_title(self):
        driver.get(file_uri("draw.html"))
        self.assertEqual(driver.title, "Draw")
    
    def test_body(self):
        driver.get(file_uri("draw.html"))
        body = driver.find_element_by_tag_name("body")
        self.assertEqual(body.value_of_css_property("color"), "rgba(128, 0, 128, 1)")

    def test_container(self):
        driver.get(file_uri("draw.html"))
        svg = driver.find_element_by_tag_name("svg")
        self.assertEqual(svg.value_of_css_property("color"), "rgba(255, 255, 255, 1)")

if __name__ == "__main__":
    unittest.main()