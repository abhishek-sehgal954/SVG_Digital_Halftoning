import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname = 'test.jpg'
image = Image.open(fname)
image = Image.open(fname).convert('L')
arr=np.asarray(image)
brr=[[] for i in range(len(arr))]
threshold=[[5, 118, 160, 58, 17],[48,201,232,170,99],[129,211,252,242,150],[89,191,221,181,68],[38,78,140,108,27]]
for i in range(0,len(arr),5):
  for j in range(0,len(arr[i]),5):
    for k in range(5):
      for l in range(5):
        if(i+k<len(arr) and j+l<len(arr[i])):
          if(arr[i+k][j+l]>=threshold[k][l]):
            brr[i+k].append(255)
          else:
            brr[i+k].append(0)
plt.imshow(brr,'gray')
plt.show()