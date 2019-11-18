# Imports
import math
import pandas as pd
import argparse


# Rounding Function
def round_half_up(n, decimals=3):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


if __name__ == "__main__":
    # Command line arg code
    parser = argparse.ArgumentParser(description='Atutorial of argparse!')
    parser.add_argument("--i", help = "Input file. Should be the picking_list from CC. Make sure to include the whole path to the file along with the file name")
    parser.add_argument("--o", help = "Output file. Make sure to include the whole path if you want it in a different directory")
    input_file = args.i
    output_file = args.o
    if input_file is None:
        input_file = input("Enter input file: ")

    if output_file is None:
        output_file = input("Enter output file: ")

    # Read in point_picking list and modify dataframe by setting columns, changing ID column to dtype = string, and making rounding Easting, Northing, Altitude, and retro to 3 decimal points. 
    # The reason that I have to round is because, I believe, when it reads in values from the csv it converts it to int64 which makes it add these trailing decimal points. If I could make it just read in
    # the points without the trailing decimals, then this would be much faster
    picking_list = pd.read_csv(source_file, sep = ",", header = None)
    picking_list.columns = ["Easting", "Northing", "Altitude"]
    df = pd.read_csv('E:/School/VIP/Data/LiDAR_Data/original/XYZ/V_20180816_I285_EB_run1(0)_2nd_leg.txt', sep = " ")
    df = df.astype({'ID': str})
    # Figure out how to get rid of this code. Takes a lot of time.
    df['Easting'] = df['Easting'].apply(round_half_up)
    df['Northing'] = df['Northing'].apply(round_half_up)
    df['Altitude'] = df['Altitude'].apply(round_half_up)
    df['Retro'] = df['Retro'].apply(round_half_up)

    # Create output dataframe
    df2 = pd.DataFrame(columns = df.columns)

    # Actually finding the original points
    for index_main, row_main in picking_list.iterrows():
        for index, row in df.iterrows():
            if (math.isclose(row['Easting'], row_main['Easting'], abs_tol = 0.001) and math.isclose(row['Northing'], row_main['Northing'], abs_tol = 0.001) and math.isclose(row['Altitude'], row_main['Altitude'], abs_tol = 0.001)):
                print('true')
                df2 = df2.append(row)
                break

    # Write found points out to .txt file
    df2.to_csv('E:/School/VIP/Data/LiDAR_Data/output/CC/found_points.txt', sep = ' ', index = False)