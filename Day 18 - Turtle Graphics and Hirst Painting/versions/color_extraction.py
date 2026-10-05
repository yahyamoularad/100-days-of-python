# Day 18: Extracting RGB Colours with colorgram
#
# This is the original colour-extraction code, uncommented.
#
# It requires:
# - the colorgram package
# - the original image.jpg used by the lesson
#
# The uploaded files did not include image.jpg, so update the path
# only after placing the original image on your computer.
#
# The original code below is preserved.

import colorgram

rgb_colors = []
colors = colorgram.extract('/home/yahya/Desktop/100 days of python/Day18/hirst-painting/image.jpg', 30)

for color in colors: 
    r = color.rgb.r 
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)
