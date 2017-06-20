import os
import webbrowser
import sys
import svgwrite
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
dwg = svgwrite.Drawing('test.svg',profile='full',size=('70cm','70cm'),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')
blend = dwg.defs.add(dwg.filter(id="B4" ,filterUnits="objectBoundingBox", x="0%", y="0%", width="100%", height="100%"))
blend.feBlend(in_='SourceGraphic', mode='screen')
def gcr(im, percentage):
    '''basic "Gray Component Replacement" function. Returns a CMYK image with 
       percentage gray component removed from the CMY halftones and put in the
       K halftone, ie. for percentage=100, (41, 100, 255, 0) >> (0, 59, 214, 41)'''
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

def intensity_dot(image,color):
  arr=np.asarray(image)
  mini=999
  maxi=0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      maxi=max(arr[i][j],maxi)
      mini=min(arr[i][j],mini)
  level=float(float(maxi-mini)/float(10));
  brr=[[0]*len(arr[0]) for i in range(len(arr))]
  for i in range(10):                                              #computing pixel intensity of each individual pixel on a scale of 0 to 9
    l1=mini+level*i
    l2=l1+level
    for j in range(len(arr)):
      for k in range(len(arr[0])):
        if(arr[j][k]>=l1 and arr[j][k]<=l2):
          brr[j][k]=i
  gray_level=[0]*10
  #print len(arr), len(arr[0]),len(brr),len(brr[0])
  
  gray_level[0] = 2.5
  gray_level[1] = 2.2
  gray_level[2] = 2
  gray_level[3] = 1.8                                              #mapping the intensity level to radius of circle
  gray_level[4] = 1.6                                             
  gray_level[5]=  1.4
  gray_level[6] = 1.2
  gray_level[7] = 1
  gray_level[8] = 0.8
  gray_level[9] = 0
  #crr=[[0]*(len(arr[0])*3) for i in (range(len(arr))*3)]
  startu=0
  endu=0

#viewBox=('0 0 3000 3000')
  #dwg = svgwrite.Drawing('test.svg', profile='full',size=('70cm', '70cm'))
  for i in range(len(brr)):
    for j in range(len(brr[i])):
        dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+5)/2)),gray_level[brr[i][j]],fill=color,opacity='0.5',filter='url(#B4)'))       #draw .svg file using circle of different 
        startu=startu+5                                                                                  #radius calculated using intensity levels.
        #print startu,endu
    endu=endu+5
    startu=0
  dwg.save() 
 

fname = 'tree_small.jpg'
image = Image.open(fname)
#image=gcr(image,100)
cmyk= image.split()  
intensity_dot(cmyk[0],'cyan')
intensity_dot(cmyk[1],'magenta')
intensity_dot(cmyk[2],'yellow')
#intensity_dot(cmyk[3],'black')


#browser=webbrowser.get('firefox')
#browser.open_new('file://' + os.path.realpath("test.svg"))
