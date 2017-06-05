import os
import webbrowser
import svgwrite
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

#dwg.add(dwg.line((0, 0), (10000, 0), stroke=svgwrite.rgb(10, 100, 160, '%')))
#dwg.add(dwg.text('Test', insert=(0, 100), fill='red'))

#dwg.add(dwg.circle((50,50),10,stroke=svgwrite.rgb(10, 100, 160, '%')))
"""dwg = svgwrite.Drawing('test.svg', profile='tiny')
dwg.add(dwg.circle((200,100),2.5))
dwg.save() 
browser=webbrowser.get('firefox')
browser.open_new('file://' + os.path.realpath("test.svg"))
"""
#dwg.add(dwg.rect((100,0),(15,15)))

#accepted
#Try specifying the "file://" at the startu of the URL. Also, use the absolute path of the file:
#webbrowser.open("http://www.google.com")

#plt.imshow("test.svg")
def intensity_2(image):
  arr=np.asarray(image)
  mini=999
  maxi=0
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
  gray_level=[0]*10

  gray_level[0] = 2.5
  gray_level[1] = 2.2
  gray_level[2] = 2
  gray_level[3] = 1.8
  gray_level[4] = 1.6
  gray_level[5]=  1.4
  gray_level[6] = 1.2
  gray_level[7] = 1
  gray_level[8] = 0.8
  gray_level[9] = 0
  #crr=[[0]*(len(arr[0])*3) for i in (range(len(arr))*3)]
  startu=100
  endu=50
  """print len(brr),len(brr[0]) 
  dwg = svgwrite.Drawing('test.svg', profile='tiny')
  for i in range(10):
  	for j in range(10):
  			dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+5)/2)),(gray_level[brr[i][j]])))
    	startu=startu+5
    	print startu,endu
   	endu=endu+5
   	startu=100"""
  #dwg.save() 
  dwg = svgwrite.Drawing('test.svg', profile='tiny')
  for i in range(len(brr)):
  	for j in range(len(brr[i])):
  		dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+5)/2)),gray_level[brr[i][j]]))
  		startu=startu+5
  		print startu,endu
  	endu=endu+5
  	startu=100
  dwg.save() 
  browser=webbrowser.get('firefox')
  browser.open_new('file://' + os.path.realpath("test.svg"))



      


fname = 'test2.jpg'
image = Image.open(fname)
image = Image.open(fname).convert('L')
#intensity_1(image,3)
#intensity_1(image,5)
#intensity_1(image,7)
intensity_2(image)