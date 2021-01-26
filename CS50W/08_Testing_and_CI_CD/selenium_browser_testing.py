import os
import pathlib
import unittest

from selenium import webdriver

def file_as_uri(filename):
	return pathlib.Path(os.path.abspath(filename)).as_uri()

driver = webdriver.Chrome()

class WebPageTests(unittest.TestCase):
	
	def test_title(self):
		'''Title is as espected.'''
		driver.get(file_as_uri("FILENAME.html"))
		self.assertEqual(driver.title, "EXPECTED TITLE")

	def test_javascript_thingy_on_click(self):
		'''Test a javascript function'''
		driver.get(file_as_uri("FILENAME.html"))
		ELEMENT_NAME = driver.find_element_by_id("ELEMENT_ID")
		ELEMENT_NAME.click()
		self.assertEqual(driver.find_element_by_tag_name("h1").text, "EXPECTED RESULT")

	...


if __name__ == '__main__':
	unnittest.main()

