from Sign import *
import pandas as pd


class SignManager:
    """
    This class manages all the signs along with the algorithms to determine which clusters are signs. Each algo will
    take in a list of clusters and determine if a cluster is a sign. They will output a list of signs.
    """
    def __init__(self):
        self.sign_list = list()


    def add_sign(self, sign: Sign):
        self.sign_list.append(sign)

    # This is a very basic algo. If a cluster has more than 20 points, then it is classified as a sign
    def num_points(self, cluster_list):
        sign_list = []
        # Loop through each cluster
        for cluster in cluster_list:
            if cluster.num_of_points >= 20:
                sign = Sign(Cluster)
                sign_list.append(sign)

    # This method creates a dataframe from the list of signs
    def convert_signlist_to_dataframe(self, sign_list):
        data = []
        for sign in sign_list:
            temp_list = []
            temp_list.append(sign.index())  # Sign_ID - Do I need to make this a formal attribute?
            temp_list.append(sign.centroid_easting)  # centroid_easting
            temp_list.append(sign.centroid_northing)  # centroid_northing
            temp_list.append(sign.centroid_altitude)  # centroid_altitude
            temp_list.append(sign.avg_retro)  # avg_retro
            temp_list.append(sign.centroid_longitude)  # centroid_long
            temp_list.append(sign.centroid_latitude)  # centroid_lat
            temp_list.append(sign.num_of_points)  # num_of_points
            temp_list.append(sign.picture)  # pic_num

            data.append(temp_list)

        df = pd.DataFrame(data, columns=['Sign_Id', 'Easting', 'Northing', 'Altitude', 'Retro' 'Long', 'Lat', 'Num_of_Points', 'Pic_Num'])

        return df