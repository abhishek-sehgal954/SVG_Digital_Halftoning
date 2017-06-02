import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname = 'test.jpg'
image = Image.open(fname)
image = Image.open(fname).convert('L')
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
for i in range(0,len(arr),3):
  for j in range(0,len(arr[i]),3):
    count=0
    for k in range(3):
      for l in range(3):
        if(i+k<len(arr) and j+l<len(arr[i])):
          if(arr[i+k][j+l]>=128):
            count=count+1
    for k in range(1,count+1,1):
    	if(i+dict3[k][0]<len(arr) and j+dict3[k][1] <len(arr[i])):
    		brr[i+dict3[k][0]][j+dict3[k][1]]=255
plt.imshow(brr,'gray')
plt.show()
brr=[[0]*len(arr[0]) for i in range(len(arr))]
for i in range(0,len(arr),5):
  for j in range(0,len(arr[i]),5):
    count=0
    for k in range(5):
      for l in range(5):
        if(i+k<len(arr) and j+l<len(arr[i])):
          if(arr[i+k][j+l]>=128):
            count=count+1
    for k in range(1,count+1,1):
    	if(i+dict5[k][0]<len(arr) and j+dict5[k][1] <len(arr[i])):
    		brr[i+dict5[k][0]][j+dict5[k][1]]=255
plt.imshow(brr,'gray')
plt.show()
brr=[[0]*len(arr[0]) for i in range(len(arr))]
for i in range(0,len(arr),7):
  for j in range(0,len(arr[i]),7):
    count=0
    for k in range(7):
      for l in range(7):
        if(i+k<len(arr) and j+l<len(arr[i])):
          if(arr[i+k][j+l]>=128):
            count=count+1
    for k in range(1,count+1,1):
    	if(i+dict7[k][0]<len(arr) and j+dict7[k][1] <len(arr[i])):
    		brr[i+dict7[k][0]][j+dict7[k][1]]=255
plt.imshow(brr,'gray')
plt.show()
