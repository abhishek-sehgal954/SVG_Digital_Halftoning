import os
import webbrowser
import sys
import svgwrite
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import subprocess
from Raster_to_SVG_halftone import intensity_dot, intensity_triangle, intensity_hexagon


p=subprocess.call(['/usr/bin/inkscape', 'test2.svg', '--export-png', 'test2.png'])
fname = 'test2.png'
image = Image.open(fname)
image = Image.open(fname).convert('L')
if(sys.argv[1] == 'dot'):
  intensity_dot(image)
elif(sys.argv[1] == 'triangle'):
  intensity_triangle(image)
elif(sys.argv[1]=='hexagon'):
  intensity_hexagon(image)
