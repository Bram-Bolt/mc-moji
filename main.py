from PIL import Image
import numpy as np
from array_generation import get_mapped_array



input_img = "examples/bram.png"
shadow_path = "shadows.png"
input_map_base = "mappings/updated/input_base.csv"
output_map_base = "mappings/updated/output_base.csv"
input_map_overlay = "mappings/updated/input_overlay.csv"
output_map_overlay = "mappings/updated/output_overlay.csv"


# make mappings
output_array_overlay = get_mapped_array(input_map_overlay, output_map_overlay, input_img)
output_array_base = get_mapped_array(input_map_base, output_map_base, input_img)


base_image = Image.fromarray(output_array_base, "RGBA")
overlay_image = Image.fromarray(output_array_overlay, "RGBA")
shadow_image = Image.open(shadow_path) 

base_image.paste(overlay_image, (0,0), mask = overlay_image) 
base_image.paste(shadow_image, (0,0), mask = shadow_image) 

base_image.save("output.png")
print("Done!")
