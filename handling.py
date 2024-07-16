import csv
import numpy as np
from icecream import ic


# read both files
def read_map(filename: str) -> list[list]:
    with open(filename, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)
    return data


# read coords
def get_coords(i: int, data: list[list]) -> tuple[int, int, int, int]:
    return int(data[i][1]), int(data[i][2]), int(data[i][3]) + 1, int(data[i][4]) + 1


# h
def get_array(i: int, data: list[list], arr: np.ndarray[list]) -> np.ndarray:
    start_x, start_y, end_x, end_y = get_coords(i, data)
    return arr[start_y:end_y, start_x:end_x]
