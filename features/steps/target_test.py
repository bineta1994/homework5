from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options
from behave import given, when, then

# Set up Chrome options for incognito mode
chrome_options = Options()
chrome_options.add_argument("--incognito")

# Use a function to get a new driver instance
def get_driver():
    driver_path = r"C:\Users\dijae\PycharmProjects\homework4\chromedriver.exe"
    service = Service(driver_path)
    return webdriver.Chrome(service=service, options=chrome_options)

@given('I open "{url}"')
def step_open_url(context, url):
    print(f"Opening {url}")
    context.browser = get_driver()
    context.browser.get(url)
    sleep(2)

@when('I click on the cart icon')
def step_click_cart_icon(context):
    print("Clicking on the cart icon")
    cart_icon = context.browser.find_element(By.CSS_SELECTOR, "[data-test='@web/CartIcon']")
    cart_icon.click()
    sleep(2)

@then('I should see the message "{message}"')
def step_verify_message(context, message):
    print(f"Verifying message: {message}")
    sleep(2)
    assert message in context.browser.page_source, "Expected message not found!"
    print("Message verified.")

@when('I click on "Sign In"')
def step_click_sign_in(context):
    print("Clicking on Sign In")
    sign_in_button = context.browser.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']")
    sign_in_button.click()
    sleep(2)

@when('I click on the "Sign In" option from the right-side navigation menu')
def step_click_sign_in_option(context):
    print("Clicking on the Sign In option in the navigation menu")
    sign_in_option = context.browser.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']")
    sign_in_option.click()
    sleep(2)

@then('the Sign In form should be displayed')
def step_verify_sign_in_form(context):
    print("Verifying the Sign In form is displayed")
    sleep(2)
    assert "Sign in" in context.browser.page_source, "Sign In form not displayed!"
    print("Sign In form verified.")

@when('I check the benefit cells')
def step_check_benefit_cells(context):
    print("Checking the benefit cells on the page")


@then('I should see 10 benefit cells')
def step_verify_benefit_cells(context):
    print("Verifying there are 10 benefit cells")
    benefit_cells = context.browser.find_elements(By.CSS_SELECTOR, "a[data-test='@web/slingshot-components/CellsComponent/Link']")

    # Print the number of benefit cells found
    print(f"Found {len(benefit_cells)} benefit cells.")

    # Check if we found exactly 10 benefit cells
    assert len(benefit_cells) == 10, f"Expected 10 benefit cells, but found {len(benefit_cells)}."

    print("Verified that there are 10 benefit cells.")
@then('close the browser')
def step_close_browser(context):
    print("Closing the browser")
    context.browser.quit()