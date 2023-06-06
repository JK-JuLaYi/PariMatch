from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from Pages.driverManager import DriverManager


def before_scenario(context, scenario):
    context.driver = DriverManager().driver()

def after_scenario(context, scenario):
    context.driver.quit()


