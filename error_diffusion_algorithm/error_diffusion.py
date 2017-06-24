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