from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions
import time
import pandas as pd
import os

#Set up Google Chrome option and open browser
options = Options()
options.add_experimental_option("detach", True)
options.add_argument("user-data-dir=C:\\Users\\Techron\\AppData\\Local\\Google\\Chrome\\User Data")
driver = webdriver.Chrome(options=options)
url = "https://store.epicgames.com/en-US/"
driver.get(url)
driver.implicitly_wait(10)


time.sleep(5)

game = 0
while True:
    free_games_div = driver.find_element(By.CLASS_NAME, "css-1vu10h2")
    free_games = free_games_div.find_elements(By.CLASS_NAME, "css-1h2ruwl")
    status = free_games_div.find_elements(By.CLASS_NAME, "css-11xvn05")
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", free_games_div)

    if game == len(status):
        break

    name = free_games[game].text
    print(name)
    free_games[game].click()
    driver.implicitly_wait(5)
    try:
        age_block = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "css-quioav")))
        continue_button = driver.find_element(By.CLASS_NAME, "css-1a6we1t")
        continue_button.click()
    except selenium.common.TimeoutException:
        pass

    driver.implicitly_wait(5)

    try:
        get_button = WebDriverWait(driver,3).until(EC.presence_of_element_located((By.XPATH,"(//button[@class='css-1vkt3xd'])")))
    except selenium.common.TimeoutException:
        get_button = driver.find_element(By.XPATH,"//span[@class = 'css-8en90x']")


    if get_button.text != "IN LIBRARY":
        get_button.click()
        place_order_button = driver.find_element(By.XPATH,"//button[contains(@class,'payment-btn payment-order-confirm__btn')]")
        place_order_button.click()
        driver.implicitly_wait(10)
        print(f"{name} saved to the library")
    else:
        print(f"{name} in library already")
        driver.back()

    game += 1


print("Exiting Browser")
driver.quit()
