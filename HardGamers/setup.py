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

# Definimos path y nombre del archivo de registro de precios
path_csv = 'C:/Users/Nico/Python/Bots/HardGamers/tablas/'

# Aqui se define el tiempo de espera entre busqueda y busqueda
delay = 10

# Esto configura la ruta e inicia el driver de Selenium. En este caso Chrome.
path = "C:\Program Files (x86)\chromedriver.exe"

# Aqui se define cada cuantas horas, se graba un registro.
frecuencia_registro = 1

# Aqui se define el ID del canal y autorizacion del bot. Esto esta explicado en el README
canal_discord = 'AQUI VA EL ID!!!!!!!!!'
header = {'authorization': 'AQUI VA EL AUTHORIZATION CODE!!!!!!!!!'}
 