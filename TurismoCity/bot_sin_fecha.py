# Importando modulos necesarios

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import winsound

# Aca se define el precio objetivo

price = int(input('Ingrese el precio que esta dispuesto a abonar, en miles\n(Ej: 30000, 120000, etc):\n'))

# Definimos el directorio del driver de chrome e iniciamos el driver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Genero un bucle que solo termina si se dispara la alerta

while True:

    # Accedo a la web con la busqueda del vuelo y espero a que cargue. 
    # Este bot esta diseñado para buscar el mejor precio, independientemente de la fecha.
    
    driver.get("https://www.turismocity.com.ar/vuelos-baratos-de-BUE-Buenos_Aires-a-TYO-Tokyo_Japon")
    time.sleep(10)

    # Intento encontrar el elemento con el primer precio. Este es el mas bajo.
    # Si lo encuentra, convierte el string en entero y lo compara con el precio deseado.
    # Si no lo encuentra, intenta el bucle de nuevo.
   
    try:
       
        # Aqui toma el primer precio de la tabla de vuelos
       
        strPrice=driver.find_element(
            By.XPATH, value='//*[@id="VuelosBaratos"]/div[1]/div[2]/div[1]/div[2]/span[1]/span'
            ).text

        # Convierte el string en entero, quitando valores indeseados.
       
        strPrice = strPrice.replace('desde $ ','')
        intPrice = int(strPrice.replace('.',''))

        # Si el valor encontrado es menor al ingresado suena una alarma y muestra un mensaje.
      
        if intPrice <= price:
            for i in range(30):
                print(f'HAY PROMO!! El precio es {intPrice} !!!!!!!!!!!')
                winsound.Beep(1100, 70)
                time.sleep(0.01)            
            winsound.Beep(1500, 3000)
            break
        else:
          
            # Si el valor encontrado es mayor al deseado, imprime un mensaje y vuelve a intentar.
          
            print(f'')
            print(f'.........................................')
            print(f'Esperando promo...')
            print(f'')
            print(f'Su eleccion es de ${price}')
            print(f'El precio actual es de ${intPrice}')        
            print(f'')
            continue
    except:
        continue
