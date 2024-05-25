import requests
import json
import sys
from haversine import haversine

# the required parameters on the command line
country1 = sys.argv[1]
country2 = sys.argv[2]

# the expected schema of the returned JSON
schema = {
    "capital_city": {
        "type": "string",
        "description": "The name of the capital city"
        },
    "latitude": {
        "type": "float",
        "description": "Decimal latitude of the capital city"
        },
    "longitude": {
        "type": "float",
        "description": "Decimal longitude of the capital city"
        }

}

# using mistral here, but you can use and compare many different models and choose the most appropriate
model = "mistral"
# Let's put our countries in a dict
countries=[]
countries.append(country1)
countries.append(country2)
# Let's initiate the cities_info dict
cities_info=[]

# This is a function that check the city_info returned by the llm agains the schema, 
# returns trus while it's all good, False when not. On false, the llm request will be repeated.
# The type verification could be enhanced with pydantic objects.

def is_valid_city_info(city_info, schema):
    try:
        if not isinstance(city_info, dict):
            return False
        for key, value in schema.items():
            if key not in city_info:
                return False
            if not isinstance(city_info[key], (float if value["type"] == "float" else str)):
                return False
        return True
    except Exception as e:
        print(f"Validation error: {e}")
        return False

# This is a function that takes a country as input - maybe it should be checked against a canonical list of countries. 
# It calls the ollama model on port 11434 of localhost. This should be factored out as parameters in a config file. 
# It returns a JSON according to the schema. For that, you can see how to put a straightjacket prompt. Change any of this
# to measure how wild it can be. 

def get_city_info(country):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "you are a helpful AI assistant. The user will enter the name of a country and the assistant will provide the \
            decimal latitude and decimal longitude of the capital city of the country. Output must be in JSON using the schema defined here {schema} according to the following example."},
            {"role": "assistant", "content": "{\"capital_city\": \"Paris\", \"latitude\": 48.8566, \"longitude\": 2.3522}"},
            {"role": "user", "content": country},
        ],
        "options": {
            "temperature": 0.0
        },
        "format": "json",
        "stream": False
    }

# Main loop, holding True until proper answers are provided. 
# Trials shoud be limited as it could go on for ever. 
# Some unnecessary extra tests are put in, you can take them out once you are pretty sure it works.
    
    while True:    
        try:
            response = requests.post("http://localhost:11434/api/chat", json=payload)
            response.raise_for_status()
            city_info = response.json()["message"]["content"]
            city_info = json.loads(city_info)
            if is_valid_city_info(city_info, schema):
                return city_info
            else:
                print(f"Invalid city info received: {city_info}. Retrying...")
            
        except requests.exceptions.RequestException as e:
            print(f"HTTP Request failed: {e}")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            sys.exit(1)
        except KeyError as e:
            print(f"Key error: {e}")
            sys.exit(1)
        
# We have new retrieved city_info , i.e. the name of the capital city and its coordinates,
# Let go and calculate the distance in km using haversine. Note that the type of the JSON must
# be respected to perform the operation.

for country in countries:
    city_info = get_city_info(country)
    print(f"Retrieved city info for {country}: {city_info}")
    cities_info.append(city_info)

city1 = cities_info[0]
city2 = cities_info[1]

city1_coords = (city1["latitude"], city1["longitude"])
city2_coords = (city2["latitude"], city2["longitude"])

print(f"City 1: {city1}")  # Debug print
print(f"City 2: {city2}")  # Debug print

distance = haversine(city1_coords, city2_coords)

print(f"The distance between {city1['capital_city']} and {city2['capital_city']} is {int(round(distance, -1))} km")

# Have fun and kick butts
