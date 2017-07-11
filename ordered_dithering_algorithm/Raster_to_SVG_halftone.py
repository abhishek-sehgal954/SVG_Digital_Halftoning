import numpy as np
from PIL import Image
import svgwrite
from ordered_dither import order_dither

dwg = svgwrite.Drawing('output.svg',profile='full',size=('70cm','70cm'),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')

def draw_svg(output):
  startu = 0
  endu = 0
  for i in range(len(output)):
  	for j in range(len(output[i])):
  		if (output[i][j]==0):
  			dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1,fill='black'))        
  		startu = startu+2                                                                               
  	endu = endu+2
  	startu = 0
  dwg.save() 

def main():
  fname = 'test.jpg'
  image = Image.open(fname).convert('L')
  output = order_dither(image)
  draw_svg(output)

if __name__=="__main__":
  main()

