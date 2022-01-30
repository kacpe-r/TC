from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TIMEOUT = 10

def wait_for_element_visible(browser, element):
    WebDriverWait(browser, TIMEOUT).until(EC.visibility_of_element_located(element))

def wait_for_element_to_be_clickable(browser, element):
    WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(element))

def wait_for_element_present(browser, element):
    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)
    WebDriverWait(browser, TIMEOUT, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(element))
