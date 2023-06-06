from selenium.webdriver.support.select import Select

from Pages.driverManager import DriverManager
from Pages.loginPage import LoginPage


class InventoryPage:
    def __init__(self,driver):
        self.driver = driver
        self.filter = '//*[@class="product_sort_container"]'
        self.all_products = '//*[@class="inventory_list"]/div'
        self.add_to_cart = "//button[contains(text(),'Add to cart')]"
        self.cart = '//*[@class="shopping_cart_link"]'
        self.checkout = '//*[@name="checkout"]'


        self.first_name = '//*[@id="first-name"]'
        self.last_name = '//*[@id="last-name"]'
        self.postal_code = '//*[@id="postal-code"]'
        self.continue_checkout = '//*[@id="continue"]'
        self.total = "//*[contains(text(),'Total:')]"

        self.finish_btn = '//*[@name="finish"]'
        self.thank_header = '//*[@class="complete-header"]'


    def verify_invontory(self):
        LoginPage(self.driver).login()
        assert 'inventory' in self.driver.current_url, 'Not at invontory page'

    def filter_low_high(self):
        filter  = self.driver.find_element_by_xpath(self.filter)
        self.select = Select(filter)
        self.select.select_by_value('lohi')

    def pick_lowest(self):
        self.driver.find_element_by_xpath(self.all_products).find_element_by_xpath(self.add_to_cart).click()
    def goto_cart(self):
        self.driver.find_element_by_xpath(self.cart).click()

    def checkout_cart(self):
        # self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath(self.checkout).click()

    def fill_info_first(self,firstname):
        self.driver.find_element_by_xpath(self.first_name).send_keys(firstname)

    def fill_info_last(self, lastname):
        self.driver.find_element_by_xpath(self.last_name).send_keys(lastname)

    def fill_info_code(self, code):
        self.driver.find_element_by_xpath(self.postal_code).send_keys(code)

    def continue_check_btn(self):
        self.driver.find_element_by_xpath(self.continue_checkout).click()

    def verify_total(self):
        price = self.driver.find_element_by_xpath(self.total).text
        print(price.split('$')[1])
        assert float(price.split('$')[1]) == 8.63, f'Cart value is {price.split(":")[1]}'

    def finish(self):
        self.driver.find_element_by_xpath(self.finish_btn).click()

    def thank_you(self):
        assert 'Thank you' in self.driver.find_element_by_xpath(self.thank_header).text, "Un successful purchase"

