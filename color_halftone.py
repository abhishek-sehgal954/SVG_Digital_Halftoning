# This program takes a raster color image and produces its raster color halftone using patterning algorithm .
# Split the image into C, M, Y, K.
# Rotate each separated image by 0, 15, 30, and 45 degrees respectively.
# Take the half-tone of each image (dot size will be proportional to the intensity).
# Rotate back each half-toned image.
# Now you have your colour separated images. The rotation step reduces 
# dot alignment issues (which would mess everything up), and things like Moire pattern
# effects will be reasonably minimized.


import numpy as np
from PIL import Image
from patterning_clustered_dot import intensity, patterning

def gcr(im, percentage):
    #  basic "Gray Component Replacement" function. Returns a CMYK image with 
    #  percentage gray component removed from the CMY halftones and put in the
    #  K halftone, ie. for percentage=100, (41, 100, 255, 0) >> (0, 59, 214, 41)
    cmyk_im = im.convert('CMYK')
    if not percentage:
        return cmyk_im
    cmyk_im = cmyk_im.split()
    cmyk = []
    for i in range(4):
        cmyk.append(cmyk_im[i].load())
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            gray = min(cmyk[0][x,y], cmyk[1][x,y], cmyk[2][x,y]) * percentage / 100
            for i in range(3):
                cmyk[i][x,y] = cmyk[i][x,y] - gray
            cmyk[3][x,y] = gray
    return Image.merge('CMYK', cmyk_im)

def color_halftoning_with_rotation(cmyk,increment_in_angle):
  dots=[]    
  angle=0
  for i in range(4):
    channel = Image.fromarray(patterning(cmyk[i].rotate(angle,expand=1))).convert('L')
    channel = channel.rotate(-angle,expand=1)
    width_half, height_half = channel.size
    xx = (width_half-cmyk[i].size[0]*3) / 2
    yy = (height_half-cmyk[i].size[1]*3) / 2
    channel = channel.crop((xx, yy, xx + cmyk[i].size[0]*3, yy + cmyk[i].size[1]*3))
    dots.append(channel)
    angle += increment_in_angle
  return dots

def main():
  fname = 'tree.jpg'
  image = Image.open(fname)
  image = gcr(image,100)
  cmyk = image.split()   
  dots = color_halftoning_with_rotation(cmyk,15)
  new_cmyk = Image.merge('CMYK',dots)
  new_cmyk.save("output.jpg")
  new_cmyk.show()
if __name__=="__main__":
  main()
    