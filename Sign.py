from ClusterManager import *
from Cluster import *

class Sign:
    """
    This class will hold the points associated to that sign along with a picture id. Now I'm thinking I will just pass
    over the clusters and their data.
    """


    def __init__(self, cluster: Cluster):
        self.point_list = cluster.point_list
        self.centroid_longitude = cluster.centroid_longitude
        self.centroid_latitude = cluster.centroid_latitude
        self.centroid_altitude = cluster.centroid_altitude
        self.avg_retro = cluster.avg_retro
        self.num_of_points = cluster.num_of_points

        # Assign a picture to the sign here.
        self.picture = "None"