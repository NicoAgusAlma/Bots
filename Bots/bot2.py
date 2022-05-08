# CHEQUEAR URLS
# CHEQUEAR TEXTO DE LA NOTA

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
   
driver.get("https://prenotami.esteri.it/Services/Booking/414")

solapa1 = driver.current_window_handle

search=driver.find_element(By.ID, value="login-email")
search.send_keys("enablegodmode@gmail.com")
search=driver.find_element(By.ID, value="login-password")
search.send_keys("Contraseña123")
search.send_keys(Keys.RETURN)
#driver.get("https://prenotami.esteri.it/Services/Booking/414")

wait = WebDriverWait(driver, 5)

assert len(driver.window_handles) == 1

driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa2 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa3 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa4 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa5 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa6 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa7 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa8 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa9 = driver.current_window_handle
driver.switch_to.new_window('tab')
#driver.get("https://prenotami.esteri.it/Services/Booking/414")
solapa10 = driver.current_window_handle

wait.until(EC.number_of_windows_to_be(10))

while True:

    driver.switch_to.window(solapa1)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa2)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa3)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa4)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa5)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa6)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa7)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa8)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa9)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa10)
    driver.get("https://prenotami.esteri.it/Services/Booking/414")
    search=driver.find_element(By.ID, value="BookingNotes")
    search.send_keys("CITTADINANZA PER RICOSTRUZIONE - HECTOR ALMAZETE")
    search=driver.find_element(By.ID, value="PrivacyCheck")
    search.send_keys(Keys.SPACE)
    search=driver.find_element(By.ID, value="btnAvanti")
    search.send_keys(Keys.RETURN)
    pyautogui.press('enter')
    time.sleep(1)

    driver.switch_to.window(solapa1)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()
            
    driver.switch_to.window(solapa2)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()   

    driver.switch_to.window(solapa3)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()

    driver.switch_to.window(solapa4)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()

    driver.switch_to.window(solapa5)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()

    driver.switch_to.window(solapa6)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()
            
    driver.switch_to.window(solapa7)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()   

    driver.switch_to.window(solapa8)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()

    driver.switch_to.window(solapa9)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()

    driver.switch_to.window(solapa10)

    while True:
        try:
            ventana=driver.find_element(By.XPATH, value="/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[3]/div")
            
            if ventana.text == 'Al momento non ci sono date disponibili per il servizio richiesto': 
                print('Salto el cartel. Intentando nuevamente.')
                break
            else:
                for i in range(30):
                    print('MAIL ENVIADOOOOOOOOOO!')
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS) 
                quit()
        except:
            for i in range(30):
                print('MAIL ENVIADOOOOOOOOOO!')
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)        
            quit()