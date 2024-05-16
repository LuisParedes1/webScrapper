import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

def scrape_disco(key_to_scrape: str):
    # Launch the Chrome browser
    driver = webdriver.Chrome()

    # Open the Coto website
    driver.get("https://www.disco.com.ar/")

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Find the search input field and enter "coca cola"
    search_input = None

    for i in range(0,4):
        try:
            search_input = wait.until(EC.presence_of_element_located((By.ID, "downshift-"+str(i)+"-input")))
            break
        except TimeoutException:
            pass
        
    search_input.send_keys(key_to_scrape)
    search_input.send_keys(Keys.ENTER)

    product_list = wait.until(EC.presence_of_element_located((By.ID, "gallery-layout-container")))
    product_containers = product_list.find_elements(By.XPATH, "./div")

    for prod in product_containers:
        print(prod.text)


if __name__ == "__main__":
    # Get from the program parameters the product to search
    key_to_scrape: str = sys.argv[1]
    scrape_disco(key_to_scrape)

    