import argparse
import os
import numpy as np
from PIL import Image
from app.image_utils import load_image, save_image
from app.map_utils import get_mapped_array
from app.image_processing import apply_overlay, apply_shadows


# parses CLI arguments
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="mc-moji",
        description="Create quick skin art based Minecraft skins.",
        epilog="For any questions, reach out to bram@gelebeer.nl.",
    )

    parser.add_argument(
        "skin",
        type=str,
        nargs="+",
        help="Put in either Minecraft name or file path to .png skin file.",
    )

    parser.add_argument(
        "-s",
        "--shadows",
        dest="shadows",
        action="store_true",
        help="Enable Shadows",
        default=False,
    )

    parser.add_argument(
        "-o",
        "--overlay",
        dest="overlay",
        action="store_true",
        help="Enable Overlay",
        default=False,
    )

    parser.add_argument(
        "-z",
        "--size",
        dest="size",
        type=int,
        help="Specify the size of the generated image. Size will be 11n x 16n.",
        default=1,
    )

    return parser.parse_args()


def main() -> None:
    # parse arguments
    args = parse_arguments()

    # get mappings
    base_dir = os.path.dirname(os.path.abspath(__file__))
    mapping_type = "beta"
    mapping_path = os.path.join(base_dir, "resources", "mappings", mapping_type)
    inp_map_base = os.path.join(mapping_path, "input_base.csv")
    outp_map_base = os.path.join(mapping_path, "output_base.csv")
    inp_map_overlay = os.path.join(mapping_path, "input_overlay.csv")
    outp_map_overlay = os.path.join(mapping_path, "output_overlay.csv")
    shadow_path = os.path.join(base_dir, "resources", "shadows.png")

    # apply mappings to all skins
    for idx, skin in enumerate(args.skin):
        img = load_image(skin)
        inp_array = np.asarray(img)

        output_array_base = get_mapped_array(inp_map_base, outp_map_base, inp_array)
        base_image = Image.fromarray(output_array_base, "RGBA")

        if args.overlay:
            output_array_overlay = get_mapped_array(
                inp_map_overlay, outp_map_overlay, inp_array
            )
            overlay_image = Image.fromarray(output_array_overlay, "RGBA")
            base_image = apply_overlay(base_image, overlay_image)

        if args.shadows:
            shadow_image = Image.open(shadow_path)
            base_image = apply_shadows(base_image, shadow_image)

        save_image(base_image, label=str(idx + 1), size=args.size)


if __name__ == "__main__":
    main()
