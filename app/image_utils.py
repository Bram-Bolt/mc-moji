from PIL import Image
import requests
from io import BytesIO
from pathlib import Path


# loads image, either from the web or local
def load_image(skin: str) -> Image:
    if skin.endswith(".png"):
        return Image.open(skin).convert("RGBA")
    url = f"https://mineskin.eu/skin/{skin}"
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


# saves the image
def save_image(image: Image, filename: str, location: str) -> None:
    save_location = Path(location, f"{filename}.png")
    image.save(save_location)
    print(f"Skin {filename} was generated successfully.")
