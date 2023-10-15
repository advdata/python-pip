FROM python:3.10 # Indica la versión de Python desde la cual parte este ambiente dockerizado

WORKDIR /app # Crea un directorio o carpeta o el espacio de trabajo para este contenedor
COPY requirements.txt /app/requirements.txt # Una buena práctica: copiar el archivo con todas las dependencias para incorporarlo a este ambiente (del ambiente local al ambiente del contenedor)

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt # Instala todas las dependencias leyendo el archivo de requerimientos (opcional: no aplique caché + upgrades)

COPY . /app # Copia todo el código del directorio actual y lo lleva al contenedor app (observe que no debe ir espacio luego del slash)

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"] # Comando para lanzar el servidor de uvicorn y que lo mantenga encendido 

# La siguiente línea era la que corría los scripts desde la linea de comandos:
# CMD bash -c "while true; do sleep 1; done"  # Mantiene en ejecución constante el contenedor 

# Este contenedor se hace correr con el código creado en un archivo: docker-compose.yml