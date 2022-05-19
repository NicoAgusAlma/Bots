
#----------------------------VERSION 2.0----------------------------#

# importamos librerias necesarias
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pip._vendor.requests 
from datetime import datetime, timedelta
import csv
import setup

# Aqui se detectan los csv de los items y en caso de que no existan, se crean con encabezado
for item in setup.busquedas:
    try:
        with open(setup.path_csv+item[0]+'.csv') as f:
            f.close
    except:
        print('Creando CSV de  ' + str(item[0]))
        with open(setup.path_csv+item[0]+'.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['FECHA','ITEM','PRECIO','DATE_TIME'])
        f.close
    
driver = webdriver.Chrome(setup.path)

# Estas variables se usan mas adelante
articulos = 0
elemento_tabla = 1
dict_items = {}

# Se crea un diccionario con los nombres de los items como llaves y la ultima hora de sus registros
for item in setup.busquedas:
    with open(setup.path_csv+item[0]+'.csv') as f:
        reader = csv.reader(f,delimiter=',') 
        rows = list(reader)
        dict_items[str(rows[-1][1])]=rows[-1][3] 
        f.close

# Este bucle provoca el ciclo constante entre los items dentro de la lista
while True:

    # articulos va incrementando a medida que pasan los items de la lista. Si ya paso el ultimo item, comienza de nuevo
    if articulos >= len(setup.busquedas):
        articulos = 0

    # Aqui ingresa en la URL del primer elemento de la lista y lee el texto del primer cuadrito
    driver.get(setup.busquedas[articulos][1])    
    casillero=driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[3]/div/section/article[" + str(elemento_tabla) + "]/div[2]/a/h3")
    texto_casillero = casillero.text
    
    # Si el nombre definido en el primer lugar del item no se encuentra en la descripcion del cuadrito, pasa al segundo y asi sucesivamente.
    # Esto es asi porque a veces HardGamer coloca al principio cuadraditos de propagandas que no tienen que ver con el item buscado.
    # De esta manera solo compara el precio si el item a comparar es el que estamos buscando.
    ignorar = False
    for i in setup.ignorar_texto:
        if i in texto_casillero:
            ignorar = True

    if setup.busquedas[articulos][0] in texto_casillero and ignorar == False:
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
        if int(texto_precio) > (setup.busquedas[articulos][2]):
            print('El precio de ' + setup.busquedas[articulos][0] + ' (' + str(texto_precio) + ') es mayor que el ingresado (' + str(setup.busquedas[articulos][2]) + ').')
            time.sleep(setup.delay)  

            # Aqui se compara la hora actual con la ultima hora registrada (almacenada en el diccionario).
            # Si ya paso mas tiempo que el designado en la variable frecuencia_registro, se agrega un nuevo registro
            # y se modifica en el diccionario la nueva ultima hora registrada de ese item.
            if datetime.today() - datetime.strptime(dict_items[setup.busquedas[articulos][0]], '%Y/%m/%d %H:%M:%S') > timedelta(hours=setup.frecuencia_registro):
                print('Guardando ultima fecha en item '+ setup.busquedas[articulos][0])  
                fecha = datetime.today().strftime('%Y/%m/%d %H:%M:%S')
                dia = datetime.today().strftime("%d/%m/%Y")
                with open(setup.path_csv+setup.busquedas[articulos][0]+'.csv', 'a', newline='') as f:
                    writer = csv.writer(f)                
                    writer.writerow([dia, setup.busquedas[articulos][0], texto_precio, fecha])
                    f.close
                dict_items[setup.busquedas[articulos][0]] = datetime.today().strftime('%Y/%m/%d %H:%M:%S')
            articulos += 1

        # Si el precio de la publicacion es menor al colocado en el tercer lugar del item en la lista,
        # envia la notificacion por Discord y detiene todos los ciclos.   
        else:
            casillero.click()
            texto_placa = driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[1]/div[2]/div[2]/a[2]/h1").text
            imagen_placa = driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[1]/div[2]/div[1]/a/img").get_attribute("src")
            web_placa = driver.find_element(By.XPATH, value="/html/body/div/div[4]/div/div[1]/div[2]/div[2]/a[4]").get_attribute("href") 
            print('El precio de ' + setup.busquedas[articulos][0] + ' (' + str(texto_precio) + ') es menor que el ingresado (' + str(setup.busquedas[articulos][2]) + ').')
            mensajeDiscord = {'content': texto_placa + ' ESTA $'+ str(texto_precio) + ' Y MAS BARATA QUE $'+ str(setup.busquedas[articulos][2]) +' !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'}            
            r = pip._vendor.requests.post("https://discord.com/api/v9/channels/"+ setup.canal_discord +"/messages", data=mensajeDiscord, headers=setup.header)            
            mensajeDiscord = {'content': imagen_placa}
            r = pip._vendor.requests.post("https://discord.com/api/v9/channels/"+ setup.canal_discord +"/messages", data=mensajeDiscord, headers=setup.header)            
            mensajeDiscord = {'content': web_placa}
            r = pip._vendor.requests.post("https://discord.com/api/v9/channels/"+ setup.canal_discord +"/messages", data=mensajeDiscord, headers=setup.header) 
            break
        continue

    # Esto se ejecuta si el texto del cuadrito no coincide con el nombre que pusimos en el item.       
    else: 
        elemento_tabla += 1
        print('Omitiendo item por configuracion en setup.py (linea 27)....')
        continue