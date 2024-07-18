from PIL import Image
import numpy as np
from array_generator import get_mapped_array


input_img = "examples/preview.png"
input_map_base = "mappings/updated/input_base.csv"
output_map_base = "mappings/updated/output_base.csv"
input_map_overlay = "mappings/updated/input_overlay.csv"
# output_map_overlay = "mappings/updated/output_overlay.csv"



output_array = get_mapped_array(input_map_overlay, output_map_base, input_img)
# save output
sliced_image = Image.fromarray(output_array, "RGBA")
sliced_image.save("output.png")
print("Done!")
