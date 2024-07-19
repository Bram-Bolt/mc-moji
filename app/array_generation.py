import numpy as np
import app.map_reading


def get_mapped_array(input_map: str, output_map: str, inp_array: str) -> np.ndarray:
    # read both files
    inp_data = app.map_reading.read_map(input_map)
    outp_data = app.map_reading.read_map(output_map)

    # form output
    outp_array = np.zeros((16, 11, 4), dtype=np.uint8)
    for i in range(1, len(inp_data)):
        try:
            start_x, start_y, end_x, end_y = app.map_reading.get_coords(i, outp_data)
            outp_array[start_y:end_y, start_x:end_x] = app.map_reading.get_array(
                i, inp_data, inp_array
            )
        except:
            print("mapping fault")
            print(inp_data[i])
    return outp_array
