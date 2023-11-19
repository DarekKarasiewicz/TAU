from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def Test(driver):
    link = "https://1login.wp.pl/zaloguj/dodaj?client_id=wp-backend&login_challenge=Cj4KJDExZTc5M2IyZjQxNDg0NDA4OTI3NzYyZTI4Mjc2NTVmOGIzZhDC3-eqBhoQCgp3cC1iYWNrZW5kEgJ2MhIgQw-ucRfu4d1kzKDURpdpE4j1PSK_eHh2T1pIE-S1YGg"

    driver.get(link)

    time.sleep(1)

    username_field = driver.find_element(By.ID, "login")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("TwójLogin@wp.pl")
    print("Wpisano login")
    password_field.send_keys("TwojeHaslo")
    print("Wpisano hasło")

    password_field.send_keys(Keys.RETURN)

    time.sleep(3)

    if "Nieprawidłowy adres e‑mail lub hasło" in driver.page_source:
        print("Błąd logowania!")
    else:
        print("Zalogowało")

    driver.quit()

Test(webdriver.Firefox())
Test(webdriver.Chrome())