
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

def Test():
    link= "https://www.calculator.net/fuel-cost-calculator.html"

    driver.get(link)

    time.sleep(3)

    distance= driver.find_element(By.NAME, "tripdistance")
    distance.clear()
    distance.send_keys("600")
    print("set distance to 600km")
    fuel= driver.find_element(By.NAME,"fuelefficiency")
    fuel.clear()
    fuel.send_keys("7")
    print("set fuel efficiency to 7 liters per 100km")
    price= driver.find_element(By.NAME,"gasprice")
    price.clear()
    price.send_keys("5")
    print("set gas price at 5 per liter")


    time.sleep(1)
    driver.find_element(By.NAME,"x").click()
    print("Calculate...")

    time.sleep(3)
    result = driver.find_element(By.CLASS_NAME, "verybigtext")
    print(result.text)

    if result.text == "This trip will require 42 liters of fuel, which amounts to a fuel cost of $210.":
        print("Result is correct")
    else:
        print("Result is incorect")

    time.sleep(3)

    driver.quit()

Test(webdriver.Firefox())
Test(webdriver.Chrome())