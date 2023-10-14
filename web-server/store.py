# Este es nuestro módulo para hacer las solicitudes en nuestro proyecto

import requests # importamos para poder hacer llamados request a http

def get_categories(): #Agregamos esta función
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # Creamos la variable y nos aseguramos de poner la dirección a la que queremos hacer las solicitudes
    print(r.status_code) # Al hacer la solicitud recibimos el estado
    print(r.text) # Recibimos el texto (contenido) que nos retorna con la solicitud
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])