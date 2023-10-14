# Este es nuestro ejecutable del proyecto

import store # Importamos el módulo que contiene la función e imprime los resultados de la solicitud
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# Por ahora comento la siguiente línea:
#app = FastAPI()

@app.get('/')
def get_list():
    return [1,2,3,]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def run(): #Definimos una función
    store.get_categories() # Que nos trae las categorías, ejecutando la función que creamos en el módulo

# Lo siguiente se incluye porque queremos que se ejecute como un script

if __name__ == '__main__':
    run() # Al correr como script, ejecuta la función run