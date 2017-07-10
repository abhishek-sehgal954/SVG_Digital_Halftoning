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
from color_halftone import gcr


dwg = svgwrite.Drawing('output.svg',profile='full',size=('70cm','70cm'),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')
#dwg.add(dwg.rect(insert=(0,0),size=("100%","100%"),fill='white'))
#blend = dwg.defs.add(dwg.filter(id="B4" ,filterUnits="objectBoundingBox", x="0%", y="0%", width="100%", height="100%"))
#blend.feBlend(in_='BackgroundImage',in2="SourceGraphic", mode='multiply')

def intensity_dot(image,color):
  arr = np.asarray(image)
  mini = 999
  maxi = 0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      maxi = max(arr[i][j],maxi)
      mini = min(arr[i][j],mini)
  level = float(float(maxi-mini)/float(10));
  brr = [[0]*len(arr[0]) for i in range(len(arr))]
  for i in range(10):                                              
    l1 = mini+level*i
    l2 = l1+level
    for j in range(len(arr)):
      for k in range(len(arr[0])):
        if(arr[j][k] >= l1 and arr[j][k] <= l2):
          brr[j][k] = i
  gray_level = [0]*10
  gray_level[0] = 2.5
  gray_level[1] = 2.2
  gray_level[2] = 2
  gray_level[3] = 1.8                                              
  gray_level[4] = 1.6                                             
  gray_level[5] =  1.4
  gray_level[6] = 1.2
  gray_level[7] = 1
  gray_level[8] = 0.8
  gray_level[9] = 0
  startu=0
  endu=0


  for i in range(len(brr)):
    for j in range(len(brr[i])):
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+5)/2)),gray_level[brr[i][j]],fill=color,filter='url(#B4)',style="mix-blend-mode: multiply;"))       
        startu = startu+5                                                                                 
    endu = endu+5
    startu = 0
  dwg.save() 
 

def main():
  fname = 'tree_small.jpg'
  image = Image.open(fname)
  cmyk = image.split()  
  intensity_dot(cmyk[0],'cyan')
  intensity_dot(cmyk[1],'magenta')
  intensity_dot(cmyk[2],'yellow')
  
 

if __name__=="__main__":
  main()