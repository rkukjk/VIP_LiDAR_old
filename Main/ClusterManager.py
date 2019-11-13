from Point import *
from Cluster import *

class ClusterManager:
    """
    This class manages all the clusters that we are going to make. As it stands, it just saves it's clusters in a list.
    I can optimize this later.
    """

    def __init__(self):
        self.cluster_list = list()


    # This method takes a point and finds the cluster that it belongs to.
    def insert_into_cluster(self, point: Point):
        lat_tolerance = Decimal("0.00002")
        long_tolerance = Decimal("0.00002")
        alt_tolerance = Decimal("1.60000")
        retro_tolerance = Decimal("0.5")

        if self.cluster_list == []:
            c = Cluster()
            c.add_point(point)
            self.cluster_list.append(c)
        else:
            # see if it falls within a certain range
            count = 0
            inserted = False
            while not inserted and count < len(self.cluster_list):
                c = self.cluster_list[count]

                lat_lower_bound = c.centroid_latitude - lat_tolerance
                lat_upper_bound = c.centroid_latitude + lat_tolerance
                long_lower_bound = c.centroid_longitude - long_tolerance
                long_upper_bound = c.centroid_longitude + long_tolerance
                alt_lower_bound = c.centroid_altitude - alt_tolerance
                alt_upper_bound = c.centroid_altitude + alt_tolerance
                retro_lower_bound = c.avg_retro - retro_tolerance
                retro_upper_bound = c.avg_retro + retro_tolerance

                if lat_lower_bound <= point.latitude <= lat_upper_bound and long_lower_bound <= point.longitude <= long_upper_bound and \
                        alt_lower_bound <= point.altitude <= alt_upper_bound and retro_lower_bound <= point.retro <= retro_upper_bound:

                    c.add_point(point)
                    inserted = True
                else:
                    count += 1

            if not inserted:
                c = Cluster()
                c.add_point(point)
                self.cluster_list.append(c)