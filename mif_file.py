# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:30:13 2025

@author: Rosshun
"""

from matplotlib import image as mpimg

# Function to create a MIF file from image data
def write_mif(data, filename):
    height, width, _ = data.shape
    with open(filename, 'w') as mif:
        mif.write('WIDTH=8;\n')
        mif.write('DEPTH={};\n'.format(height * width))
        mif.write('ADDRESS_RADIX=HEX;\n')
        mif.write('DATA_RADIX=HEX;\n')
        mif.write('CONTENT BEGIN\n')
        
        address = 0
        for row in data:
            for pixel in row:
                # Convert RGB values to a single integer (assuming 8 bits per channel)
                value = (pixel[0] << 16) + (pixel[1] << 8) + pixel[2]
                mif.write('{:04X} : {:06X};\n'.format(address, value))
                address += 1
        
        mif.write('END;\n')

# Load image as pixel array
img_path = input('Enter the image file path: ')
data = mpimg.imread(img_path)

# Ensure the image is in RGB format
if data.shape[-1] == 4:  # RGBA to RGB
    data = data[..., :3]

# Save the data for the MIF
write_mif(data, 'output.mif')

print("MIF file created successfully!")