# Este es nuestro módulo para hacer las solicitudes en nuestro proyecto

import requests # importamos para poder hacer llamados request a http

def get_categories(): #Agregamos esta función

    r = requests.get('https://api.escuelajs.co/api/v1/categories') # Creamos la variable y nos aseguramos de poner la dirección a la que queremos hacer las solicitudes
    
    print(r.status_code) # Al hacer la solicitud recibimos el estado
       
    print(r.text) # Recibimos el texto (contenido) que nos retorna con la solicitud
    
    print(type(r.text)) # Para que nos indique de qué tipo es la respuesta a nuestra solicitud (de hecho es un string, entregado como una lista con un diccionario)
    
    categories = r.json() # Para transformar ese string muy largo, entonces pido que las categorías las convierta en un formato json: lista reconocible por Python (en lugar de un txt)
    
    for category in categories: # Itero el formato json
        print(category['name']) # imprimo el título o nombre de cada categoría, unicamente


# De un estudiante: Les recomendaré una buena práctica, en el archivo de store py declaren la url como una variable:

# api_url_categories = 'https://api.escuelajs.co/api/v1/categories'