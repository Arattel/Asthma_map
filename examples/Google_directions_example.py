import googlemaps
import json
from datetime import datetime

gmaps = googlemaps.Client(key='AIzaSyDfRTmsQoa-teVgFT7eX6zqJxqiMlThCBY')

# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)
print(directions_result[0]['legs'][0]['duration']['text'])