'''#Write the feature files
I would write the feature files login.feature and order.feature based on the acceptance criteria provided:
# login.feature
Feature: Login
  As a customer who is not locked out
  I need to be able to log in
  So that I can purchase merchandise

Scenario: 1 Successful Login
  Given I am on the DemoLogin Page
  When I fill the account information for account StandardUser into the Username field and the Password field
  And I click the Login Button
  Then I am redirected to the Demo Main Page
  And I verify the App Logo exists

Scenario: 2 Failed Login
  Given I am on the DemoLogin Page
  When I fill the account information for account LockedOutUser into the Username field and the Password field
  And I click the Login Button
  Then I verify the Error Message contains the text "Sorry, this user has been banned. "

# order.feature
Feature: Order a product
  As a customer
  I need to be able to order a product
  So that I can purchase merchandise

Scenario: 3 Order a product
  Given I am on the inventory page
  When user sorts products from high price to low price
  And user adds highest priced product
  And user clicks on cart
  And user clicks on checkout
  And user enters first name Alice
  And user enters last name Doe
  And user enters zip code 592
  And user clicks Continue button
  Then I verify in Checkout overview page if the total amount for the added item is $49.99
  When user clicks Finish button
  Then Thank You header is shown in Checkout Complete page'''

#Write the step definitions
I would write the step definitions in login_steps.py and order_steps.py files:

# login_steps.py
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I am on the DemoLogin Page")
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")

@when("I fill the account information for account {account} into the Username field and the Password field")
def step_impl(context, account):
    username = context.accounts[account]["username"]
    password = context.accounts[account]["password"]
    context.driver.find_element_by_name("user-name").send_keys(username)
    context.driver.find_element_by_name("password").send_keys(password)

@when("I click the Login Button")
def step_impl(context):
    context.driver.find_element_by_name("login-button").click()

@then("I am redirected to the Demo Main Page")
def step_impl(context):
    assert context.driver.title == "Swag Labs"

@then("I verify the App Logo exists")
def step_impl(context):
    assert context.driver.find_element_by_css_selector(".app_logo").is_displayed()

@then("I verify the Error Message contains the text {error_message}")
def step_impl(context, error_message):
    assert error_message in context.driver.find_element_by_css_selector(".error-message").text

# order_steps.py
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given("I am on the inventory page")
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/inventory.html")

@when("user sorts products from high price to low price")
def step_impl(context):
    context.driver.find_element_by_css_selector(".product_sort_container").click()
    context.driver.find_element_by_css_selector(".product_sort_container option[value='hilo']").click()

@when("user adds highest priced product")
def step_impl(context):
    products = context.driver.find_elements_by_css_selector(".inventory_item")
    products[0].find_element_by_css_selector(".btn_primary").click()

@when("user clicks on cart")
def step_impl(context):
    context.driver.find_element_by_css_selector(".shopping_cart_link").click()

@when("user clicks on checkout")
def step_impl(context):
    context.driver.find_element_by_css_selector(".checkout_button").click()

@when("user enters first name {first_name}")
def step_impl(context, first_name):
    context.driver.find_element_by_name("first-name").send_keys(first_name)

@when("user enters last name {last_name}")
def step_impl(context, last_name):
    context.driver.find_element_by_name("last-name").send_keys(last_name)

@when("user enters zip code {zip_code}")
def step_impl(context, zip_code):
    context.driver.find_element_by_name("postal-code").send_keys(zip_code)

@when("user clicks Continue button")
def step_impl(context):
    context.driver.find_element_by_name("continue").click()

@then("I verify in Checkout overview page if the total amount for the added item is ${total_amount}")
def step_impl(context, total_amount):
    assert context.driver.find_element_by_css_selector(".summary_subtotal_label").text == total_amount

@when("user clicks Finish button")
def step_impl(context):
    context.driver.find_element_by_name("finish").click()

@then("Thank You header is shown in Checkout Complete page")
def step_impl(context):
    assert context.driver.find_element_by_css_selector(".complete-header").text == "Thank you for your order"

#Write the environment file
I would write the environment.py file to set up the Selenium WebDriver and define the accounts:

from selenium import webdriver

def before_all(context):
    context.driver = webdriver.Chrome()
    context.accounts = {
        "StandardUser": {"username": "standard_user", "password": "secret_sauce"},
        "LockedOutUser": {"username": "locked_out_user", "password": "secret_sauce"}
    }

def after_all(context):
    context.driver.quit()

#Write the batch/shell script
I would write the run_tests.sh file to run the tests:

#!/bin/bash
behave -f behave/ features/

#Run the tests and generate the report
I would run the tests using the run_tests.sh script and generate the BehaveX report.



