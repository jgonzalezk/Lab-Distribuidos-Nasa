from urllib.parse import parse_qs, urlparse
from datetime import datetime
from kafka import KafkaProducer
import requests
import json
import sys

if __name__ == '__main__':

     # Create Producer instance
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    def delivery_callback(err, msg):
        if err is not None:
            print(f'ERROR: Message failed delivery: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

    def define_asteroid(asteroid, date):

        estimated_diameter_meters = asteroid["estimated_diameter"]["meters"]
        estimated_diameter_min = estimated_diameter_meters["estimated_diameter_min"]
        estimated_diameter_max = estimated_diameter_meters["estimated_diameter_max"]
        
        close_approach_data = asteroid["close_approach_data"][0]
        orbiting_body =close_approach_data["orbiting_body"]
        relative_velocity_KpS = close_approach_data["relative_velocity"]["kilometers_per_second"]

        asteroid_dict = {
            "ID": asteroid["id"],
            "Name": asteroid["name"],
            "Date": date,
            "Absolute_magnitude_h": asteroid["absolute_magnitude_h"],
            "Is_potentially_hazardous_asteroid": asteroid["is_potentially_hazardous_asteroid"],
            "Estimated_diameter_met_min": estimated_diameter_min,
            "Estimated_diameter_met_max": estimated_diameter_max,
            "Orbiting_body": orbiting_body,
            "Relative_velocity_KpS": relative_velocity_KpS,
            "Is_sentry_object": asteroid["is_sentry_object"]
        }
        return asteroid_dict
    
    def define_url(start_date_str, end_date_str, api_key):
        # Get url
        return f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date_str}&end_date={end_date_str}&api_key={api_key}'
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
    api_key = 'izjbQge0O64wnofaQHB8PeYljVFl8Nzmh2yYRwNF'
    url = define_url('2023-07-09', '2023-07-15', api_key)
    print(url)
    # Flag to end while when data is from today
    close = False
    while ( to_date(get_start_date(url)) <= today and close == False):
        
        if to_date(get_end_date(url)) == today:

            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                near_earth_objects = data["near_earth_objects"]

                for date in near_earth_objects:
                    asteroids = near_earth_objects[date]
                    for asteroid in asteroids:
                        try:
                            asteroid_dict = define_asteroid(asteroid, date)
                            print(asteroid_dict)
                            # Serialize the dictionary in JSON format
                            asteroid_json = json.dumps(asteroid_dict)
                            # Encode the JSON in bytes
                            message_value = asteroid_json.encode('utf-8')
                            # Send dictionary asteroid
                            producer.send('asteroid', message_value).add_callback(delivery_callback)
                        except Exception as e:
                            id = asteroid["id"]
                            print(f"OjO: json del asteroide con id: {id} en la fecha: {date}, esta defectuoso. Error en parametro: {str(e)}. Asteroide no guardado")
                            continue # Ignore the faulty asteroid and continue
                close = True   
            except requests.exceptions.RequestException as e:
                print(f"Error al realizar la solicitud: {e}. URL: {url}")
                sys.exit()
            except ValueError as e:
                print(f"Error al analizar JSON: {e}. URL: {url}")
                sys.exit()
            except Exception as e:
                print(f"Error inesperado:: {e}. URL: {url}")
                sys.exit()

        elif to_date(get_end_date(url)) > today:

            url = define_url( to_date(get_start_date(url)).strftime('%Y-%m-%d'), today.strftime('%Y-%m-%d'), api_key)
            try:
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                near_earth_objects = data["near_earth_objects"]

                for date in near_earth_objects:
                    asteroids = near_earth_objects[date]

                    for asteroid in asteroids:
                        try:
                            asteroid_dict = define_asteroid(asteroid, date)
                            print(asteroid_dict)
                            # Serialize the dictionary in JSON format
                            asteroid_json = json.dumps(asteroid_dict)
                            # Encode the JSON in bytes
                            message_value = asteroid_json.encode('utf-8')
                            # Send dictionary asteroid
                            producer.send('asteroid', message_value).add_callback(delivery_callback)
                        except Exception as e:
                            id = asteroid["id"]
                            print(f"OjO: json del asteroide con id: {id} en la fecha: {date}, esta defectuoso. Error en parametro: {str(e)}. Asteroide no guardado")
                            continue # Ignore the faulty asteroid and continue
                close = True
            except requests.exceptions.RequestException as e:
                print(f"Error al realizar la solicitud: {e}. URL: {url}")
            except ValueError as e:
                print(f"Error al analizar JSON: {e}. URL: {url}")
                sys.exit()
            except Exception as e:
                print(f"Error inesperado:: {e}. URL: {url}")
                sys.exit()

        else:

            try:
                response = requests.get(url)   
                response.raise_for_status() 
                data = response.json()
                near_earth_objects = data["near_earth_objects"]
                
                for date in near_earth_objects:
                    # Information from the last date will not be saved, since the following url saves it
                    if date != get_end_date(url):
                        asteroids = near_earth_objects[date]

                        for asteroid in asteroids:
                            try:
                                asteroid_dict = define_asteroid(asteroid, date)
                                print(asteroid_dict)
                                # Serialize the dictionary in JSON format
                                asteroid_json = json.dumps(asteroid_dict)
                                # Encode the JSON in bytes
                                message_value = asteroid_json.encode('utf-8')
                                # Send dictionary asteroid
                                producer.send('asteroid', message_value).add_callback(delivery_callback)
                            except Exception as e:
                                id = asteroid["id"]
                                print(f"OjO: json del asteroide con id: {id} en la fecha: {date}, esta defectuoso. Error en parametro: {str(e)}. Asteroide no guardado")
                                continue # Ignore the faulty asteroid and continue
                url = data["links"]["next"]
            except requests.exceptions.RequestException as e:
                print(f"Error al realizar la solicitud: {e}. URL: {url}")
                sys.exit()
            except ValueError as e:
                print(f"Error al analizar JSON: {e}. URL: {url}")
                sys.exit()
            except Exception as e:
                print(f"Error inesperado:: {e}. URL: {url}")
                sys.exit()

    # Block until the messages are sent.
    producer.flush()
    print("Proceso finalizado exitosamente \(^o^)/")