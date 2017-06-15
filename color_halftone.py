import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
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
def color_halftoning(image):
  arr = np.array(image)
  mini=999
  maxi=0
  #print len(arr),len(arr[0])
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      maxi=max(arr[i][j],maxi)
      mini=min(arr[i][j],mini)
  level=float(float(maxi-mini)/float(10));

  brr=[[0]*len(arr[0]) for i in range(len(arr))]
  for i in range(10):
    l1=mini+level*i
    l2=l1+level
    for j in range(len(arr)):
      for k in range(len(arr[0])):
        if(arr[j][k]>=l1 and arr[j][k]<=l2):
          brr[j][k]=i
  gray_level=[[[0,0,0],[0,0,0],[0,0,0]] for i in range(10)]

  gray_level[0] = [[0,0,0],[0,0,0],[0,0,0]];
  gray_level[1] = [[0,255,0],[0,0,0],[0,0,0]];
  gray_level[2] = [[0,255,0],[0,0,0],[0,0,255]];
  gray_level[3] = [[255,255,0],[0,0,0],[0,0,255]];
  gray_level[4] = [[255,255,0],[0,0,0],[255,0,255]];
  gray_level[5]= [[255,255,255],[0,0,0],[255,0,255]];
  gray_level[6] = [[255,255,255],[0,0,255],[255,0,255]];
  gray_level[7] = [[255,255,255],[0,0,255],[255,255,255]];
  gray_level[8] = [[255,255,255],[255,0,255],[255,255,255]];
  gray_level[9] = [[255,255,255],[255,255,255],[255,255,255]];
  crr= np.zeros((len(arr)*3, len(arr[0])*3, 3), dtype=np.uint8)
  #crr=[[0]*(len(arr[0])*3) for i in (range(len(arr))*3)]
  for i in range(len(brr)):
    for j in range(len(brr[i])):
      new_i=i+2*(i-1)
      new_j=j+2*(j-1)
      for k in range(3):
        for l in range(3):
          crr[new_i+k][new_j+l]=gray_level[brr[i][j]][k][l]
  img = Image.fromarray(crr)
  return img

def halftoning_with_rotation(cmyk,increment_in_angle):
  dots=[]    
  angle=0
  for i in range(4):
    channel = color_halftoning(cmyk[i].rotate(angle,expand=1)).convert('L')
    channel=channel.rotate(-angle,expand=1)
    width_half, height_half = channel.size
    xx=(width_half-cmyk[i].size[0]*3) / 2
    yy=(height_half-cmyk[i].size[1]*3) / 2
    channel = channel.crop((xx, yy, xx + cmyk[i].size[0]*3, yy + cmyk[i].size[1]*3))
    dots.append(channel)
    angle += increment_in_angle
  return dots

fname = 'tree.jpg'
image = Image.open(fname)
image=gcr(image,100)
cmyk= image.split()   
dots=halftoning_with_rotation(cmyk,15)
new_cmyk = Image.merge('CMYK',dots)
new_cmyk.save("output.jpg")
new_cmyk.show()
    