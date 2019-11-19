from Cluster import *
import pandas as pd

class ClusterManager:
    """
    This class manages all the clusters that we are going to make along wth all the clustering algorithms. As it stands,
    it just saves it's clusters in a list. I can optimize this later.
    """

    def __init__(self):
        self.cluster_list = list()


    # This method will go point by point and insert them into clusters. Only input is dataframe. Return value is a list
    # of clusters
    def progressive_kdmean(self, df):
        easting_tolerance = 1.0
        northing_tolerance = 1.0
        alt_tolerance = 1.0
        retro_tolerance = 0.5

        cluster_list = []

        for index, row in df.iterrows():

            if cluster_list == []:
                c_df = pd.DataFrame(columns = df.columns)
                c = Cluster(c_df)
                c.add_point(row)
                cluster_list.append(c)
            else:
                # see if it falls within a certain range
                count = 0
                inserted = False
                while not inserted and count < len(self.cluster_list):
                    c = cluster_list[count] #c is a cluster

                    easting_lower_bound = c.centroid_easting - easting_tolerance
                    easting_upper_bound = c.centroid_easting + easting_tolerance
                    northing_lower_bound = c.centroid_northing - northing_tolerance
                    northing_upper_bound = c.centroid_northing + northing_tolerance
                    alt_lower_bound = c.centroid_altitude - alt_tolerance
                    alt_upper_bound = c.centroid_altitude + alt_tolerance
                    retro_lower_bound = c.avg_retro - retro_tolerance
                    retro_upper_bound = c.avg_retro + retro_tolerance

                    if easting_lower_bound <= row['Easting'] <= easting_upper_bound and northing_lower_bound <= row['Northing'] <= northing_upper_bound and \
                            alt_lower_bound <= row['Altitude'] <= alt_upper_bound and retro_lower_bound <= row['Retro'] <= retro_upper_bound:

                        c.add_point(row)
                        inserted = True
                    else:
                        count += 1

                if not inserted:
                    c_df = pd.DataFrame(columns=df.columns)
                    c = Cluster(c_df)
                    c.add_point(row)
                    cluster_list.append(c)

        return cluster_list
