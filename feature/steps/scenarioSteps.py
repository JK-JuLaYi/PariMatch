from behave import given,when,then

from Pages.inventoryPage import InventoryPage
from Pages.loginPage import LoginPage


@given(u'I am on the Demo Login Page')
def step_login(context):
    context.driver.get('https://www.saucedemo.com/')

@when(u'I fill the account information for account StandardUser into the Username field and the Password field')
def step_fill_form(context):
    LoginPage(context.driver).fill_login_form(username='standard_user',password='secret_sauce')

@when(u'I fill the account information for account LockedOutUser into the Username field and the Password field')
def step_fill_form(context):
    LoginPage(context.driver).fill_login_form(username='locked_out_user',password='secret_sauce')

@when(u'I click the Login Button')
def step_click_login(context):
    LoginPage(context.driver).click_login_btn()

@then(u'I verify the Error Message contains the text "Sorry, this user has been banned."')
def step_locked_out_verify(context):
    LoginPage(context.driver).login_verify()



@given(u'I am on the inventory page')
def step_inventoryPage(context):
    step_login(context)
    InventoryPage(context.driver).verify_invontory()


@when(u'user sorts products from low price to high price')
def step_impl(context):
    InventoryPage(context.driver).filter_low_high()


@when(u'user adds lowest priced product')
def step_impl(context):
    InventoryPage(context.driver).pick_lowest()


@when(u'user clicks on cart')
def step_impl(context):
    InventoryPage(context.driver).goto_cart()


@when(u'user clicks on checkout')
def step_impl(context):
    InventoryPage(context.driver).checkout_cart()


@when(u'user enters first name {first_name}')
def step_impl(context,first_name):
    InventoryPage(context.driver).fill_info_first(first_name)


@when(u'user enters last name {last_name}')
def step_impl(context,last_name):
    InventoryPage(context.driver).fill_info_last(last_name)


@when(u'user enters zip code {zipcode}')
def step_impl(context,zipcode):
    InventoryPage(context.driver).fill_info_code(zipcode)


@when(u'user clicks Continue button')
def step_impl(context):
    InventoryPage(context.driver).continue_check_btn()


@then(u'I verify in Checkout overview page if the total amount for the added item is $8.63')
def step_impl(context):
    InventoryPage(context.driver).verify_total()


@when(u'user clicks Finish button')
def step_impl(context):
    InventoryPage(context.driver).finish()


@then(u'Thank You header is shown in Checkout Complete page')
def step_impl(context):
    InventoryPage(context.driver).thank_you()



@then(u'I am redirected to the Demo Main Page')
def step_wait_Dashboard(context):
    LoginPage(context.driver).wait_dashboard_load()


@then(u'I verify the App Logo exists')
def step_check_Logo(context):
    LoginPage(context.driver).logo_verify()
