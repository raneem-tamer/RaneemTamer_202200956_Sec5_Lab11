from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Step 1: Set up Chrome Options
options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

# Step 2: Set up the WebDriver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

def extract_price(driver):
    """ Extract product price using multiple strategies. """
    price = "Price not available"
    try:
        # First try: Standard price element
        price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen").text
    except NoSuchElementException:
        try:
            # Second try: Deal price
            price = driver.find_element(By.ID, "priceblock_dealprice").text
        except NoSuchElementException:
            try:
                # Third try: Our price
                price = driver.find_element(By.ID, "priceblock_ourprice").text
            except NoSuchElementException:
                try:
                    # Fourth try: Using XPath for embedded price
                    price = driver.find_element(By.XPATH, "//*[contains(@class, 'a-price')]/span").text
                except NoSuchElementException:
                    logging.warning("Could not locate the price element.")
    return price

try:
    # Step 3: Open the Amazon website
    base_url = "https://www.amazon.com"
    driver.get(base_url)

    # Step 4: Search for a product category
    search_term = "Headphones"
    search_bar = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.RETURN)

    # Step 5: Wait for search results
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.s-main-slot"))
    )

    # Step 6: Click on the first product
    first_product = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result'] a"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
    time.sleep(2)  # Allow for overlays to load
    first_product.click()

    # Step 7: Extract product details
    product_title = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    ).text
    product_url = driver.current_url
    product_price = extract_price(driver)

    # Logic for extracting rating
    try:
        product_rating = driver.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
    except NoSuchElementException:
        product_rating = "Rating not available"

    # Step 8: Print details
    logging.info("Product Title: %s", product_title)
    logging.info("Product URL: %s", product_url)
    logging.info("Product Price: %s", product_price)
    logging.info("Product Rating: %s", product_rating)

    # Step 9: Screenshot
    screenshot_name = "product_page_screenshot.png"
    driver.save_screenshot(screenshot_name)
    logging.info("Screenshot saved as %s", screenshot_name)

    time.sleep(3)  # Optional delay before closing

finally:
    driver.quit()
