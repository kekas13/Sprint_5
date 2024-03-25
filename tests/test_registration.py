from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Sprint_5 import urls, locators, data


class TestRegistration:
    def test_successful_registration(self, registration):
        registration.find_element(By.XPATH, locators.TestLocators.input_email_login_locator).send_keys(data.reg_email)
        registration.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys(data.reg_password)
        registration.find_element(By.XPATH, locators.TestLocators.button_login_locator).click()
        WebDriverWait(registration, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.header_locator)))
        assert registration.current_url == urls.url_main

    def test_registration_check_error_for_wrong_password(self, driver):
        driver.get(urls.url_regs)
        driver.find_element(By.XPATH, locators.TestLocators.input_name_locator).send_keys(data.reg_name)
        driver.find_element(By.XPATH, locators.TestLocators.input_email_locator).send_keys(data.reg_email)
        driver.find_element(By.XPATH, locators.TestLocators.input_password_locator).send_keys('12345')
        driver.find_element(By.XPATH, locators.TestLocators.button_reg_locator).click()
        assert driver.find_element(By.CSS_SELECTOR, locators.TestLocators.error_text_locator).text == 'Некорректный пароль'
