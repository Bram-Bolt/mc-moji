# processing.py
import os
import numpy as np
from PIL import Image
from app.image_utils import load_image, save_image
from app.map_utils import get_mapped_array
from app.image_processing import apply_overlay, apply_shadows


def generate_avatar(
    skin_path: str, enable_shadows: bool, enable_overlay: bool, size: int
) -> Image:
    # get mappings
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mapping_type = "beta"
    mapping_path = os.path.join(base_dir, "resources", "mappings", mapping_type)
    inp_map_base = os.path.join(mapping_path, "input_base.csv")
    outp_map_base = os.path.join(mapping_path, "output_base.csv")
    inp_map_overlay = os.path.join(mapping_path, "input_overlay.csv")
    outp_map_overlay = os.path.join(mapping_path, "output_overlay.csv")
    shadow_path = os.path.join(base_dir, "resources", "shadows.png")

    img = load_image(skin_path)
    inp_array = np.asarray(img)

    output_array_base = get_mapped_array(inp_map_base, outp_map_base, inp_array)
    base_image = Image.fromarray(output_array_base, "RGBA")

    if enable_overlay:
        output_array_overlay = get_mapped_array(
            inp_map_overlay, outp_map_overlay, inp_array
        )
        overlay_image = Image.fromarray(output_array_overlay, "RGBA")
        base_image = apply_overlay(base_image, overlay_image)

    if enable_shadows:
        shadow_image = Image.open(shadow_path)
        base_image = apply_shadows(base_image, shadow_image)

    return base_image
