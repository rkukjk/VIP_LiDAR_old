from Point import *
from decimal import *
from ClusterManager import *
from Cluster import *
from Camera import *
import pyproj
import csv


if __name__ == '__main__':

    # row = ["2000000", "-84.452865269", "33.881385968", "278.7242", "-0.61897", "4.322", "0.224", "69034.00499"]
    # p1 = Point(int(row[0]), Decimal(row[1]), Decimal(row[2]), Decimal(row[3]), Decimal(row[4]), Decimal(row[5]), Decimal(row[6]), Decimal(row[7]))
    #
    # row = ["2000001", "-84.452865269", "33.881385968", "278.7242", "-0.61897", "4.322", "0.255", "69034.00499"]
    # p2 = Point(int(row[0]), Decimal(row[1]), Decimal(row[2]), Decimal(row[3]), Decimal(row[4]), Decimal(row[5]),
    #            Decimal(row[6]), Decimal(row[7]))
    #
    # cluster_manager = ClusterManager()
    #
    # cluster_manager.insert_into_cluster(p1)
    # cluster_manager.insert_into_cluster(p2)
    #
    # # print(len(cluster_manager.cluster_list))
    #
    # print(cluster_manager.cluster_list[0].avg_retro)

    camera = Camera('coords.csv')


    point_long = Decimal('-84.45498008')
    point_lat = Decimal('33.88435326')

    print(camera.get_closest_pic(point_long, point_lat))