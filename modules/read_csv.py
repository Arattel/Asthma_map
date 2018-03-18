from point import Point
from possible_points import PossiblePoints
import pandas
import googlemaps
import time


def read_csv(name = 'simplemaps-worldcities-basic.csv'):
    """
    (str) -> (PossiblePoints)
    This function reads a .csv file and returns PossiblePoints object
    """
    points_data = pandas.read_csv(name)
    possible = PossiblePoints()
    cities = points_data['city_ascii']
    latitudes = points_data['lat']
    longitudes = points_data['lng']
    for i in range(len(cities)):
        possible.add_point(Point(cities[i], latitudes[i], longitudes[i]))
    return possible


def find_best_coord(city, lat, lng, radius):
    """
    (str, float, float) -> (str)
    This function inputs a city, its latitude, its longitude and radius of search and returns a best city to live in
    given radius
    """
    cities_500km = read_csv().distance_list(Point(city, lat, lng), radius=radius)
    result = []
    for x in cities_500km:
        try:
            is_good = x[0].is_good()
            if is_good:
                return x[0].name
            result.append(x[0])
        except:
            pass
    result = min(result, key=lambda x: x.delta)
    return "{0}, {1} km away".format(result.name, round(result.find_distance(Point(city, lat, lng)), 2))


def find_best(city, radius):
    """
    (str, float) -> (str)
    This function inputs city name and radius and finds a best possible city inside radius
    """
    gmaps = googlemaps.Client(key='AIzaSyAhBzKOrjhfJO22CLf7uNzW8hF57z9EmdI')
    geocode_result = gmaps.geocode(city)
    coord = geocode_result[0]['geometry']['location']
    return find_best_coord(city, coord['lat'], coord['lng'], radius)


def input_city_radius():
    """
    () -> (str, float)
    This function inputs city and radius
    """
    city = input('Please, input city: ')
    country = input('Please, input country: ')
    address = "{0}, {1}".format(city, country)
    radius = float(input("Please, input radius: "))
    return (address, radius)

def main():
    """
    () -> None
    This function find a best place and outputs it
    """
    city, radius = input_city_radius()
    print(find_best(city, radius))
main()