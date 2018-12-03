import math
import operator


def closest_x_destinations(all_locations, num_of_deliveries):
    d0 = [0, 0]
    distance_to_destinations = []

    def distance(p0, p1):
        return math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)

    for x in all_locations:
        if not distance(d0, x).is_integer():
            distance_to_destinations.append(round(distance(d0, x), 3))
        else:
            distance_to_destinations.append(round(distance(d0, x)))

    locations_distance_tuple = [tuple(l) for l in all_locations]

    distance_dict = dict(zip(locations_distance_tuple, distance_to_destinations))

    sorted_distance_dict = sorted(distance_dict.items(), key=operator.itemgetter(1))

    first_n_closest = sorted_distance_dict[:num_of_deliveries]

    return [item[0] for item in first_n_closest]


# Test Input
all_locations = [[1, 2], [1, -1], [3, 4]]
num_of_deliveries = 2

print(closest_x_destinations(all_locations, num_of_deliveries))