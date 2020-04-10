# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
import csv


class City:

    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return f"< City: {self.name}, {self.lat}, {self.lon} >"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list

    with open("cities.csv", newline="") as csvfile:

        # Create our reader
        reader = csv.reader(csvfile)

        # =============================================================
        # In order to dynamically find our class's needed attributes,
        # We can look at the first line to find our attr names.
        # Whatever index our attr names are at on the first row
        #     is the same index we can use for all other rows.
        #
        # Example:
        #     first row:  ['city',       'extra', 'lat', 'lon', 'pop']
        #     second row: ['carrollton', 'texas', '45',  '120', '45]
        #
        #     By looking at the first row,
        #         we know that all other rows will have the
        #         'city', 'lat', and 'lon' at indices 0, 2, and 3.
        #
        # We could hardcode these values in, but this first_line search
        #     makes the search dynamic, in case the csv file changes.
        # =============================================================
        first_line = True
        index_values = []

        for row in reader:
            if first_line:
                index_values = [
                    i for i, val in enumerate(row) if val in ["city", "lat", "lng"]]
                first_line = False
            else:
                name = row[index_values[0]]
                lat = float(row[index_values[1]])
                lon = float(row[index_values[2]])
                cities.append(City(name, lat, lon))

    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def display_example():
    print("   [X][ ][ ][ ]                       [ ][ ][ ][X]  ")
    print("   [ ][ ][ ][ ]                       [ ][ ][ ][ ]  ")
    print("   [ ][ ][ ][ ]                       [ ][ ][ ][ ]  ")
    print("   [ ][ ][ ][X]                       [X][ ][ ][ ]  ")
    print("upper-left/lower-right           upper-right/lower-left\n")
    print("Please enter latitude and longitude of the lower-left/upper-right corners")
    print("or the upper-left/lower-right corners of an area you would like to search.")
    print("Your input should be \"lat, lon\"")
    print("Example input: \"45, -120\"\n")

from os import system
from time import sleep

def get_corner():
    while True:
        system("cls||clear")
        display_example()
        user_in = input("Please enter one corner >>")
        try:
            return user_in.split(", ")
        except:
            print("Invalid input. Please try again.")
            sleep(0.8)


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    # TODO Ensure that the lat and lon valuse are all floats
    # Go through each city and check to see if it falls within
    # the specified coordinates.

    return within

# corner1 = get_corner()
# corner2 = get_corner()
# cities_within = cityreader_stretch(corner1[0], corner1[1], corner2[0], corner2[1])

