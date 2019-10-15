from Point import *
from Cluster import *
from ClusterManager import *
from Sign import *
from SignManager import *
from decimal import *
import csv


if __name__ == '__main__':

    # This chunk of code will read the csv in row by row and create a list of points. I can go ahead and filter out
    # by Ra value at this stage so as to not have to load in ALLLLL that data in a pd data frame to begin with.
    csv_file = open('V_20180816_I285_EB_run1(0)_2nd_leg.csv', 'r')
    reader = csv.reader(csv_file)

    retro_threshold = 0.7

    row_num = 0
    point_list = list()
    for row in reader:
        # If not the header row and if the retro-intensity is greater than our threshold, the create a point object.
        if row_num != 0 and Decimal(row[6]) >= Decimal(0.7):
            p = Point(int(row[0]), Decimal(row[1]), Decimal(row[2]), Decimal(row[3]), Decimal(row[4]), Decimal(row[5]), Decimal(row[6]), Decimal(row[7]))
            point_list.append(p)
        row_num += 1

    csv_file.close()



    # Custom Clustering Algo
    # Loop through points and start assigning them to clusters. Look at csv's to find adequate tolerances for clustering
    cluster_manager = ClusterManager()
    for point in point_list:
        # Put in a cluster
        cluster_manager.insert_into_cluster(point)


    # Now that I have my clusters, I can go through and verify that they are signs. For now, I will do something simple
    # like filter by cluster size
    sign_manager = SignManager()
    for cluster in cluster_manager.cluster_list:
        if cluster.num_of_points >= 20:
            sign = Sign(cluster)
            sign_manager.add(sign)

    # Rough number of signs
    print(len(sign_manager.sign_list))
