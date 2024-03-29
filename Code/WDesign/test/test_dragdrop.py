# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestDragdrog():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(20)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_dragdrog(self):
    self.driver.get("http://localhost:3300/")
    self.driver.set_window_size(1047, 605)
    dragged = WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/nav/div/div/div/table/tr[7]/td[2]/p')))
    dropped = WebDriverWait(self.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div')))
    # dropped = self.driver.find_element(By.CSS_SELECTOR, ".in-element")
    actions = ActionChains(self.driver)
    actions.drag_and_drop(dragged, dropped).perform()
  
    if __name__ == '__main__':
      pytest.main()