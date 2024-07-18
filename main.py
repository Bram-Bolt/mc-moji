from PIL import Image
import numpy as np
from array_generation import get_mapped_array
from array_generation import merge_layers


input_img = "examples/bram.png"
input_map_base = "mappings/updated/input_base.csv"
output_map_base = "mappings/updated/output_base.csv"
input_map_overlay = "mappings/updated/input_overlay.csv"
output_map_overlay = "mappings/updated/output_overlay.csv"


# make mappings
output_array_overlay = get_mapped_array(input_map_overlay, output_map_overlay, input_img)
output_array_base = get_mapped_array(input_map_base, output_map_base, input_img)

# merge mappings
output_array = merge_layers(output_array_base, output_array_overlay)

sliced_image = Image.fromarray(output_array, "RGBA")
sliced_image.save("output.png")
print("Done!")
