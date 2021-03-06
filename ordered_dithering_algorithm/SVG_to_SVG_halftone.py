import os
import sys
import svgwrite
import numpy as np
from PIL import Image
import subprocess
from Raster_to_SVG_halftone import draw_svg
from ordered_dither import order_dither

def main():
	p=subprocess.call(['/usr/bin/inkscape', 'test_svg.svg', '--export-png', 'test_svg.jpg'])
	fname = 'test_svg.jpg'
	image = Image.open(fname).convert('L')
	output = order_dither(image)
  	draw_svg(output)
  		
if __name__=="__main__":
  main()