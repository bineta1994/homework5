from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application


def get_driver():
    """
    Set up and return a new instance of a Chrome WebDriver with required options.
    """
    # Set up Chrome options for incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--incognito")

    # path to chromedriver
    driver_path = r"C:\Users\dijae\PycharmProjects\homework4\chromedriver.exe"

    # service using chromedriver path
    service = Service(driver_path)

    # Return the Chrome WebDriver instance
    return webdriver.Chrome(service=service, options=chrome_options)


def before_all(context):
    """
    Set up the browser driver and application instance before all tests.
    """
    context.driver = get_driver()  # Store driver in context
    context.app = Application(context.driver)


def after_all(context):
    """
    Quit the browser after all tests are completed.
    """
    context.driver.quit()
