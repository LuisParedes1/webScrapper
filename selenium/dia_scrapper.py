import re
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def scrape_jumbo(key_to_scrape: str):
    # Launch the Chrome browser
    driver = webdriver.Chrome()

    # Open the Coto website
    driver.get("https://diaonline.supermercadosdia.com.ar/")

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Find the search input field and enter "coca cola"
    input_id = re.search(r'downshift-(\d+)-input', driver.page_source)
    
    try:
        search_input = wait.until(EC.presence_of_element_located((By.ID, f"{input_id.group(0)}")))

    except TimeoutException:
        print("No se encontró el input")
        return

    search_input.send_keys(key_to_scrape)
    search_input.send_keys(Keys.ENTER)

    product_list = wait.until(EC.presence_of_element_located((By.ID, "gallery-layout-container")))
    product_containers = product_list.find_elements(By.XPATH, "./div")

    for prod in product_containers:
        print(prod.text)


if __name__ == "__main__":
    # Get from the program parameters the product to search
    key_to_scrape: str = sys.argv[1]
    scrape_jumbo(key_to_scrape)