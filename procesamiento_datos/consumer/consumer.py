import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient
from kafka import KafkaConsumer

if __name__ == '__main__':

    # Load enviroment
    load_dotenv()
    # Enviroment values
    MONGO_USERNAME= os.environ.get("MONGO_USERNAME")
    MONGO_PASSWORD= os.environ.get("MONGO_PASSWORD")
    MONGO_HOSTNAME= os.environ.get("MONGO_HOSTNAME")
    MONGO_PORT= os.environ.get("MONGO_PORT")
    MONGO_DB= os.environ.get("MONGO_DB")

    # Creat mongo url
    mongo_url = f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}:{MONGO_PORT}/{MONGO_DB}?authSource=admin'
    client = MongoClient(mongo_url)
    print(mongo_url)

    # Configuring the connection to MongoDB
    client = MongoClient(mongo_url)
    db = client[MONGO_DB]  # Database name
    collection = db['asteroids']  # Collection name

    KAFKA_SERVER = os.environ.get("KAFKA_SERVER")
    consumer_config = {
        'bootstrap_servers': [KAFKA_SERVER],  # Kafka server cluster
        'group_id': 'nasa_group',  # Container group
        'auto_offset_reset': 'earliest',  # Establece el offset al principio para recibir todos los mensajes
        'enable_auto_commit': False  # Deshabilita el auto commit
    }

    # Create consumer instance with config
    consumer = KafkaConsumer('asteroid', **consumer_config)

    # Poll for new messages from Kafka and print them.
    try:
        for msg in consumer:
            # Decode message
            asteroid = msg.value.decode('utf-8')
            asteroid_dict = json.loads(asteroid)
            print(asteroid_dict)
            # Insert datas in MongoDB
            collection.insert_one(asteroid_dict)
            # Confirmar la posición de lectura del mensaje
            consumer.commit()

    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()
        # Close connection to database
        client.close()