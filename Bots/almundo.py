from pydoc import classname
import time
from wsgiref.handlers import SimpleHandler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import winsound

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

while True:

    driver.get("https://almundo.com.ar/flights/results?from=BUE,CUN&to=CUN,BUE&date=2022-09-15,2022-09-30&adults=2&exclude=matrix#sortBy=PRICE")

    time.sleep(10)

    try:

        precioTexto=driver.find_element(By.CLASS_NAME, value='pricebox__price__total')

        precio_neto = precioTexto.text[2:5]

        precioK = int(precio_neto)

        # Aqui se aclara el precio en miles -> 30.000 se pondria como 30
        if precioK <= 400:
            for i in range(30):
                print(f'HAY PROMO!! El precio es {precioK}K')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)    
            break
        else:
            print('Esperando promo...')
            continue
    except:
        continue

