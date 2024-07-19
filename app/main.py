import argparse
import app.image_generation

parser = argparse.ArgumentParser(
    prog="mc-moji",
    description="Create quick skin art based minecraft skins.",
    epilog="For any questions, reach out to bram@gelebeer.nl.",
)

parser.add_argument(
    "skin",
    type=str,
    nargs="+",
    help="Put in either minecraft name or file path to .png skin file.",
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

args = parser.parse_args()

for idx, skin in enumerate(args.skin):
    app.image_generation.make_image(
        skin=skin,
        label=idx + 1,
        overlay=args.overlay,
        shadows=args.shadows,
        size=args.size,
    )


def main():
    print("All skins arts generations are finished.")
