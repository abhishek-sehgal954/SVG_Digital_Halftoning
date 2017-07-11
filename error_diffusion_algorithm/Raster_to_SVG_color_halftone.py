import numpy as np
from PIL import Image
import svgwrite
from error_diffusion import error_dispersion

dwg = svgwrite.Drawing('output.svg',profile='full',size=('30cm','30cm'),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')
def draw_svg(output,color):
  startu = 0
  endu = 0
  for i in range(len(output)):
  	for j in range(len(output[i])):
  		if (output[i][j]==0):
  			dwg.add(dwg.circle((int((startu+startu+1)/2),int((endu+endu+1)/2)),1,fill=color,style="mix-blend-mode: multiply;"))        
  		startu = startu+2                                                                               
  	endu = endu+2
  	startu = 0
  dwg.save() 



def main():
  fname = 'tree_small.jpg'
  image = Image.open(fname)
  cmyk = image.split()  
  output_cyan = error_dispersion(cmyk[0])
  output_magenta = error_dispersion(cmyk[1])
  output_yellow = error_dispersion(cmyk[2])
  draw_svg(output_cyan,'cyan')
  draw_svg(output_magenta,'magenta')
  draw_svg(output_yellow,'yellow')

if __name__=="__main__":
  main()