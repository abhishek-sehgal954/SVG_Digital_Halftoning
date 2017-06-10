import os
import webbrowser
import sys
import svgwrite
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def intensity_dot(image):
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
  dwg = svgwrite.Drawing('test.svg', profile='full',size=('70cm', '70cm'))
  for i in range(len(brr)):
  	for j in range(len(brr[i])):
  		dwg.add(dwg.circle((int((startu+startu+5)/2),int((endu+endu+5)/2)),gray_level[brr[i][j]]))       #draw .svg file using circle of different 
  		startu=startu+5                                                                                  #radius calculated using intensity levels.
  		#print startu,endu
  	endu=endu+5
  	startu=0
  dwg.save() 
  browser=webbrowser.get('firefox')
  browser.open_new('file://' + os.path.realpath("test.svg"))


  #print gray_level[brr[0][0]]
def intensity_triangle(image):
  arr=np.asarray(image)
  mini=999
  maxi=0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      maxi=max(arr[i][j],maxi)
      mini=min(arr[i][j],mini)
  level=float(float(maxi-mini)/float(10));
  brr=[[0]*len(arr[0]) for i in range(len(arr))]                #computing pixel intensity of each individual pixel on a scale of 0 to 9
  for i in range(10):
    l1=mini+level*i
    l2=l1+level
    for j in range(len(arr)):
      for k in range(len(arr[0])):
        if(arr[j][k]>=l1 and arr[j][k]<=l2):
          brr[j][k]=i
  dwg = svgwrite.Drawing('test.svg', profile='full',size=('70cm', '70cm'))
  startu=0
  endu=0
  for i in range(len(brr)):
    for j in range(len(brr[i])):
      temp_list=[]
      if(brr[i][j]==0):
       
        temp_list.append((int((startu+startu+5)/2),endu))
        temp_list.append((startu,endu+5))
        temp_list.append((startu+5,endu+5))
      elif(brr[i][j]==1):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.1))
        temp_list.append((startu+0.1,endu+5-0.1))                                     #draw .svg file using triangle of different size
        temp_list.append((startu+5-0.1,endu+5-0.1))                                   #calculated using intensity levels.
      elif(brr[i][j]==2):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.2))
        temp_list.append((startu+0.2,endu+5-0.2))
        temp_list.append((startu+5-0.2,endu+5-0.2))
      elif(brr[i][j]==3):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.3))
        temp_list.append((startu+0.3,endu+5-0.3))
        temp_list.append((startu+5-0.3,endu+5-0.3))
      elif(brr[i][j]==4):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.4))
        temp_list.append((startu+0.4,endu+5-0.4))
        temp_list.append((startu+5-0.4,endu+5-0.4))
      elif(brr[i][j]==5):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.5))
        temp_list.append((startu+0.5,endu+5-0.5))
        temp_list.append((startu+5-0.5,endu+5-0.5))
      elif(brr[i][j]==6):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.6))
        temp_list.append((startu+0.6,endu+5-0.6))
        temp_list.append((startu+5-0.6,endu+5-0.6))
      elif(brr[i][j]==7):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.7))
        temp_list.append((startu+0.7,endu+5-0.7))
        temp_list.append((startu+5-0.7,endu+5-0.7))
      elif(brr[i][j]==8):
        #temp_list=[]
        temp_list.append((int((startu+startu+5)/2),endu+0.8))
        temp_list.append((startu+0.8,endu+5-0.8))
        temp_list.append((startu+5-0.8,endu+5-0.8))
      
        

      
      #print temp_list
      if(len(temp_list)!=0):
        dwg.add(dwg.polygon(temp_list,fill='black'))
      startu=startu+5
      #print startu,endu
    endu=endu+5
    startu=0
  dwg.save() 
  browser=webbrowser.get('firefox')
  browser.open_new('file://' + os.path.realpath("test.svg"))

def intensity_hexagon(image):                          
  arr=np.asarray(image)
  mini=999
  maxi=0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      maxi=max(arr[i][j],maxi)
      mini=min(arr[i][j],mini)
  level=float(float(maxi-mini)/float(10));
  brr=[[0]*len(arr[0]) for i in range(len(arr))]                         #computing pixel intensity of each individual pixel on a scale of 0 to 9
  for i in range(10):
    l1=mini+level*i
    l2=l1+level
    for j in range(len(arr)):
      for k in range(len(arr[0])):
        if(arr[j][k]>=l1 and arr[j][k]<=l2):
          brr[j][k]=i
  dwg = svgwrite.Drawing('test.svg', profile='full',size=('70cm', '70cm'))
  startu=0
  endu=0
  for i in range(len(brr)):
    for j in range(len(brr[i])):
      temp_list=[]
      if(brr[i][j]==0):
       
        temp_list.append((startu+2,endu))
        temp_list.append((startu+4,endu))
        temp_list.append((startu,endu+3))
        temp_list.append((startu+6,endu+3))
        temp_list.append((startu+2,endu+3))
        temp_list.append((startu+4,endu+3))
      elif(brr[i][j]==1):
        #temp_list=[]
        temp_list.append((startu+2,endu+0.2))
        temp_list.append((startu+4,endu+0.2))
        temp_list.append((startu+0.2,endu+3))
        temp_list.append((startu+6-0.2,endu+3))                #draw .svg file using hexagon of different size
        temp_list.append((startu+2,endu+3-0.2))                #calculated using intensity levels.
        temp_list.append((startu+4,endu+3-0.2))
      elif(brr[i][j]==2):
        #temp_list=[]
        temp_list.append((startu+2,endu+0.4))
        temp_list.append((startu+4,endu+0.4))
        temp_list.append((startu+0.4,endu+3))
        temp_list.append((startu+6-0.4,endu+3))
        temp_list.append((startu+2,endu+3-0.4))
        temp_list.append((startu+4,endu+3-0.4))
      elif(brr[i][j]==3):
        #temp_list=[]
        temp_list.append((startu+2,endu+0.6))
        temp_list.append((startu+4,endu+0.6))
        temp_list.append((startu+0.6,endu+3))
        temp_list.append((startu+6-0.6,endu+3))
        temp_list.append((startu+2,endu+3-0.6))
        temp_list.append((startu+4,endu+3-0.6))
      elif(brr[i][j]==4):
        #temp_list=[]
        temp_list.append((startu+2,endu+0.8))
        temp_list.append((startu+4,endu+0.8))
        temp_list.append((startu+0.8,endu+3))
        temp_list.append((startu+6-0.8,endu+3))
        temp_list.append((startu+2,endu+3-0.8))
        temp_list.append((startu+4,endu+3-0.8))
      elif(brr[i][j]==5):
        #temp_list=[]
        temp_list.append((startu+2,endu+1))
        temp_list.append((startu+4,endu+1))
        temp_list.append((startu+1,endu+3))
        temp_list.append((startu+6-1,endu+3))
        temp_list.append((startu+2,endu+3-1))
        temp_list.append((startu+4,endu+3-1))
      elif(brr[i][j]==6):
        #temp_list=[]
        temp_list.append((startu+2,endu+1.2))
        temp_list.append((startu+4,endu+1.2))
        temp_list.append((startu+1.2,endu+3))
        temp_list.append((startu+6-1.2,endu+3))
        temp_list.append((startu+2,endu+3-1.2))
        temp_list.append((startu+4,endu+3-1.2))

      elif(brr[i][j]==7):
        #temp_list=[]
        temp_list.append((startu+2,endu+1.4))
        temp_list.append((startu+4,endu+1.4))
        temp_list.append((startu+1.4,endu+3))
        temp_list.append((startu+6-1.4,endu+3))
        temp_list.append((startu+2,endu+3-1.4))
        temp_list.append((startu+4,endu+3-1.4))     

      elif(brr[i][j]==8):
        #temp_list=[]
        temp_list.append((startu+2,endu+1.6))
        temp_list.append((startu+4,endu+1.6))
        temp_list.append((startu+1.6,endu+3))
        temp_list.append((startu+6-1.6,endu+3))
        temp_list.append((startu+2,endu+3-1.6))
        temp_list.append((startu+4,endu+3-1.6))
      
        

      
      #print temp_list
      if(len(temp_list)!=0):
        dwg.add(dwg.polygon(temp_list,fill='black'))
      startu=startu+5
      #print startu,endu
    endu=endu+5
    startu=0
  dwg.save() 
  browser=webbrowser.get('firefox')
  browser.open_new('file://' + os.path.realpath("test.svg")) 


def main():
  fname = 'test.jpg'
  image = Image.open(fname)
  image = Image.open(fname).convert('L')
  if(sys.argv[1] == 'dot'):
    intensity_dot(image)
  elif(sys.argv[1] == 'triangle'):
    intensity_triangle(image)
  elif(sys.argv[1]=='hexagon'):
    intensity_hexagon(image)
if __name__=="__main__":
  main()