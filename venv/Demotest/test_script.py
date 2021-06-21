import pytest
import selenium
import pytest_webdriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

#login case with valid credentials
@pytest.fixture()
def test_setup():
 global driver
 driver = webdriver.Chrome(executable_path="D://chromedriver_win32//chromedriver_win32//chromedriver.exe")
 driver.implicitly_wait(10)
 driver.maximize_window()
 yield
 driver.close()
 driver.quit()
 
def test_login(test_setup):
 driver.get("http://mca-management-admin.us-east-1.elasticbeanstalk.com/login")
 driver.find_element(By.ID, "vaadinLoginUsername").send_keys('admin')
 driver.find_element(By.ID,"vaadinLoginPassword").send_keys('admin')
 driver.find_element(By.XPATH, "/html/body/vaadin-vertical-layout/vaadin-login-form/vaadin-login-form-wrapper/form/vaadin-button").click()
 time.sleep(5)
 assert driver.find_element(By.CSS_SELECTOR, ("#tabs > vaadin-tab:nth-child(10) > a")).is_displayed()==True

 
 # logincase with valid username and invalid password
def test_invalidlogin(test_setup):
 driver.get("http://mca-management-admin.us-east-1.elasticbeanstalk.com/login")
 driver.find_element(By.ID, "vaadinLoginUsername").send_keys('admin')
 driver.find_element(By.ID, "vaadinLoginPassword").send_keys('ajay')
 driver.find_element(By.XPATH,
                     "/html/body/vaadin-vertical-layout/vaadin-login-form/vaadin-login-form-wrapper/form/vaadin-button").click()
 time.sleep(5)
 assert driver.find_element(By.XPATH, ("/html/body/vaadin-vertical-layout/vaadin-login-form")).is_displayed() == False



 
  
 
 







