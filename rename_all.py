# import required module
import os

# assign directory
directory = 'photos-print-spring24'
 
# iterate over files in
# that directory
i = 0
for filename in os.listdir(directory):

    input_file_path = os.path.join(directory, filename)
    os.rename(directory + "/" + filename, directory + "/" + 'IMG_' + str(i) + '.jpg')
    i += 1
