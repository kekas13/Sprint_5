from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from Sprint_5 import urls, locators


class TestConstructorTabs:
    def test_constructor_switch_tab_to_sauce(self, driver):
        driver.get(urls.url_main)
        driver.find_element(By.XPATH, locators.TestLocators.tab_sauce_locator).click()
        assert (driver.find_element(By.XPATH, locators.TestLocators.scroll_sauce_locator) and
                driver.find_element(By.XPATH, locators.TestLocators.header_sauce_locator))

    def test_constructor_switch_tab_to_fillings(self, driver):
        driver.get(urls.url_main)
        driver.find_element(By.XPATH, locators.TestLocators.tab_fillings_locator).click()
        assert (driver.find_element(By.XPATH, locators.TestLocators.scroll_fillings_locator) and
                driver.find_element(By.XPATH, locators.TestLocators.header_fillings_locator))

    def test_constructor_switch_tab_to_buns(self, driver):
        driver.get(urls.url_main)
        driver.find_element(By.XPATH, locators.TestLocators.tab_fillings_locator).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locators.TestLocators.scroll_fillings_locator)))
        driver.find_element(By.XPATH, locators.TestLocators.tab_buns_locator).click()
        assert (driver.find_element(By.XPATH, locators.TestLocators.scroll_buns_locator) and
                driver.find_element(By.XPATH, locators.TestLocators.header_buns_locator))
