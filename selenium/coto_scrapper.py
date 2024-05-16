import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_coto(key_to_scrape):
    # Launch the Chrome browser
    driver = webdriver.Chrome()

    # Open the Coto website
    driver.get("https://www.cotodigital3.com.ar/sitios/cdigi/")

    # Wait for the page to load
    wait = WebDriverWait(driver, 10)

    # Find the search input field and enter "coca cola"
    search_input = wait.until(EC.presence_of_element_located((By.ID, "atg_store_searchInput")))
    search_input.send_keys(key_to_scrape)

    # Submit the search form
    search_input.submit()

    # Wait for the search results page to load
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[starts-with(@id, 'descrip_container_')]")))

    # Find the list
    product_list = wait.until(EC.presence_of_element_located((By.ID, "products")))

    # Find all list items within the list
    product_containers = product_list.find_elements(By.TAG_NAME, "li")

    for container in product_containers:
        # Find the product name within each container
        product_name = container.find_element(By.XPATH, ".//div[starts-with(@id, 'descrip_container_')]").text

        # Check if the discount price element exists
        discount_price_elements = container.find_elements(By.XPATH, ".//span[@class='price_discount']")
        if discount_price_elements:
            # Use JavaScript to get the text, remove leading and trailing whitespace, and replace newline characters
            product_price = driver.execute_script("return arguments[0].innerText;", discount_price_elements[0]).strip().replace('\n', '')
        else:
            # Check if the regular price element exists
            price_elements = container.find_elements(By.XPATH, ".//span[@class='atg_store_newPrice']")
            if price_elements:
                # Use JavaScript to get the text, remove leading and trailing whitespace, and replace newline characters
                product_price = driver.execute_script("return arguments[0].innerText;", price_elements[0]).strip().replace('\n', '')
            else:
                product_price = "Price not available"

        print("Product Name: ", product_name)
        print("Price: ", product_price)


if __name__ == "__main__":
    # Get from the program parameters the product to search
    key_to_scrape = sys.argv[1]
    scrape_coto(key_to_scrape)