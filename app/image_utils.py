from PIL import Image
import requests
from io import BytesIO


# loads image, either from the web or local
def load_image(skin: str) -> Image:
    if skin.endswith(".png"):
        return Image.open(skin).convert("RGBA")
    url = f"https://mineskin.eu/skin/{skin}"
    response = requests.get(url)
    return Image.open(BytesIO(response.content))


# saves the image
def save_image(image: Image, filename: str) -> None:
    image.save(f"{filename}.png")
    print(f"Skin {filename} was generated successfully.")
