from Point import *
from decimal import *
from ClusterManager import *
from Cluster import *
from Camera import *
from Sign import *
import pyproj
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv


if __name__ == '__main__':
    # # Creating random points
    # p1 = ['2000000', '-84.45364898812', '33.88268998936', '281.397268', '0.73152', '-0.61897', '4.322', '0.224', '69034.00499']
    # p2 = ['2000001', '-84.454140107315', '33.883156407041', '288.718034931506', '0.77472602739726', '-0.61897', '4.322', '0.224','69034.00499']
    # point1 = Point(int(p1[0]), Decimal(p1[1]), Decimal(p1[2]), Decimal(p1[3]), Decimal(p1[4]), Decimal(p1[5]), Decimal(p1[6]), Decimal(p1[7]))
    # point2 = Point(int(p2[0]), Decimal(p2[1]), Decimal(p2[2]), Decimal(p2[3]), Decimal(p2[4]), Decimal(p2[5]), Decimal(p2[6]),Decimal(p2[7]))
    #
    # cluster = Cluster()
    # cluster.add_point(point1)
    # cluster.add_point(point2)
    #
    # sign = Sign(cluster)
    # df = sign.convert_sign_to_panda_dataframe(sign, 0)
    #
    # df = df.groupby('sign_id')
    # sign_to_plot = int(input("Please enter the sign_id you want to plot"))
    #
    # df = df.get_group(sign_to_plot)
    #
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    #
    # x = []
    # y = []
    # z = []
    # for row in df.iterrows():
    #     index = row[0]
    #     value = row[1]
    #
    #     x.append(value['long'])
    #     y.append(value['lat'])
    #     z.append(value['alt'])
    #
    # ax.scatter(x, y, z, s=3, c='r', marker='o')
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    #
    # plt.show()


    data = ['2000000', '735578.41', '3751924.73', '0.224', '-0.61897', '69034.00499', '-84.45286527', '33.88138597', '278.7242 4.322']
    line = data[0] + ' ' + data[1]

    print(line)


