import sys
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Consumer, OFFSET_BEGINNING
import json
from pymongo import MongoClient

if __name__ == '__main__':

    # Configuring the connection to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client['NASA_data']  # Database name
    collection = db['asteroids']  # Collection name
    
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()

    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])
    config.update(config_parser['consumer3'])

    # Create Consumer instance
    consumer = Consumer(config)

    # Set up a callback to handle the '--reset' flag.
    def reset_offset(consumer, partitions):
        if args.reset:
            for p in partitions:
                p.offset = OFFSET_BEGINNING
            consumer.assign(partitions)

    # Subscribe to topic
    topic = "asteroid3"
    consumer.subscribe([topic], on_assign=reset_offset)

    # Poll for new messages from Kafka and print them.
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                # Initial message consumption may take up to
                # `session.timeout.ms` for the consumer group to
                # rebalance and start consuming
                #print("Waiting...")
                print(".")

            elif msg.error():
                print("ERROR: %s".format(msg.error()))

            else:
                #Decode message 
                asteroid = msg.value().decode('utf-8')
                asteroid_dict = json.loads(asteroid)
                # Insert datas in MongoDB
                collection.insert_one(asteroid_dict)
                # Confirmar la posición de lectura del mensaje
                consumer.commit(msg)
                
    except KeyboardInterrupt:
        pass
    finally:
        # Leave group and commit final offsets
        consumer.close()
        # Close connection to database
        client.close()