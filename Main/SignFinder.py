from Point import *
from Cluster import *
from ClusterManager import *
from Sign import *
from SignManager import *
from Camera import *
from decimal import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv


if __name__ == '__main__':

    # This chunk of code will read the csv in row by row and create a list of points. I can go ahead and filter out
    # by Ra value at this stage so as to not have to load in ALLLLL that data in a pd data frame to begin with.
    csv_file = open('UTMNew.csv', 'r')
    reader = csv.reader(csv_file)

    retro_threshold = 0.7

    row_num = 0
    point_list = list()
    for row in reader:
        # If not the header row and if the retro-intensity is greater than our threshold, the create a point object.
        if row_num != 0 and Decimal(row[3]) >= Decimal(0.7):
            p = Point(int(row[0]), float(row[1]), float(row[2]), Decimal(row[3]), Decimal(row[4]), Decimal(row[5]), Decimal(row[6]), Decimal(row[7]), Decimal(row[8]), Decimal(row[9]))
            point_list.append(p)
        row_num += 1

    csv_file.close()


    # Custom Clustering Algo
    # Loop through points and start assigning them to clusters. Look at csv's to find adequate tolerances for clustering
    cluster_manager = ClusterManager()
    for point in point_list:
        # Put in a cluster
        cluster_manager.insert_into_cluster(point)

    # Now that I have my clusters, I can go through and verify that they are signs.
    # For now, I filter by cluster size.
    sign_manager = SignManager()
    for cluster in cluster_manager.cluster_list:
        if cluster.num_of_points >= 20:
            sign = Sign(cluster)
            sign_manager.add(sign)

    # Get the picture number that corresponds to each sign
    camera = Camera('coords.csv')
    for sign in sign_manager.sign_list:
        pic_num = camera.get_closest_pic(sign.centroid_longitude, sign.centroid_latitude)
        pic_num -= 2
        sign.picture = pic_num

    # Preliminary new output file format
    txt_file = open('output_big.txt', 'w')

    print(len(sign_manager.sign_list))

    for s in sign_manager.sign_list:
        for p in s.point_list:
            line = str(p.x) + ' ' + str(p.y) + ' ' + str(p.altitude) + ' ' + str(p.retro) + '\n'
            txt_file.write(line)

    txt_file.close()

    # # Code to write out to a csv for verifying
    # csv_data = [['Sign_ID', 'sign_centroid_long', 'sign_centroid_lat', 'sign_centroid_alt', 'avg_retro', 'num_of_points', 'pic_num']]
    #
    # # Put all sign info into csv_data
    # for i in range(len(sign_manager.sign_list)):
    #     sign_info = [i, sign_manager.sign_list[i].centroid_longitude, sign_manager.sign_list[i].centroid_latitude,
    #                  sign_manager.sign_list[i].centroid_altitude, sign_manager.sign_list[i].avg_retro, sign_manager.sign_list[i].num_of_points,
    #                  sign_manager.sign_list[i].picture]
    #     csv_data.append(sign_info)
    #
    # # Actually writing to csv
    # csv_file = open('output.csv', 'w')
    # writer = csv.writer(csv_file, lineterminator='\n')
    #
    # for i in range(len(csv_data)):
    #     writer.writerow(csv_data[i])
    #
    # csv_file.close()
    #
    #
    # # Code for visualizing the point cloud. Just used for teting. This is some janky code. Do something better than this
    # # I will redo this. I just need to hurry up and finish this
    # while True:
    #     sign_id = int(input("Please enter the sign_id you want to plot"))
    #     df = sign_manager.sign_list[sign_id].convert_sign_to_panda_dataframe(sign_manager.sign_list[sign_id], sign_id)
    #     df = df.groupby('sign_id')
    #     df = df.get_group(sign_id)
    #     fig = plt.figure()
    #     ax = fig.add_subplot(111, projection='3d')
    #
    #     x = []
    #     y = []
    #     z = []
    #     for row in df.iterrows():
    #         index = row[0]
    #         value = row[1]
    #
    #         x.append(value['long'])
    #         y.append(value['lat'])
    #         z.append(value['alt'])
    #
    #     ax.scatter(x, y, z, s=3, c='r', marker='o')
    #     ax.set_xlabel('X Label')
    #     ax.set_ylabel('Y Label')
    #     ax.set_zlabel('Z Label')
    #
    #     plt.show()