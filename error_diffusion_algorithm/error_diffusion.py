"""function b=floyd(a)
width=size(a,2);
height=size(a,1);
err=zeros(size(a));
for x=1:width,
        for y=1:height,
                if (a(y,x)+err(y,x))<128, b(y,x)=0;
                else b(y,x)=255; 
                end;
                diff=(a(y,x)+err(y,x))-b(y,x);
                if x<width, err(y,x+1)=err(y,x+1)+diff*7/16; end;
                if y<height, 
                        err(y+1,x)=err(y+1,x)+diff*5/16;
                        if x>1, err(y+1,x-1)=err(y+1,x-1)+diff*3/16; end;
                        if x<width err(y+1,x+1)=err(y+1,x+1)+diff*1/16; end;
                end;
        end;
end;
f=figure('Position',[512,512,width,height]);
colormap(gray(256));
g=axes('Po"""
import numpy as np
from PIL import Image

def error_dispersion(image):
  arr = np.asarray(image)
  height = len(arr)
  width = len(arr[0])
  err = [[0]*len(arr[0]) for i in range(len(arr))]
  crr = np.zeros((len(arr),len(arr[0])))
  for i in range(height):
    for j in range(width):
      if(arr[i][j] + err[i][j] < 128):
        crr[i][j] = 0 
      else:
        crr[i][j] = 255
      diff = arr[i][j] + err[i][j] - crr[i][j]
      if(j+1 < width):
        err[i][j+1] = float(float(err[i][j+1]) + float(diff*float(float(7)/float(16))))
      if(i+1 < height):
        err[i+1][j] = float(float(err[i+1][j]) + float(diff*float(float(5)/float(16))))
      if(i+1 < height and j-1 >= 0):
        err[i+1][j-1] = float(float(err[i+1][j-1]) + float(diff*float(float(3)/float(16))))
      if(i+1 < height and j+1 < width):
        err[i+1][j+1] = float(float(err[i+1][j+1]) + float(diff*float(float(1)/float(16))))
  return crr

def main():
  fname = 'test2.jpg'
  image = Image.open(fname).convert('L')
  output = error_dispersion(image)
  im = Image.fromarray(output)
  im.convert('RGB').save("output.jpg")
  im.show()

if __name__=="__main__":
  main()