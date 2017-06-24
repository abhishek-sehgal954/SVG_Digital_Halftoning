import numpy as np
from PIL import Image


def intensity(arr):
  #  calcluates intensity of a pixel from 0 to 9
  mini = 999
  maxi = 0
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      maxi = max(arr[i][j],maxi)
      mini = min(arr[i][j],mini)
  level = float(float(maxi-mini)/float(10));
  brr = [[0]*len(arr[0]) for i in range(len(arr))]
  for i in range(10):
    l1 = mini+level*i
    l2 = l1+level
    for j in range(len(arr)):
      for k in range(len(arr[0])):
        if(arr[j][k] >= l1 and arr[j][k] <= l2):
          brr[j][k]=i
  return brr

def order_dither(image):
  arr = np.asarray(image)
  brr = intensity(arr)
  crr = [[8, 3, 4], [6, 1, 2], [7, 5, 9]]
  drr = np.zeros((len(arr),len(arr[0])))
  for i in range(len(arr)):
    for j in range(len(arr[0])):
      if(brr[i][j] > crr[i%3][j%3]):
        drr[i][j] = 255
      else:
        drr[i][j] = 0
  return drr

def main():
  fname = 'test.jpg'
  image = Image.open(fname).convert('L')
  output = order_dither(image)
  im = Image.fromarray(output)
  im.convert('RGB').save("output.jpg")
  im.show()

if __name__=="__main__":
  main()

