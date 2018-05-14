# Brief characteristics of a program

This program is created to help people with asthma to find a place with better climate to spend some time, when they want to have a kind of remission. It finds an ideal place near the place of living or the place with the best weather in given radius. 

## Input and output data

Input data:

1) City/town
2) Country
3) Radius of search or 0 if radius doesn't matter

Output data:

1) City with better weather 
2) Distance to it. 

## Program structure

##### point.py:
 
 class Point - represents a geographical point
 
 .find_distance(another_point) - finds a distance to another point
 
 .weather_forecast() - This method inputs  name of a city and outputs list of tuples ( humidity, temperature)
 
 .is_good()- This method returns True only if weather in given point fits humidity and temperature criterias
 
 
 ##### possible_points.py
 
 class PossiblePoints - This class is created to represent point collection
 
 .add_point(point) -  This method adds a point into PossiblePoints instance
 
 .distance_list(point, radius) - This method creates a sorted list of points and distances from point to argument point
 
 
##### read_csv.py

###### functions:

read_csv

This function reads a .csv file and returns PossiblePoints object


find_best_coord

This function inputs a city, its latitude, its longitude and radius of search and returns a best city to live in given radius

find_best

This function inputs city name and radius and finds a best possible city inside radius
    
 main
 
 This function find a best place and outputs it
 
 # How to use this program
 
You just need to launch read_csv.py and enter data

## Test cases


Enter data:

1) Lviv
2) Ukraine
3) 120


You'll see result.