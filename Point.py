from decimal import Decimal

class Point:

    def __init__(self, point_index, long, lat, alt, angle, distance, retro, utc):
        self.point_index = point_index
        self.latitude = lat
        self.longitude = long
        self.altitude = alt
        # Should I convert to cartesian here on Point creation?
        self.x = None
        self.y = None
        self.z = None

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
