
from datetime import datetime
from urllib.parse import parse_qs, urlparse
from datetime import datetime
from argparse import ArgumentParser, FileType
from configparser import ConfigParser
from confluent_kafka import Producer
import requests
import json
import time

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

    def delivery_callback(err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))

    def define_asteroid(asteroid, date):
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
        return asteroid_dict
    
    def define_url(start_date_str, end_date_str):
        # Get url
        return f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date_str}&end_date={end_date_str}&api_key=DEMO_KEY'
    
    def get_start_date(url):
        # Parse the URL and extract the parameters date
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        return query_params.get('start_date', [None])[0]
    
    def get_end_date(url):
        # Parse the URL and extract the parameters date
        parsed_url = urlparse(url)
        query_params = parse_qs(parsed_url.query)
        return query_params.get('end_date', [None])[0]
        
    def to_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d').date()

    #  Today
    today = datetime.now().date()
    # Url of init date (2000 at the moment)
    url = 'http://api.nasa.gov/neo/rest/v1/feed?start_date=2023-04-08&end_date=2023-04-15&detailed=false&api_key=DEMO_KEY'
    # Flag to end while when data is from today
    close = False
    count = 1
    while ( to_date(get_start_date(url)) <= today and close == False):

        if(count == 6): #API die at 6 request 
            time.sleep(10)
            count = 1
        
        if to_date(get_end_date(url)) == today:

            response = requests.get(url)
            data = response.json()
            near_earth_objects = data["near_earth_objects"]

            for date in near_earth_objects:
                print(date + " 1")
                asteroids = near_earth_objects[date]
                for asteroid in asteroids:
                    asteroid_dict = define_asteroid(asteroid, date)
                    # Serialize the dictionary in JSON format
                    asteroid_json = json.dumps(asteroid_dict)
                    # Encode the JSON in bytes
                    message_value = asteroid_json.encode('utf-8')
                    # Send dictionary asteroid
                    producer.produce('asteroid', message_value, callback=delivery_callback)
            close = True    

        elif to_date(get_end_date(url)) > today:

            url = define_url( to_date(get_start_date(url)).strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d'))
            print(url)
            response = requests.get(url)
            data = response.json()
            near_earth_objects = data["near_earth_objects"]

            for date in near_earth_objects:
                print(date+" 2")
                asteroids = near_earth_objects[date]

                for asteroid in asteroids:
                    asteroid_dict = define_asteroid(asteroid, date)
                    # Serialize the dictionary in JSON format
                    asteroid_json = json.dumps(asteroid_dict)
                    # Encode the JSON in bytes
                    message_value = asteroid_json.encode('utf-8')
                    # Send dictionary asteroid
                    producer.produce('asteroid', message_value, callback=delivery_callback)
            close = True

        else:
            response = requests.get(url)    
            data = response.json()
            near_earth_objects = data["near_earth_objects"]
            
            for date in near_earth_objects:
                # Information from the last date will not be saved, since the following url saves it
                if date != get_end_date(url):
                    asteroids = near_earth_objects[date]
                    print(date+" 3")

                    for asteroid in asteroids:
                        asteroid_dict = define_asteroid(asteroid, date)
                        # Serialize the dictionary in JSON format
                        asteroid_json = json.dumps(asteroid_dict)
                        # Encode the JSON in bytes
                        message_value = asteroid_json.encode('utf-8')
                        # Send dictionary asteroid
                        producer.produce('asteroid', message_value, callback=delivery_callback)
            url = data["links"]["next"]
            print(url)
        count += 1

    print(today)
    # Block until the messages are sent.
    producer.poll(10000)
    producer.flush()