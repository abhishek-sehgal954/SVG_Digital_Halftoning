#This program takes a raster image and produces its raster halftone using matrix thresholding.

""" In Fixed thresholding each pixel is compared to 128(threshold) and if it is greater than 128
then it is set to 255(white) else it is set to 0(black). In matrix thresholding we go block by block,
(in our case we have considered 5*5 block) and use a threshold matrix.
Threshold matrix is chosen in such a way that different bigger size dot patterns are produced"""



import numpy as np
from PIL import Image

def matrix_threshold(image):
	""" each submatrix of 5*5 is compared with the threshold matrix"""
	arr=np.asarray(image)
	brr = np.zeros((len(arr),len(arr[0])))
	threshold=[[5, 118, 160, 58, 17],[48,201,232,170,99],[129,211,252,242,150],[89,191,221,181,68],[38,78,140,108,27]]
	for i in range(0,len(arr),5):
		for j in range(0,len(arr[i]),5):
			for k in range(5):
				for l in range(5):
					if(i+k<len(arr) and j+l<len(arr[i])):
						if(arr[i+k][j+l]>=threshold[k][l]):
							brr[i+k][j+l]=255
						else:
							brr[i+k][j+l]=0
	return brr

def main():
	fname = 'test.jpg'
	image = Image.open(fname).convert('L')
	output=matrix_threshold(image)
	im = Image.fromarray(output)
	im.convert('RGB').save("output.jpg")
	im.show()

if __name__=="__main__":
  main()
