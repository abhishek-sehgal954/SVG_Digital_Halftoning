#This program takes a vector image and produces its vector halftone using patterning algorithm .
# It supports 4 patterns 
# 1. Clustered dot
# 2. Triangle
# 3. Hexagon
# 4. Dispersed dot
# output file produced is output.svg which can be opened with any SVG viewer (inkscape, imagemagick etc.)

import os
import sys
import svgwrite
import numpy as np
from PIL import Image
import subprocess
from Raster_to_SVG_halftone import clustered_dot, triangle, hexagon, dispersed_dot

def main():
	p=subprocess.call(['/usr/bin/inkscape', 'test_svg.svg', '--export-png', 'test_svg.jpg'])
	fname = 'test_svg.jpg'
	image = Image.open(fname).convert('L')
	if(sys.argv[1] == 'clustered_dot'):
  		clustered_dot(image)
	elif(sys.argv[1] == 'triangle'):
  		triangle(image)
	elif(sys.argv[1] == 'hexagon'):
  		hexagon(image)
	elif(sys.argv[1] == 'dispersed'):
  		dispersed_dot(image)	
if __name__=="__main__":
  main()