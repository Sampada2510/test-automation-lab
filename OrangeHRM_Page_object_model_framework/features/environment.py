from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def before_all(context):
    """
    Executed once before all tests. Initializes the WebDriver.
    """
    try:
        # Set up Chrome options
        chrome_options = webdriver.ChromeOptions()

        # Optionally, run tests in headless mode if you don't want the browser UI
        # chrome_options.add_argument("--headless")  # Uncomment for headless mode
        chrome_options.add_argument("--window-size=1700,1700")  # Set custom window size

        # Initialize WebDriver with options
        context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        context.driver.implicitly_wait(10)
        context.driver.delete_all_cookies()
        context.driver.get('about:blank')
        print("WebDriver initialized successfully.")
        
    except Exception as e:
        print(f"Error during WebDriver initialization: {e}")
        raise

def after_all(context):
    """
    Executed once after all tests. Quits the WebDriver.
    """
    try:
        if hasattr(context, 'driver') and context.driver:
            context.driver.quit()
            print("WebDriver quit successfully.")
        else:
            print("WebDriver was not initialized.")
    except Exception as e:
        print(f"Error during WebDriver shutdown: {e}")
        raise

