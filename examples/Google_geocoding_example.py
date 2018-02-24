import googlemaps

gmaps = googlemaps.Client(key='AIzaSyAhBzKOrjhfJO22CLf7uNzW8hF57z9EmdI')

geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
print(geocode_result[0]['geometry']['location'])
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))
print(reverse_geocode_result[0]['address_components'][2]['long_name'])

