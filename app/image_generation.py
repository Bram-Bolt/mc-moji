from PIL import Image
import numpy as np
import os
import app.array_generation
import requests
from io import BytesIO


# image loader
def load_image(skin) -> Image:
    if skin.endswith(".png"):
        return Image.open(skin).convert("RGBA")
    url = f"https://mineskin.eu/skin/{skin}"
    response = requests.get(url)
    return Image.open(BytesIO(response.content))
  
# SET UP
def make_image(
    skin: str,
    label: str,
    overlay: bool,
    shadows: bool,
    size: int,  # yet to be supported
    mapping_type: str = "beta",
):
    # set base directory
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Config of mappings
    mapping_type = "beta"
    mapping_path = os.path.join(base_dir, "resources", "mappings", mapping_type)
    inp_map_base = os.path.join(mapping_path, "input_base.csv")
    outp_map_base = os.path.join(mapping_path, "output_base.csv")
    inp_map_overlay = os.path.join(mapping_path, "input_overlay.csv")
    outp_map_overlay = os.path.join(mapping_path, "output_overlay.csv")
    shadow_path = os.path.join(base_dir, "resources", "shadows.png")

    img = load_image(skin)
    # generate array
    inp_array = np.asarray(img)

    # make mappings
    output_array_overlay = app.array_generation.get_mapped_array(
        inp_map_overlay, outp_map_overlay, inp_array
    )
    output_array_base = app.array_generation.get_mapped_array(
        inp_map_base, outp_map_base, inp_array
    )
    base_image = Image.fromarray(output_array_base, "RGBA")

    # options
    if overlay:
        overlay_image = Image.fromarray(output_array_overlay, "RGBA")
        base_image.paste(overlay_image, (0, 0), mask=overlay_image)
    if shadows:
        shadow_image = Image.open(shadow_path)
        base_image.paste(shadow_image, (0, 0), mask=shadow_image)

    # resize
    final_image = base_image.resize((11 * size, 16 * size), Image.NEAREST)
    final_image.save(f"output_{label}.png")
    print(f"Skin {label} was generated sucesfully.")
