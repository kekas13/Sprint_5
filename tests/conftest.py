import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Sprint_5 import urls, locators, data


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def registration(driver):
    driver.get(urls.url_regs)
    driver.find_element(By.XPATH, locators.TestLocators.input_name_locator).send_keys(data.reg_name)
    driver.find_element(By.XPATH, locators.TestLocators.input_email_locator).send_keys(data.reg_email)
    driver.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys(data.reg_password)
    driver.find_element(By.XPATH, locators.TestLocators.button_reg_locator).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.TestLocators.button_login_locator)))
    return driver


@pytest.fixture()
def auth(driver):
    driver.get(urls.url_login)
    driver.find_element(By.XPATH, locators.TestLocators.input_email_login_locator).send_keys(data.user_email)
    driver.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys(data.user_password)
    driver.find_element(By.XPATH, locators.TestLocators.button_login_locator).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, locators.TestLocators.header_locator)))
    return driver
