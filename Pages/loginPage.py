from selenium import webdriver



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username = '//*[@id="user-name"]'
        self.password = '//*[@id="password"]'
        self.login_btn = '//*[@id="login-button"]'
        self.logo_image = "//div[text()='Swag Labs']"
        self.login_error = '//*[@class="error-button"]'

    def login(self):

        self.fill_login_form('standard_user','secret_sauce')
        self.click_login_btn()

    def fill_login_form(self,username,password):
        self.driver.find_element_by_xpath(self.username).send_keys(username)
        self.driver.find_element_by_xpath(self.password).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element_by_xpath(self.login_btn).click()


    def wait_dashboard_load(self):
        self.driver.implicitly_wait(20)

    def login_verify(self):

        if "Sorry, this user has been banned." in self.driver.find_element_by_xpath(self.login_error).text :
            print('Sorry, this user has been banned')

    def logo_verify(self):
        assert self.driver.find_element_by_xpath("//div[text()='Swag Labs']").is_displayed(), "Logo Not available"