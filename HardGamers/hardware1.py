
#----------------------------VERSION 1.0----------------------------#

# importamos librerias necesarias
from re import U
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pip._vendor.requests 

# Aqui se define el ID del canal y autorizacion del bot. Esto esta explicado en el README
canal_discord = 'AQUI VA EL ID!!!!!!!!!'
header = {'authorization': 'AQUI VA EL AUTHORIZATION CODE!!!!!!!!!'}
     
# Esto configura la ruta e inicia el driver de Selenium. En este caso Chrome.
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Aqui se ingresan las palabras claves, las URL y el precio dispuesto a pagar
busquedas = [
    ['RTX 3080','https://www.hardgamers.com.ar/search?text=rtx+3080', 120000],
    ['RTX 3070','https://www.hardgamers.com.ar/search?text=rtx+3070', 100000],
]

# Aqui se colocan textos que podrian encontrarse dentro del primer cuadrito y que deseamos ignorar
# P.ej: Si el primer cuadradito contiene una frase como "ARMADO DE PC CON RTX 3060" y estamos interesados justamente en esa placa,
# podemos simplemente agregar la frase "ARMADO DE PC" y el bot ignorara todo articulo y precio que contenga esa frase.
ignorar_texto = [
    'ARMADO RIG',
    'SLI',
]

# Aqui se define el tiempo de espera entre busqueda y busqueda
delay = 5

# Estas variables se usan mas adelante
articulos = 0
elemento_tabla = 1

# Este bucle provoca el ciclo constante entre los items dentro de la lista
while True:

    # articulos va incrementando a medida que pasan los items de la lista. Si ya paso el ultimo item, comienza de nuevo
    if articulos >= len(busquedas):
        articulos = 0

    # Aqui ingresa en la URL del primer elemento de la lista y lee el texto del primer cuadrito
    driver.get(busquedas[articulos][1])    
    casillero=driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[3]/div/section/article[" + str(elemento_tabla) + "]/div[2]/a/h3")
    texto_casillero = casillero.text
    
    # Si el nombre definido en el primer lugar del item no se encuentra en la descripcion del cuadrito, pasa al segundo y asi sucesivamente.
    # Esto es asi porque a veces HardGamer coloca al principio cuadraditos de propagandas que no tienen que ver con el item buscado.
    # De esta manera solo compara el precio si el item a comparar es el que estamos buscando.
    
    ignorar = False
    for i in ignorar_texto:
        if i in texto_casillero:
            ignorar = True

    if busquedas[articulos][0] in texto_casillero and ignorar == False:
        casillero_precio=driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[3]/div/section/article[" + str(elemento_tabla) + "]/div[2]/div[1]/h2[2]")          
        texto_precio = casillero_precio.text

        # Reemplaza caracteres innecesarios dentro del precio y lo almacena como numero entero
        try:
            texto_precio = texto_precio.replace(',00','')
        except:
            pass
        try:
            texto_precio = texto_precio.replace(',99','')
        except:
            pass
        try:
            texto_precio = texto_precio.replace('.','')
        except:
            pass
        elemento_tabla = 1

        # Si el precio de la publicacion es mayor al colocado en el tercer lugar del item en la lista, 
        # pasa al siguiente articulo de la lista y comienza el ciclo nuevamente.
        if int(texto_precio) > (busquedas[articulos][2]):
            print('El precio de ' + busquedas[articulos][0] + ' (' + str(texto_precio) + ') es mayor que el ingresado (' + str(busquedas[articulos][2]) + ').')
            time.sleep(delay)
            articulos += 1

        # Si el precio de la publicacion es menor al colocado en el tercer lugar del item en la lista,
        # envia la notificacion por Discord y detiene todos los ciclos.   
        else:
            casillero.click()
            texto_placa = driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[1]/div[2]/div[2]/a[2]/h1").text
            imagen_placa = driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[1]/div[2]/div[1]/a/img").get_attribute("src")
            web_placa = driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[1]/div[2]/div[2]/a[4]").get_attribute("href") 
            print('El precio de ' + busquedas[articulos][0] + ' (' + str(texto_precio) + ') es menor que el ingresado (' + str(busquedas[articulos][2]) + ').')
            mensajeDiscord = {'content': texto_placa + ' ESTA BARATA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'}            
            r = pip._vendor.requests.post("https://discord.com/api/v9/channels/"+ canal_discord +"/messages", data=mensajeDiscord, headers=header)            
            mensajeDiscord = {'content': imagen_placa}
            r = pip._vendor.requests.post("https://discord.com/api/v9/channels/"+ canal_discord +"/messages", data=mensajeDiscord, headers=header)            
            mensajeDiscord = {'content': web_placa}
            r = pip._vendor.requests.post("https://discord.com/api/v9/channels/"+ canal_discord +"/messages", data=mensajeDiscord, headers=header) 
            break
        continue

    # Esto se ejecuta si el texto del cuadrito no coincide con el nombre que pusimos en el item.       
    else: 
        elemento_tabla += 1
        print('Siguiente precio....')
        continue