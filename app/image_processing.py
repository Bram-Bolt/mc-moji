from PIL import Image


# adds overlay
def apply_overlay(base_image: Image, overlay_image: Image) -> Image:
    # base_image.paste(overlay_image, (0, 0), mask=overlay_image)
    # return base_image
    combined_image = Image.alpha_composite(base_image, overlay_image)
    return combined_image


# adds shadows
def apply_shadows(base_image: Image, shadow_image: Image) -> Image:
    # base_image.paste(shadow_image, (0, 0), mask=shadow_image)
    combined_image = Image.alpha_composite(base_image, shadow_image)
    return combined_image
