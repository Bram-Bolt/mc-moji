import csv
import numpy as np


# reads out csv map
def read_map(filename: str) -> list[list]:
    with open(filename, "r") as csvfile:
        csv_reader = csv.reader(csvfile)
        data = list(csv_reader)
    return data


# get coords of the csv map
def get_coords(i: int, data: list[list]) -> tuple[int, int, int, int]:
    return int(data[i][1]), int(data[i][2]), int(data[i][3]) + 1, int(data[i][4]) + 1


# generate an array based on map
def get_array(i: int, data: list[list], arr: np.ndarray) -> np.ndarray:
    start_x, start_y, end_x, end_y = get_coords(i, data)
    return arr[start_y:end_y, start_x:end_x]


def get_mapped_array(
    input_map: str, output_map: str, inp_array: np.ndarray
) -> np.ndarray:
    inp_data = read_map(input_map)
    outp_data = read_map(output_map)
    outp_array = np.zeros((16, 11, 4), dtype=np.uint8)
    for i in range(1, len(inp_data)):
        try:
            start_x, start_y, end_x, end_y = get_coords(i, outp_data)
            outp_array[start_y:end_y, start_x:end_x] = get_array(i, inp_data, inp_array)
        except:
            print("Mapping fault")
            print(inp_data[i])
    return outp_array
