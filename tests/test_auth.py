from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Sprint_5 import urls, locators, data


class TestAuth:
    def test_auth_by_login_button_on_main_page(self, driver):
        driver.get(urls.url_main)
        driver.find_element(By.XPATH, locators.TestLocators.button_login_main_page_locator).click()
        driver.find_element(By.XPATH, locators.TestLocators.input_email_login_locator).send_keys(data.user_email)
        driver.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys(data.user_password)
        driver.find_element(By.XPATH, locators.TestLocators.button_login_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.header_locator)))
        assert driver.current_url == urls.url_main

    def test_auth_from_profile_on_main_page(self, driver):
        driver.get(urls.url_main)
        driver.find_element(By.XPATH, locators.TestLocators.button_go_to_profile_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_login_locator)))
        driver.find_element(By.XPATH, locators.TestLocators.input_email_login_locator).send_keys(data.user_email)
        driver.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys(data.user_password)
        driver.find_element(By.XPATH, locators.TestLocators.button_login_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.header_locator)))
        assert driver.current_url == urls.url_main

    def test_auth_by_login_button_on_registration_page(self, driver):
        driver.get(urls.url_regs)
        driver.find_element(By.XPATH, locators.TestLocators.button_login_alternate_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_login_locator)))
        driver.find_element(By.XPATH, locators.TestLocators.input_email_login_locator).send_keys(data.user_email)
        driver.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys(data.user_password)
        driver.find_element(By.XPATH, locators.TestLocators.button_login_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.header_locator)))
        assert driver.current_url == urls.url_main

    def test_auth_by_login_button_on_forgot_password_page(self, driver):
        driver.get(urls.url_forgot_password)
        driver.find_element(By.XPATH, locators.TestLocators.button_login_alternate_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_login_locator)))
        driver.find_element(By.XPATH, locators.TestLocators.input_email_login_locator).send_keys(data.user_email)
        driver.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys(data.user_password)
        driver.find_element(By.XPATH, locators.TestLocators.button_login_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.header_locator)))
        assert driver.current_url == urls.url_main

    def test_logout_from_account(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.button_go_to_profile_locator).click()
        WebDriverWait(auth, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_save_profile_locator)))
        auth.find_element(By.XPATH, locators.TestLocators.button_logout_locator).click()
        WebDriverWait(auth, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_login_locator)))
        assert auth.current_url == urls.url_login
