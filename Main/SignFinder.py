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
import math
import pandas as pd


# Rounding Function
def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

if __name__ == '__main__':
    # # Command line arg code
    # parser = argparse.ArgumentParser(description='Finding Signs in LiDAR data!')
    # parser.add_argument("--i", help = "Input file.")
    # parser.add_argument("--o", help = "Output file")
    # input_file = args.i
    # output_file = args.o
    # if input_file is None:
    #     input_file = input("Enter input file: ")
    #
    # if output_file is None:
    #     output_file = input("Enter output file: ")

    # Global variables
    # cluster_list = []

    # Reading in data into a dataframe and formatting it.
    df = pd.read_csv('E:/School/VIP/Data/LiDAR_Data/original/XYZ/V_20180816_I285_EB_run1(0)_2nd_leg.txt', sep = " ")
    df = df.astype({'ID': int})
    # TODO: Figure out how to read in data with only a certain number of demicals. This takes a lot of time.
    df['Easting'] = df['Easting'].apply(round_half_up)
    df['Northing'] = df['Northing'].apply(round_half_up)
    df['Altitude'] = df['Altitude'].apply(round_half_up)
    df['Retro'] = df['Retro'].apply(round_half_up)

# ========================================== Filtering ===============================================================
    # Filtering by Retro values
    df = df.loc[df['Retro'] > 0.7]
    df = df.reset_index(drop=True)
# ====================================================================================================================


# ========================================= Clustering ===============================================================
    cluster_manager = ClusterManager()
    cluster_manager.cluster_list = cluster_manager.progressive_kdmean(df)
# ====================================================================================================================


# ========================================== Classifying =============================================================
    sign_manager = SignManager()
    sign_manager.sign_list = sign_manager.num_points(cluster_manager.cluster_list)
# ====================================================================================================================


# ========================================== Adding photos ===========================================================
    # Get the picture number that corresponds to each sign
    camera = Camera('E:/School/VIP/Data/LiDAR_Data/coords/coords.csv')
    for sign in sign_manager.sign_list:
        pic_num = camera.get_closest_pic(sign.centroid_longitude, sign.centroid_latitude)
        pic_num -= 2
        sign.add_pic(pic_num)
# ====================================================================================================================


# ======================================== Book keeping and output files =============================================
    sign_list_df = sign_manager.convert_signlist_to_dataframe(sign_manager.sign_list)

    sign_list_df.to_csv('sign_list_output.csv', index = False)