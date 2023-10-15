# Paso 1: Indica la versión de Python desde la cual parte este ambiente dockerizado:
FROM python:3.8

# Paso 2: Crea un directorio o carpeta o el espacio de trabajo para este contenedor:
WORKDIR /app

# Paso 3: Una buena práctica: copiar el archivo con todas las dependencias para incorporarlo a este ambiente (del ambiente local al ambiente del contenedor):
COPY requirements.txt /app/requirements.txt

# Paso 4: Instala todas las dependencias leyendo el archivo de requerimientos (opcional: no aplique caché + upgrades):
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Paso 5: Copia todo el código del directorio actual y lo lleva al contenedor app (observe que no debe ir espacio luego del slash
COPY . /app

# Paso 6: Mantiene en ejecución constante el contenedor 
CMD bash -c "while true; do sleep 1; done"

# Nota: Este contenedor se hace correr con el código creado en un archivo: docker-compose.yml