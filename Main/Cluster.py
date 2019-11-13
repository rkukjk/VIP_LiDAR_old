from Point import *
from decimal import Decimal

class Cluster:

    # Cluster class has a list (may be changed to a different data structure) to keep all the points that belong to that
    # cluster
    def __init__(self):
        self.point_list = list()
        self.centroid_longitude = Decimal(0.00)
        self.centroid_latitude = Decimal(0.00)
        self.centroid_altitude = Decimal(0.00)
        self.avg_retro = Decimal(0.00)
        self.num_of_points = 0

    # This function adds a point to the point list.
    def add_point(self, point: Point):
        self.point_list.append(point)
        self.num_of_points += 1

        # Calculate new centroid of cluster
        self.centroid_longitude, self.centroid_latitude, self.centroid_altitude = self.centroid()

        # Calculate the new average retro value
        self.avg_retro = self.retro_average()


    # This function calculates the centroid of the cluster. This could be improved by using the median of a data set
    # instead of the average
    def centroid(self):
        long_avg = 0
        lat_avg = 0
        alt_avg = 0

        for point in self.point_list:
            long_avg = long_avg + point.longitude
            lat_avg = lat_avg + point.latitude
            alt_avg = alt_avg + point.altitude

        long_avg = long_avg / self.num_of_points
        lat_avg = lat_avg / self.num_of_points
        alt_avg = alt_avg / self.num_of_points

        rv = (long_avg, lat_avg, alt_avg)

        return rv

    # This  method calculates the average retro value
    def retro_average(self):
        retro_avg = Decimal(0.00)

        for point in self.point_list:
            retro_avg = retro_avg + point.retro

        retro_avg = retro_avg / self.num_of_points

        return retro_avg