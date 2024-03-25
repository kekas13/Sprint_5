from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Sprint_5 import urls, locators


class TestTransitions:
    def test_open_profile_page(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.button_go_to_profile_locator).click()
        WebDriverWait(auth, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_save_profile_locator)))
        assert auth.current_url == urls.url_profile

    def test_transition_by_constructor(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.button_go_to_profile_locator).click()
        WebDriverWait(auth, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_save_profile_locator)))
        auth.find_element(By.XPATH, locators.TestLocators.button_constructor_locator).click()
        WebDriverWait(auth, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.header_locator)))
        assert auth.current_url == urls.url_main

    def test_transition_by_logo(self, auth):
        auth.find_element(By.XPATH, locators.TestLocators.button_go_to_profile_locator).click()
        WebDriverWait(auth, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.button_save_profile_locator)))
        auth.find_element(By.XPATH, locators.TestLocators.button_logo_locator).click()
        WebDriverWait(auth, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.header_locator)))
        assert auth.current_url == urls.url_main
