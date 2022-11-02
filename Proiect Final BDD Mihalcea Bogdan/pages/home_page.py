from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from time import sleep


class Home_Page(Base_page):
    SEARCH_BOX = (By.ID, "keyword")
    SEARCH_BUTTON = (By.XPATH, '//button/i[@class="icon-search"]')
    MANUFACTURER_FILTER = (By.XPATH, "//div/a[@href='https://www.cel.ro/cauta/laptop+i7/dell/1j-1']")
    CLICK_SORTING_LIST = (By.ID, "sortare")
    DESCENDING_PRICE_FILTER = (By.XPATH, "//form/select/option[5]")
    PRICE =(By.CLASS_NAME, "price")
    ADD_TO_CHART = (By.CLASS_NAME,"buy-product hasCBF")
    NO_OF_RESULTS = (By.XPATH, "//*[@id='filters']/div[2]/div[2]/div[5]/a/span")

    def test_navigate_to_home_page(self):
        self.chrome.get('https://www.cel.ro/')

    def test_enter_search_criteria(self):
        self.chrome.find_element(*self.SEARCH_BOX).send_keys("laptop i7")
        sleep(1)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()
        sleep(2)

    def filter_after_manufacturer(self):
        self.chrome.find_element(*self.MANUFACTURER_FILTER).click()
        sleep(2)

    def open_sorting_options(self):
        self.chrome.find_element(*self.CLICK_SORTING_LIST).click()

    def filter_after_descending_price(self):
        self.chrome.find_element(*self.DESCENDING_PRICE_FILTER).click()
        sleep(2)

    def check_results(self):
        results = self.chrome.find_element(*self.NO_OF_RESULTS)
        results_x = results[0].text.replace('(','').replace(')','')
        assert int(results_x) >= 3
        sleep(3)

