from PIL import Image
import numpy as np

import app.array_generation
import requests
from io import BytesIO


# SET UP
def make_image(
    skin: str,
    label: str,
    overlay: bool,
    shadows: bool,
    size: int,  # yet to be supported
    mapping_type: str = "beta",
):
    # config of mappings
    mapping_type = "beta"
    mapping_path = f"app/resources/mappings/{mapping_type}"
    inp_map_base = f"{mapping_path}/input_base.csv"
    outp_map_base = f"{mapping_path}/output_base.csv"
    inp_map_overlay = f"{mapping_path}/input_overlay.csv"
    outp_map_overlay = f"{mapping_path}/output_overlay.csv"
    shadow_path = "resources/shadows.png"

    # load image
    if skin.endswith(".png"):
        img = Image.open(skin).convert("RGBA")
    else:
        url = f"https://mineskin.eu/skin/{skin}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))

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
