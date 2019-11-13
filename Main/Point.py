from decimal import Decimal

class Point:

    def __init__(self, point_index, easting, northing, retro, angle, utc, long, lat, alt, distance):
        self.point_index = point_index
        self.longitude = long
        self.latitude = lat
        self.altitude = alt
        # Should I convert to cartesian here on Point creation?
        self.x = easting
        self.y = northing

        self.angle = angle
        self.distance = distance
        self.retro = retro
        self.timestamp = utc

    # toString method
    def __str__(self):
        return "Point has the following characteristics: Index: {}, GPS Coordinates: {}, {}, {} , Angle: {}, " \
               "Distance: {}, Retro: {}, Timestamp: {}".format(self.point_index, self.latitude, self.longitude,
                                                              self.altitude, self.angle, self.distance, self.retro,
                                                              self.timestamp)
