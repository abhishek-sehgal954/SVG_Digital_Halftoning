# This program takes a raster color image and produces its vector color halftone using patterning algorithm.
# Split the image into C, M, Y, K.
# Take the half-tone of each image (dot size will be proportional to the intensity).
# and write it on a SVG File
# output file produced is output.svg which can be opened with any SVG viewer (inkscape, imagemagick etc.)


import os
import webbrowser
import sys
import svgwrite
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from ordered_dither import order_dither



dwg = svgwrite.Drawing('output.svg',profile='full',size=('30cm','30cm'),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')

def draw_svg(output,color):
  startu = 0
  endu = 0
  for i in range(len(output)):
    for j in range(len(output[i])):
      if (output[i][j]==0):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1,fill=color,style="mix-blend-mode: multiply;"))        
      startu = startu+2                                                                               
    endu = endu+2
    startu = 0
  dwg.save() 

def main():
  fname = 'tree_small.jpg'
  image = Image.open(fname)
  cmyk = image.split()  
  output_cyan = order_dither(cmyk[0])
  output_magenta = order_dither(cmyk[1])
  output_yellow = order_dither(cmyk[2])
  draw_svg(output_cyan,'cyan')
  draw_svg(output_magenta,'magenta')
  draw_svg(output_yellow,'yellow')

if __name__=="__main__":
  main()