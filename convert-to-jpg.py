import imageio.v3 as iio
from PIL import Image
# import required module
import os

# assign directory
directory = 'photos-print-spring24'
 
# iterate over files in
# that directory
for filename in os.listdir(directory):

    input_file_path = os.path.join(directory, filename)


    # Read the HEIC file using imageio
    img = iio.imread(input_file_path)

    # Convert to a PIL image
    pil_img = Image.fromarray(img)

    # Save as JPEG
    output_file_path = filename[:-5] + '.jpg'
    pil_img.save(output_file_path, 'JPEG')

    print(f"Image successfully converted to {output_file_path}")
