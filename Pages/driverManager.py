from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:
    def driver(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

        return self.driver
    def get_url(self,url):
        self.driver.get(url)



