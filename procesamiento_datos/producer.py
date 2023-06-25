#!/usr/bin/env python

import sys
from random import choice
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
import requests
import json

if __name__ == '__main__':
    # Parse the command line.
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    args = parser.parse_args()

    # Parse the configuration.
    # See https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    config_parser = ConfigParser()
    config_parser.read_file(args.config_file)
    config = dict(config_parser['default'])
    
   # Create Producer instance
    producer = Producer(config)

        # Optional per-message delivery callback (triggered by poll() or flush())
        # when a message has been successfully delivered or permanently
        # failed delivery (after retries).
    """def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
         else:
            print("Produced event to topic {topic}: value = {value:12}".format(
                topic=msg.topic(), value=msg.value().decode('utf-8'))) """
    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))


    #api_key = 'YEZdkjrSdir4Wnal1hTqz9tpMN84Djl95RUY1Owp'
    #response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=202https://cdn.discordapp.com/attachments/1094071233693356118/1115503381788770345/Distribuidos2.png1-01-01&end_date=2021-01-06&api_key='+api_key)
    response = requests.get('https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-10&api_key=DEMO_KEY')
    data = response.json()

    near_earth_objects = data["near_earth_objects"]

    for date in near_earth_objects:
        asteroids = near_earth_objects[date]

        for asteroid in asteroids:

            asteroid_id = asteroid["id"]
            name = asteroid["name"]
            absolute_magnitude_h = asteroid["absolute_magnitude_h"]
            is_potentially_hazardous = asteroid["is_potentially_hazardous_asteroid"]
            is_sentry_object = asteroid["is_sentry_object"]

            estimated_diameter = asteroid["estimated_diameter"]
            estimated_diameter_meters = estimated_diameter["meters"]
            estimated_diameter_min = estimated_diameter_meters["estimated_diameter_min"]
            estimated_diameter_max = estimated_diameter_meters["estimated_diameter_max"]

            
            close_approach_data = asteroid["close_approach_data"]
            close_approach_data = close_approach_data[0]
            orbiting_body =close_approach_data["orbiting_body"]
            relative_velocity = close_approach_data["relative_velocity"]
            relative_velocity_KpS = relative_velocity["kilometers_per_second"]


            asteroid_dict = {
                "ID": asteroid_id,
                "Name": name,
                "Date": date,
                "Absolute_magnitude_h": absolute_magnitude_h,
                "Is_potentially_hazardous_asteroid": is_potentially_hazardous,
                "Estimated_diameter_met_min": estimated_diameter_min,
                "Estimated_diameter_met_max": estimated_diameter_max,
                "Orbiting_body": orbiting_body,
                "Relative_velocity_KpS": relative_velocity_KpS,
                "Is_sentry_object": is_sentry_object
            } 

            # Serialize the dictionary in JSON format
            asteroid_json = json.dumps(asteroid_dict)
            # Encode the JSON in bytes
            message_value = asteroid_json.encode('utf-8')
            # Send dictionary asteroid
            producer.produce('asteroid', message_value, callback=delivery_callback)

    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()