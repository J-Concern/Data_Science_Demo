import numpy as np
import csv
from path import PATH

with open(PATH) as file_obj:
    reader_obj = csv.reader(file_obj)
