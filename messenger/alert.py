# Author: Paul Molina
# Date: Sept 2018
# Version: 0.1
#
# This package uses Selenium to send an alert message to a potentially-troubled
# user on Tumblr.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def alertUser(target_user):
	driver = webdriver.Firefox()
	driver.get("https://www.tumblr.com")

	# Login Process
	login_button = driver.find_element_by_id('signup_login_button')
	login_button.click()

	# Username and Password
	username = 'pmoli004@fiu.edu'
	password = 'ShellHacks2018'

	# Puts in the username and goes to the next screen
	id_box = driver.find_element_by_id('signup_determine_email')
	id_box.send_keys(username)
	next_button = driver.find_element_by_id('signup_forms_submit')
	next_button.click()

	# Password Logic
	time.sleep(1) # allows scrolling to occur
	use_password = driver.find_element_by_class_name('chrome.magiclink_password_container')
	use_password.click()
	password_box = driver.find_element_by_id('signup_password')
	password_box.send_keys(password)

	# Logs User In
	login_button = driver.find_element_by_id('signup_forms_submit')
	login_button.click()

	# Gets message box open
	driver.get('https://' + target_user +  '.tumblr.com')
	driver.get('https://www.tumblr.com/message/' + target_user)

	time.sleep(5)

	# Sends desired user a message
	user_message_box = driver.find_element_by_class_name('text-input')
	user_message_box.send_keys("Based on your latest posts we think you might be going through a tough time...\n")
	
	time.sleep(3)
	user_message_box.send_keys("If you are, please don't hesitate to contact a volunteer trained in crisis intervention.\n")
	
	time.sleep(3)
	user_message_box.send_keys("You can talk to one at www.iamalive.org\n")
	
	time.sleep(3)
	user_message_box.send_keys("Or you could also do it anonymously at www.7cups.com\n")

	time.sleep(3)
	user_message_box.send_keys("Remember... You are not alone!\n")