import numpy as np
import pandas as pd
from pyproj import Proj


"""
This class houses all the methods used to convert data.
"""


class Converter:



    # This method takes in gps data and returns the UTM counterpart
    def gps_2_utm(self, lat, long, alt):
