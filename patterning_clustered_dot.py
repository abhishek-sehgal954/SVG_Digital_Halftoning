#This program takes a raster image and produces its raster halftone using patterning algorithm.

"""
For each possible value in the image, we create and display a pattern of
pixels that approximates that value. Remembering the concept of spatial integration, 
if we choose the appropriate patterns we can simulate the appearance of various
intensity levels -- even though our display can only generate a limited set
of intensities.

For example, consider a 3 x 3 pattern. It can have one of 512 different
arrangements of pixels:  however, in terms of intensity, not all of them are
unique.  Since the number of black pixels in the pattern determines the
darkness of the pattern, we really have only 10 discrete intensity patterns
(including the all-white pattern), each one having one more black pixel than
the previous one.

But which 10 patterns?  Well, we can eliminate, right off the bat, patterns
like:

     ---        X--        --X        X--
     XXX or     -X-   or   -X-   or   X--
     ---        --X        X--        X--


because if they were repeated over a large area (a common occurrence in many
images) they would create vertical, horizontal, or diagonal lines. 
Also, studies have shown that the patterns should form a "growth
sequence:"  once a pixel is intensified for a particular value, it should
remain intensified for all subsequent values.  In this fashion, each pattern
is a superset of the previous one; this similarity between adjacent
intensity patterns minimizes any contouring artifacts.

Here is a good pattern for a 3-by-3 matrix which subscribes to the rules set
forth above: 


     ---   ---   ---   -X-   -XX   -XX   -XX   -XX   XXX   XXX
     ---   -X-   -XX   -XX   -XX   -XX   XXX   XXX   XXX   XXX
     ---   ---   ---   ---   ---   -X-   -X-   XX-   XX-   XXX


This pattern matrix effectively simulates a screened halftone with dots of
various sizes.  In large areas of constant value, the repetitive pattern
formed will be mostly artifact-free.

Obviously applying this patterning process to our image will triple its 
size in each direction.  Because of this, patterning can only be used where 
the display's spatial resolution is much
greater than that of the image.

Another limitation of patterning is that the effective spatial resolution is
decreased, since a multiple-pixel "cell" is used to simulate the single,
larger halftone dot.  The more intensity resolution we want, the larger the
halftone cell used and, by extension, the lower the spatial resolution.  

In the above example, using 3 x 3 patterning, we are able to simulate 10
intensity levels (not a very good rendering) but we must reduce the spatial
resolution to 1/3 of the original figure.  To get 64 intensity levels (a
very acceptable rendering), we would have to go to an 8 x 8 pattern and an
eight-fold decrease in spatial resolution.  And to get the full 256 levels
of intensity in our source image, we would need a 16 x 16 pattern and would
incur a 16-fold reduction in spatial resolution.  Because of this size
distortion of the image, and with the development of more effective digital
halftoning methods, patterning is only infrequently used today."""



import numpy as np
from PIL import Image


def patterning(image):
    #  first calcluates intensity of a pixel from 0 to 9 and the based on the intensity maps it 
    #  to the corresponding block of 3*3 
    #  ---   ---   ---   -X-   -XX   -XX   -XX   -XX   XXX   XXX
    #  ---   -X-   -XX   -XX   -XX   -XX   XXX   XXX   XXX   XXX
    #  ---   ---   ---   ---   ---   -X-   -X-   XX-   XX-   XXX
    #  9     8     7     6     5     4     3     2     1     0  
    #  X = 0
    #  - = 255
    #  Therefore intensity 0 being the blackest block.
  arr = np.asarray(image)
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
  gray_level = [[[0,0,0],[0,0,0],[0,0,0]] for i in range(10)]

  gray_level[0] = [[0,0,0],[0,0,0],[0,0,0]];
  gray_level[1] = [[0,255,0],[0,0,0],[0,0,0]];
  gray_level[2] = [[0,255,0],[0,0,0],[0,0,255]];
  gray_level[3] = [[255,255,0],[0,0,0],[0,0,255]];
  gray_level[4] = [[255,255,0],[0,0,0],[255,0,255]];
  gray_level[5] = [[255,255,255],[0,0,0],[255,0,255]];
  gray_level[6] = [[255,255,255],[0,0,255],[255,0,255]];
  gray_level[7] = [[255,255,255],[0,0,255],[255,255,255]];
  gray_level[8] = [[255,255,255],[255,0,255],[255,255,255]];
  gray_level[9] = [[255,255,255],[255,255,255],[255,255,255]];
  crr = np.zeros((len(arr)*3,len(arr[0])*3))
  cnt=0
  for i in range(len(brr)):
    cnt+=1
    for j in range(len(brr[i])):
      new_i = i+2*(i-1)
      new_j = j+2*(j-1)
      for k in range(3):
        for l in range(3):
          crr[new_i+k][new_j+l] = gray_level[brr[i][j]][k][l]
  return crr

def main():
  fname = 'test.jpg'
  image = Image.open(fname).convert('L')
  output = patterning(image)
  im = Image.fromarray(output)
  im.convert('RGB').save("output.jpg")
  im.show()

if __name__=="__main__":
  main()