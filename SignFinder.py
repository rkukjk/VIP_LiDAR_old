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
import argparse


# Rounding Function
def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

if __name__ == '__main__':
    # Command line arg code
    parser = argparse.ArgumentParser(description='Finding Signs in LiDAR data!')
    parser.add_argument("--i", help = "Input file.")
    parser.add_argument("--o", help = "Output file")
    input_file = args.i
    output_file = args.o
    if input_file is None:
        input_file = input("Enter input file: ")

    if output_file is None:
        output_file = input("Enter output file: ")

    # Reading in data into a dataframe and formatting it.
    df = pd.read_csv(input_file, sep = " ")
    df = df.astype({'ID': int})
    # TODO: Figure out how to read in data with only a certain number of demicals. This takes a lot of time.
    df['Easting'] = df['Easting'].apply(round_half_up)
    df['Northing'] = df['Northing'].apply(round_half_up)
    df['Altitude'] = df['Altitude'].apply(round_half_up)
    df['Retro'] = df['Retro'].apply(round_half_up)

# ========================================== Filtering ===============================================================







# ====================================================================================================================



# ========================================= Clustering ===============================================================

# ====================================================================================================================




# ========================================== Classifying =============================================================

# ====================================================================================================================



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


    # Code for visualizing the point cloud. Just used for teting. This is some janky code. Do something better than this
    # I will redo this. I just need to hurry up and finish this
    while True:
        sign_id = int(input("Please enter the sign_id you want to plot"))
        df = sign_manager.sign_list[sign_id].convert_sign_to_panda_dataframe(sign_manager.sign_list[sign_id], sign_id)
        df = df.groupby('sign_id')
        df = df.get_group(sign_id)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        x = []
        y = []
        z = []
        for row in df.iterrows():
            index = row[0]
            value = row[1]

            x.append(value['long'])
            y.append(value['lat'])
            z.append(value['alt'])

        ax.scatter(x, y, z, s=3, c='r', marker='o')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')

        plt.show()