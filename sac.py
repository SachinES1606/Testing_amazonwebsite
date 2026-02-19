from concurrent.futures import wait
from random import random
from selenium import webdriver
from selenium.webdriver.common.by import By         
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

driver=webdriver.Chrome()
driver.get("https://www.google.com")

#searching the amazon website

elem = driver.find_element(By.XPATH,"//*[@id='APjFqb']")
elem.send_keys("Amazon")
elem.send_keys(Keys.RETURN)
time.sleep(25)

#clicking the second link of the search result

elem = driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/div/div/div/div[2]/cite").click()
time.sleep(10)

#searching for a product 

elem = driver.find_element(By.XPATH,"//*[@id='twotabsearchtextbox']")
elem.send_keys("iPhone 17 Pro Max")
elem.send_keys(Keys.RETURN)
time.sleep(8)

#Random clicking

iphone=driver.find_elements(By.CLASS_NAME,"s-search-results")
time.sleep(4)


# Scroll down to load more iphone and select a random iphone from the list

if iphone:
    random_iphone =driver.execute_script("window.scrollBy(0, 3000)")
    random_iphone = random.choice(iphone)
try:
    wait.until(EC.element_to_be_clickable(random_iphone)).click()
except:
    driver.execute_script("arguments[0].click();", random_iphone)

time.sleep(5)

#Switch to the new tab

elem2 = driver.switch_to.window(driver.window_handles[-1])
    # Add to cart

try:
    add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='add-to-cart-button']")))
    add_to_cart.click()
    print("Added to cart successfully ✅")
except:
    print("Add to cart not found ❌")


input("Press Enter to close the browser...")
driver.quit()