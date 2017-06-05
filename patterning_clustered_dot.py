import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def intensity_1(image,block_size):
  arr=np.asarray(image)
  size3=[[8,3,4],[6,1,2],[7,5,9]]
  size5=[[16,21,23,19,10],[14,8,4,6,12],[22,3,1,2,24],[13,7,5,9,15],[11,18,25,20,17]]
  size7=[[34,30,46,26,49,29,32],[38,20,24,16,22,19,41],[45,13,9,2,6,12,43],[36,11,4,1,5,10,37],[42,14,7,3,8,15,44],[40,18,23,17,25,21,39],
       [33,28,48,27,47,31,35]]
  dict3={}
  dict5={}
  dict7={}
  for i in range(3):
	 for j in range(3):
		  dict3[size3[i][j]]=[i,j]
  for i in range(5):
	 for j in range(5):
	   	dict5[size5[i][j]]=[i,j]
  for i in range(7):
	 for j in range(7):
		  dict7[size7[i][j]]=[i,j]

  brr=[[0]*len(arr[0]) for i in range(len(arr))]
  for i in range(0,len(arr),block_size):
    for j in range(0,len(arr[i]),block_size):
      count=0
      for k in range(block_size):
        for l in range(block_size):
          if(i+k<len(arr) and j+l<len(arr[i])):
            if(arr[i+k][j+l]>=128):
              count=count+1
      for k in range(1,count+1,1):
        if(block_size==3):
    	   if(i+dict3[k][0]<len(arr) and j+dict3[k][1] <len(arr[i])):
    		   brr[i+dict3[k][0]][j+dict3[k][1]]=1
        elif(block_size==5):
          if(i+dict5[k][0]<len(arr) and j+dict5[k][1] <len(arr[i])):
            brr[i+dict5[k][0]][j+dict5[k][1]]=1
        elif(block_size==7):
          if(i+dict7[k][0]<len(arr) and j+dict7[k][1] <len(arr[i])):
            brr[i+dict7[k][0]][j+dict7[k][1]]=1
  plt.imshow(brr,'gray')
  plt.show()

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
  gray_level=[[[0,0,0],[0,0,0],[0,0,0]] for i in range(10)]

  gray_level[0] = [[0,0,0],[0,0,0],[0,0,0]];
  gray_level[1] = [[0,1,0],[0,0,0],[0,0,0]];
  gray_level[2] = [[0,1,0],[0,0,0],[0,0,1]];
  gray_level[3] = [[1,1,0],[0,0,0],[0,0,1]];
  gray_level[4] = [[1,1,0],[0,0,0],[1,0,1]];
  gray_level[5]= [[1,1,1],[0,0,0],[1,0,1]];
  gray_level[6] = [[1,1,1],[0,0,1],[1,0,1]];
  gray_level[7] = [[1,1,1],[0,0,1],[1,1,1]];
  gray_level[8] = [[1,1,1],[1,0,1],[1,1,1]];
  gray_level[9] = [[1,1,1],[1,1,1],[1,1,1]];
  crr=[[0]*(len(arr[0])*3) for i in (range(len(arr))*3)]
  for i in range(len(brr)):
    for j in range(len(brr[i])):
      new_i=i+2*(i-1)
      new_j=j+2*(j-1)
      for k in range(3):
        for l in range(3):
          crr[new_i+k][new_j+l]=gray_level[brr[i][j]][k][l]
  plt.imshow(crr,'gray')
  plt.show()


fname = 'test2.jpg'
image = Image.open(fname)
image = Image.open(fname).convert('L')
#intensity_1(image,3)
#intensity_1(image,5)
#intensity_1(image,7)
intensity_2(image)