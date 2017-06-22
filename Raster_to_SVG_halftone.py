#This program takes a raster image and produces its vector halftone using patterning algorithm .
# It supports 4 patterns 
# 1. Clustered dot
# 2. Triangle
# 3. Hexagon
# 4. Dispersed dot
# output file produced is output.svg which can be opened with any SVG viewer (inkscape, imagemagick etc.)
import os
import sys
import svgwrite
import numpy as np
from PIL import Image

def intensity(arr):
  #  calcluates intensity of a pixel from 0 to 9
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
          brr[j][k]=i
  return brr

def clustered_dot(image):
  # based on the intensity maps pixel to the circle of different radiuses
  # intensity 0 begin the circle with maximum black area
  arr = np.asarray(image)
  brr = intensity(arr)
  gray_level = [0]*10
  gray_level[0] = 2.5
  gray_level[1] = 2.2
  gray_level[2] = 2
  gray_level[3] = 1.8                                              
  gray_level[4] = 1.6                                             
  gray_level[5] = 1.4
  gray_level[6] = 1.2
  gray_level[7] = 1
  gray_level[8] = 0.8
  gray_level[9] = 0
  startu = 0
  endu = 0
  dwg = svgwrite.Drawing('output.svg', profile = 'full')
  for i in range(len(brr)):
  	for j in range(len(brr[i])):
  		dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+5)/2)),gray_level[brr[i][j]]))        
  		startu = startu+5                                                                                  
  	endu = endu+5
  	startu = 0
  dwg.save() 

def triangle(image):
  # based on the intensity maps pixel to the triangle of different areas
  # intensity 0 begin the triangle with maximum black area
  arr = np.asarray(image)
  brr = intensity(arr)
  dwg = svgwrite.Drawing('output.svg', profile='full')
  startu = 0
  endu = 0
  for i in range(len(brr)):
    for j in range(len(brr[i])):
      temp_list = []
      if(brr[i][j] == 0):
        temp_list.append((int((startu+startu+5)/2),endu))
        temp_list.append((startu,endu+5))
        temp_list.append((startu+5,endu+5))
      elif(brr[i][j] == 1):
        temp_list.append((int((startu+startu+5)/2),endu+0.1))
        temp_list.append((startu+0.1,endu+5-0.1))                                     
        temp_list.append((startu+5-0.1,endu+5-0.1))                                   
      elif(brr[i][j] == 2):
        temp_list.append((int((startu+startu+5)/2),endu+0.2))
        temp_list.append((startu+0.2,endu+5-0.2))
        temp_list.append((startu+5-0.2,endu+5-0.2))
      elif(brr[i][j] == 3):
        temp_list.append((int((startu+startu+5)/2),endu+0.3))
        temp_list.append((startu+0.3,endu+5-0.3))
        temp_list.append((startu+5-0.3,endu+5-0.3))
      elif(brr[i][j] == 4):
        temp_list.append((int((startu+startu+5)/2),endu+0.4))
        temp_list.append((startu+0.4,endu+5-0.4))
        temp_list.append((startu+5-0.4,endu+5-0.4))
      elif(brr[i][j] == 5):
        temp_list.append((int((startu+startu+5)/2),endu+0.5))
        temp_list.append((startu+0.5,endu+5-0.5))
        temp_list.append((startu+5-0.5,endu+5-0.5))
      elif(brr[i][j] == 6):
        temp_list.append((int((startu+startu+5)/2),endu+0.6))
        temp_list.append((startu+0.6,endu+5-0.6))
        temp_list.append((startu+5-0.6,endu+5-0.6))
      elif(brr[i][j] == 7):
        temp_list.append((int((startu+startu+5)/2),endu+0.7))
        temp_list.append((startu+0.7,endu+5-0.7))
        temp_list.append((startu+5-0.7,endu+5-0.7))
      elif(brr[i][j] == 8):
        temp_list.append((int((startu+startu+5)/2),endu+0.8))
        temp_list.append((startu+0.8,endu+5-0.8))
        temp_list.append((startu+5-0.8,endu+5-0.8))
      
      if(len(temp_list) != 0):
        dwg.add(dwg.polygon(temp_list,fill='black'))
      startu = startu+5
    endu = endu+5
    startu = 0
  dwg.save()

def hexagon(image):        
  # based on the intensity maps pixel to the hexagon of different areas
  # intensity 0 begin the hexagon with maximum black area                  
  arr = np.asarray(image)
  brr = intensity(arr)
  dwg = svgwrite.Drawing('output.svg', profile='full')
  startu = 0
  endu = 0
  for i in range(len(brr)):
    for j in range(len(brr[i])):
      temp_list = []
      if(brr[i][j] == 0):
        temp_list.append((startu+2,endu))
        temp_list.append((startu+4,endu))
        temp_list.append((startu,endu+3))
        temp_list.append((startu+6,endu+3))
        temp_list.append((startu+2,endu+3))
        temp_list.append((startu+4,endu+3))
      elif(brr[i][j] == 1):
        temp_list.append((startu+2,endu+0.2))
        temp_list.append((startu+4,endu+0.2))
        temp_list.append((startu+0.2,endu+3))
        temp_list.append((startu+6-0.2,endu+3))                
        temp_list.append((startu+2,endu+3-0.2))                
        temp_list.append((startu+4,endu+3-0.2))
      elif(brr[i][j] == 2):
        temp_list.append((startu+2,endu+0.4))
        temp_list.append((startu+4,endu+0.4))
        temp_list.append((startu+0.4,endu+3))
        temp_list.append((startu+6-0.4,endu+3))
        temp_list.append((startu+2,endu+3-0.4))
        temp_list.append((startu+4,endu+3-0.4))
      elif(brr[i][j] == 3):
        temp_list.append((startu+2,endu+0.6))
        temp_list.append((startu+4,endu+0.6))
        temp_list.append((startu+0.6,endu+3))
        temp_list.append((startu+6-0.6,endu+3))
        temp_list.append((startu+2,endu+3-0.6))
        temp_list.append((startu+4,endu+3-0.6))
      elif(brr[i][j] == 4):
        temp_list.append((startu+2,endu+0.8))
        temp_list.append((startu+4,endu+0.8))
        temp_list.append((startu+0.8,endu+3))
        temp_list.append((startu+6-0.8,endu+3))
        temp_list.append((startu+2,endu+3-0.8))
        temp_list.append((startu+4,endu+3-0.8))
      elif(brr[i][j] == 5):
        temp_list.append((startu+2,endu+1))
        temp_list.append((startu+4,endu+1))
        temp_list.append((startu+1,endu+3))
        temp_list.append((startu+6-1,endu+3))
        temp_list.append((startu+2,endu+3-1))
        temp_list.append((startu+4,endu+3-1))
      elif(brr[i][j] == 6):
        temp_list.append((startu+2,endu+1.2))
        temp_list.append((startu+4,endu+1.2))
        temp_list.append((startu+1.2,endu+3))
        temp_list.append((startu+6-1.2,endu+3))
        temp_list.append((startu+2,endu+3-1.2))
        temp_list.append((startu+4,endu+3-1.2))
      elif(brr[i][j] == 7):
        temp_list.append((startu+2,endu+1.4))
        temp_list.append((startu+4,endu+1.4))
        temp_list.append((startu+1.4,endu+3))
        temp_list.append((startu+6-1.4,endu+3))
        temp_list.append((startu+2,endu+3-1.4))
        temp_list.append((startu+4,endu+3-1.4))     
      elif(brr[i][j] == 8):
        temp_list.append((startu+2,endu+1.6))
        temp_list.append((startu+4,endu+1.6))
        temp_list.append((startu+1.6,endu+3))
        temp_list.append((startu+6-1.6,endu+3))
        temp_list.append((startu+2,endu+3-1.6))
        temp_list.append((startu+4,endu+3-1.6))
      
      if(len(temp_list) != 0):
        dwg.add(dwg.polygon(temp_list,fill='black'))
      startu = startu+5
    endu = endu+5
    startu = 0
  dwg.save() 

def dispersed_dot(image):
  arr = np.asarray(image)
  brr = intensity(arr)
  dwg = svgwrite.Drawing('output.svg', profile='full')
  startu = 0
  endu = 0
  for i in range(len(brr)):
    for j in range(len(brr[i])):
      if(brr[i][j] == 0):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+3)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+3)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+3)/2)),1)) 
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+5)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 1):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+3)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+3)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+3)/2)),1)) 
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+5)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 2):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+3)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+3)/2)),1)) 
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+5)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 3):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+3)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+3)/2)),1)) 
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+5)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 4):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+3)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+3)/2)),1)) 
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 5):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+3)/2)),1)) 
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 6):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+3)/2)),1)) 
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 7):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
        dwg.add(dwg.circle((int((startu+startu+3)/2),int((endu+endu+5)/2)),1))
      elif(brr[i][j] == 8):
        dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1))
      startu = startu+3
    endu = endu+3;
    startu = 0;
  dwg.save() 

def main():
  fname = 'test.jpg'
  image = Image.open(fname).convert('L')
  if(sys.argv[1] == 'clustered_dot'):
    clustered_dot(image)
  elif(sys.argv[1] == 'triangle'):
    triangle(image)
  elif(sys.argv[1]=='hexagon'):
    hexagon(image)
  elif(sys.argv[1]=='dispersed_dot'):
    dispersed_dot(image)
if __name__=="__main__":
  main()