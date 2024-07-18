from PIL import Image
import numpy as np
import handling

def get_mapped_array(input_map: str, output_map: str, input_img: str) -> np.ndarray:
    # read both files
    inp_data = handling.read_map(input_map)
    outp_data = handling.read_map(output_map)

    # load input
    inp = Image.open(input_img).convert("RGBA")
    inp_array = np.asarray(inp)

    # form output
    outp_array = np.zeros((16, 10, 4), dtype=np.uint8)
    for i in range(1, len(inp_data)):
        try:
            start_x, start_y, end_x, end_y = handling.get_coords(i, outp_data)
            outp_array[start_y:end_y, start_x:end_x] = handling.get_array(i, inp_data, inp_array)
        except:
            print("mapping fault")
            print(inp_data[i])
    return outp_array