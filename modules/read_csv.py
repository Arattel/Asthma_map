import folium
import googlemaps
import pandas

from point import Point
from possible_points import PossiblePoints


def read_csv(name='simplemaps-worldcities-basic.csv'):
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
                return x[0], Point(city, lat, lng)
            result.append(x[0])
        except Exception:
            pass
    result = min(result, key=lambda x: x.delta)
    return result, Point(city, lat, lng)


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


def create_template(cities, ind):
    start = cities[1]
    end = cities[0]
    map_1 = folium.Map(location=[start.lat, start.lon], zoom_start=5)
    folium.Marker([start.lat, start.lon], popup=start.name, icon=folium.Icon(icon='info-sign', color='red')).add_to(
        map_1)
    folium.Marker([end.lat, end.lon], popup=end.name, icon=folium.Icon(icon='info-sign', color='green')).add_to(map_1)
    folium.PolyLine([(start.lat, start.lon), (end.lat, end.lon)], color="green", weight=5, opacity=1,
                    popup=str(start.find_distance(end)) + ' km').add_to(map_1)
    map_1.save('templates/map{}.html'.format(ind))


if __name__ == '__main__':
    create_template(find_best('Lviv, Ukraine', 190))
