import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
fname = 'test.jpg'
image = Image.open(fname)
image = Image.open(fname).convert('L')
arr=np.asarray(image)
brr=[[] for i in range(len(arr))]
for i in range(len(arr)):
	for j in range(len(arr[i])):
		if(arr[i][j] > 128):
			brr[i].append(255)
		else:
			brr[i].append(0)
plt.imshow(brr,'gray')
plt.show()
