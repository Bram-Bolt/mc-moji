import argparse
from app.avatar_generator import generate_avatar
from app.image_utils import save_image


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
    # generate avatars based on arguments
    args = parse_arguments()
    for idx, skin in enumerate(args.skin):
        processed_image = generate_avatar(skin, args.shadows, args.overlay, args.size)
        save_image(processed_image, label=str(idx + 1), size=args.size)


if __name__ == "__main__":
    main()
