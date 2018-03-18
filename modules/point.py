from math import radians, sin, cos, sqrt, asin
import pyowm


class Point(object):
    """
    This class is used to represent a geographical point with latitude and longitude
    """

    def __init__(self, name, lat, lon):
        """
        (Point, float, float) -> None
        This method creates a Point object instance
        """
        self.name = name
        self.lat = lat
        self.lon = lon
        self.delta = 0

    def __str__(self):
        """
        (Point) -> (str)
        This method is used for string representation of Point instance
        """
        return '{0},{1},{2}'.format(self.name, self.lat, self.lon)

    def find_distance(self, another_point):
        """
        (Point, Point) -> (float)
        This method is used to find distance between 2 point objects
        """
        r = 6371
        lat1, lat2 = self.lat, another_point.lat
        lon1, lon2 = self.lon, another_point.lon
        delta_lat = radians(lat2 - lat1)
        delta_lon = radians(lon2 - lon1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)
        a = sin(delta_lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
        c = 2 * asin(sqrt(a))
        return r*c

    def weather_forecast(self):
        """
        (str) -> (list)
        This function inputs  name of a city and outputs list of tuples ( humidity, temperature)
        """
        owm = pyowm.OWM('b4a90387458cb975bafe21c7c9ea0737')
        fc = owm.three_hours_forecast(self.name)
        weather_lst = []
        time = pyowm.timeutils.next_three_hours()
        while True:
            try:
                if int(str(time)[11:13]) > 8 and int(str(time)[11:13]) < 22:
                    weather_lst.append((fc.get_weather_at(time).get_humidity(),
                                        fc.get_weather_at(time).get_temperature('celsius')['temp']))
                time = pyowm.timeutils.next_three_hours(time)
            except:
                break
        return weather_lst

    def is_good(self):
        """
        (Point) -> (bool)
        This method returns True only if weather in given point fits humidity and temperature criterias
        """
        isgood = True
        weather = self.weather_forecast()
        for i, j in weather:
            if i > 80 or i < 50 or j < 8 or j > 30:
                isgood = False
                self.delta += abs(65 - i) + abs(20 - j)
        return isgood


if __name__ == "__main__":
    k = Point('Drohobych', 49.358012, 23.512319 )
    print(k.is_good())
    print(k.delta)
