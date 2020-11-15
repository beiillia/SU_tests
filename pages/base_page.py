from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator, time_out=TIMEOUT):
        WebDriverWait(self.driver, time_out).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text, time_out=TIMEOUT):
        WebDriverWait(self.driver, time_out).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator, time_out=TIMEOUT):
        element = WebDriverWait(self.driver, time_out).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator, time_out=TIMEOUT):
        element = WebDriverWait(self.driver, time_out).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title, time_out=TIMEOUT):
        WebDriverWait(self.driver, time_out).until(ec.title_is(title))
        return self.driver.title

  #  def usec_connection(self):