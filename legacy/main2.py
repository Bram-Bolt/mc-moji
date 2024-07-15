from PIL import Image

# Define the input and output coordinates as dictionaries
input_coords = [
    ("face_top", 10, 4, 16, 5),
    ("face_bottom", 10, 7, 16, 11),
    ("cheek_top", 8, 4, 9, 5),
    ("cheek_bottom", 8, 7, 9, 11),
    ("back_head_top", 7, 4, 7, 5),
    ("back_head_bottom", 7, 7, 7, 11),
    ("chest_top_left", 22, 16, 22, 17),
    ("chest_middle_left", 22, 19, 22, 20),
    ("chest_bottom_left", 22, 23, 22, 27),
    ("chest_top_center", 25, 16, 26, 17),
    ("chest_middle_center", 25, 19, 26, 20),
    ("chest_bottom_center", 25, 23, 26, 27),
    ("chest_top_right", 29, 16, 29, 17),
    ("chest_middle_right", 29, 19, 29, 20),
    ("chest_bottom_right", 29, 23, 29, 27),
    ("left_shoulder_top", 48, 16, 48, 16),
    ("left_shoulder_bottom", 47, 17, 48, 17),
    ("left_arm_top", 46, 19, 48, 20),
    ("left_arm_bottom", 46, 23, 48, 27),
    ("right_shoulder_top", 46, 32, 46, 32),
    ("right_shoulder_bottom", 46, 33, 47, 33),
    ("right_arm_top", 46, 35, 48, 36),
    ("right_arm_bottom", 46, 39, 48, 43),
]

output_coords = [
    ("face_top", 3, 0, 9, 1),
    ("face_bottom", 3, 2, 9, 6),
    ("cheek_top", 1, 0, 2, 1),
    ("cheek_bottom", 1, 2, 2, 6),
    ("back_head_top", 0, 0, 0, 1),
    ("back_head_bottom", 0, 2, 0, 6),
    ("chest_top_left", 3, 7, 3, 8),
    ("chest_middle_left", 3, 9, 3, 10),
    ("chest_bottom_left", 3, 11, 3, 15),
    ("chest_top_center", 4, 7, 5, 8),
    ("chest_middle_center", 4, 9, 5, 10),
    ("chest_bottom_center", 4, 11, 5, 15),
    ("chest_top_right", 6, 7, 6, 7),
    ("chest_middle_right", 6, 9, 6, 10),
    ("chest_bottom_right", 6, 11, 6, 15),
    ("left_shoulder_top", 2, 7, 2, 7),
    ("left_shoulder_bottom", 1, 8, 2, 8),
    ("left_arm_top", 0, 9, 2, 10),
    ("left_arm_bottom", 0, 11, 2, 15),
    ("right_shoulder_top", 7, 7, 7, 7),
    ("right_shoulder_bottom", 7, 8, 8, 8),
    ("right_arm_top", 7, 9, 9, 10),
    ("right_arm_bottom", 7, 11, 9, 15),
]

# Function to map the areas from input to output
def map_areas(input_image, output_image, input_coords, output_coords):
    for i in range(len(input_coords)):
        name, in_x1, in_y1, in_x2, in_y2 = input_coords[i]
        _, out_x1, out_y1, out_x2, out_y2 = output_coords[i]

        in_x2 += 1  # To include the end pixel
        in_y2 += 1  # To include the end pixel
        out_x2 += 1  # To include the end pixel
        out_y2 += 1  # To include the end pixel

        # Crop the input area
        cropped_area = input_image.crop((in_x1, in_y1, in_x2, in_y2))

        # Calculate the size of the output area
        output_width = out_x2 - out_x1
        output_height = out_y2 - out_y1

        # Resize the cropped area to fit the output area
        resized_area = cropped_area.resize((output_width, output_height), Image.ANTIALIAS)

        # Paste the resized area into the output image
        output_image.paste(resized_area, (out_x1, out_y1))

# Load the input image
input_image = Image.open("x.png")

# Create a new image with the same mode and size as the input image
output_image = Image.new(input_image.mode, input_image.size)

# Map the areas
map_areas(input_image, output_image, input_coords, output_coords)

# Save the output image
output_image.save("output.png")

print("Mapping complete. Output saved as 'output.png'.")
