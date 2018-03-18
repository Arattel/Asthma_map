import requests
import json

#Example with Open Weather Map
response1 = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=London,us&mode=json&appid=b4a90387458cb975bafe21c7c9ea0737')
print(json.loads(response1.content))

#Example with Google Geocoding API
response2 = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyAhBzKOrjhfJO22CLf7uNzW8hF57z9EmdI')
print(json.loads(response2.content))