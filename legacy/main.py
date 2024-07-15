from PIL import Image
import numpy as np



# Load the image and convert to RGBA
inp = Image.open('x.png').convert("RGBA")


# # Convert image to numpy array
# inp_array = np.asarray(inp)
# print(inp_array.shape)  # Check the shape of the array

# # Define the slice coordinates
# start_x, end_x = 8, 16
# start_y, end_y = 8, 16

# # Slice the part of the array
# head_array = inp_array[start_x:end_x, start_y:end_y]

# # Create a new image from the sliced array
# sliced_image = Image.fromarray(sliced_array, 'RGBA')

# # Save or display the new image
# sliced_image.save('sliced_image.png')
# sliced_image.show()