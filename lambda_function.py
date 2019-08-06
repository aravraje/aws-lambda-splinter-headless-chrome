from splinter import Browser
from selenium.webdriver.chrome.options import Options
import os

def lambda_handler(event, context):
    # TODO implement
    print("Starting google.com")
    
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--single-process')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.binary_location = os.getcwd() + "/headless-chromium"

    chrome_driver_path = {'executable_path': os.getcwd() + '/chromedriver'}

    browser = Browser('chrome', options=chrome_options, **chrome_driver_path)
    
    browser.visit('https://www.google.com/')

    body = f"Headless Chrome Initialized, Page title: {browser.title}"

    print(body)

    browser.cookies.delete()
    browser.quit()
    return body

