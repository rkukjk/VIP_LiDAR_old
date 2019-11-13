from ClusterManager import *
from Cluster import *
import pandas as pd

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
        self.picture = -1

    def convert_sign_to_panda_dataframe(self, sign, index):
        data = []
        for point in sign.point_list:
            temp_list = []
            temp_list.append(index) # Sign_ID - Do I need to make this a formal attribute?
            temp_list.append(float(point.point_index))
            temp_list.append(float(point.longitude))
            temp_list.append(float(point.latitude))
            temp_list.append(float(point.altitude))
            temp_list.append(float(point.angle))
            temp_list.append(float(point.distance))
            temp_list.append(float(point.retro))
            temp_list.append(float(point.timestamp))

            data.append(temp_list)

        df = pd.DataFrame(data, columns = ['sign_id', 'point_index', 'long', 'lat', 'alt', 'angle', 'distance', 'retro', 'timestamp'])

        return df