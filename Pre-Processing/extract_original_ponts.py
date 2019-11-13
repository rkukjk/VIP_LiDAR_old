import math
import pandas as pd

if __name__ == "__main__":
    picking_list = pd.read_csv('picking_list.txt', sep = " ", header = None)
    picking_list.columns = ["cc_index", "easting", "northing", "altitude"]