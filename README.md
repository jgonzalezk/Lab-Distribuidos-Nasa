# Laboratorio de Sistemas Distribuidos
blablabla

## API - Nasa Asteroids NeoWs

### Procesamiento de datos
Creación de la base de datos______________

Para crear este proyecto se usa Mongodb v5.

Instalar la librería necesarias para trabajar con Mongo en la carpeta de procesamiento de datos:
```shell
npm install mongodb
pip install pymongo
```
Para crear base de datos (tener instalado node y conección a localhost:27017 en mongo):
```shell
node database_create.js
```

Producción y consumo de API_____________

Instalar la librería necesaria de Kafka:
```shell
pip install confluent-kafka
```
Ahora para poder correr Kafka con el contenedor de Docker, en la carpeta de procesamiento de datos ejecutar:
```shell
docker compose up -d
```

Para utilizar el productor ejecutar una de estas opciones:
```shell
./producer.py getting_started.ini
```
```shell
python producer.py getting_started.ini
```
Para utilizar el consumidor ejecutar una de estas opciones:
```shell
./consumer.py getting_started.ini
```
```shell
python consumer.py getting_started.ini
```

### Backend
Insertar hacen correr esta parte

### Frontend
Insertar hacen correr esta parte
```shell
pip install
npm run dev
```
