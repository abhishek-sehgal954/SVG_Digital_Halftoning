#This program takes a raster image and produces its raster halftone using fixed thresholding.

"""
Fixed Thresholding

A good place to start is with the example of performing a simple (or fixed)
thresholding operation on our grayscale image in order to display it on our
black and white device.  This is accomplished by establishing a demarcation
point, or threshold, at the 50% gray level.  Each dot of the source image is
compared against this threshold value: if it is darker than the value, the
device plots it black, and if it's lighter, the device plots it white.
  
What happens to the image during this operation?  Well, some detail
survives, but our perception of gray levels is completely gone.  This means
that a lot of the image content is obliterated.  Take an area of the image
which is made up of various gray shades in the range of 60-90%.  After fixed
thresholding, all of those shades (being darker than the 50% gray threshold)
will be mapped to solid black.  So much for variations of intensity.

Another portion of the image might show an object with an increasing,
diffused shadow across one of its surfaces, with gray shades in the range of
20-70%.  This gradual variation in intensity will be lost in fixed
thresholding, giving way to two separate areas (one white, one black) and a
distinct, visible boundary between them.  The situation where a transition
from one intensity or shade to another is very conspicuous is known as
contouring.

"""



import numpy as np
from PIL import Image

def fixed_threshold(image):
	"""each pixel is compared with 128, if it is greater, it is set to 255(white) 
	else it is set to 0(black)"""
	arr = np.asarray(image)
	brr = np.zeros((len(arr),len(arr[0])))
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			if(arr[i][j] > 128):
				brr[i][j] = 255
			else:
				brr[i][j] = 0
	return brr

def main():
	fname = 'test.jpg'
	image = Image.open(fname).convert('L')
	output = fixed_threshold(image)
	im = Image.fromarray(output)
	im.convert('RGB').save("output.jpg")
	im.show()

if __name__=="__main__":
  main()


