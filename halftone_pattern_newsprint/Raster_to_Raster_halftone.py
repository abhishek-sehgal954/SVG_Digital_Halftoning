import Image, ImageDraw, ImageStat

def gcr(im, percentage):
    '''basic "Gray Component Replacement" function. Returns a CMYK image with 
       percentage gray component removed from the CMY channels and put in the
       K channel, ie. for percentage=100, (41, 100, 255, 0) >> (0, 59, 214, 41)'''
    cmyk_im = im.convert('CMYK')
    if not percentage:
        return cmyk_im
    cmyk_im = cmyk_im.split()
    cmyk = []
    for i in xrange(4):
        cmyk.append(cmyk_im[i].load())
    for x in xrange(im.size[0]):
        for y in xrange(im.size[1]):
            gray = min(cmyk[0][x,y], cmyk[1][x,y], cmyk[2][x,y]) * percentage / 100
            for i in xrange(3):
                cmyk[i][x,y] = cmyk[i][x,y] - gray
            cmyk[3][x,y] = gray
    return Image.merge('CMYK', cmyk_im)

def halftone(im, cmyk, sample, scale):
    '''Returns list of half-tone images for cmyk image. sample (pixels), 
       determines the sample box size from the original image. The maximum 
       output dot diameter is given by sample * scale (which is also the number 
       of possible dot sizes). So sample=1 will presevere the original image 
       resolution, but scale must be >1 to allow variation in dot size.'''
    cmyk = cmyk.split()
    dots = []
    angle = 0
    for channel in cmyk:
        channel = channel.rotate(angle, expand=1)
        size = channel.size[0]*scale, channel.size[1]*scale
        half_tone = Image.new('L', size)
        draw = ImageDraw.Draw(half_tone)
        for x in xrange(0, channel.size[0], sample):
            for y in xrange(0, channel.size[1], sample):
                box = channel.crop((x, y, x + sample, y + sample))
                stat = ImageStat.Stat(box)
                diameter = (stat.mean[0] / 255)**0.5
                edge = 0.5*(1-diameter)
                x_pos, y_pos = (x+edge)*scale, (y+edge)*scale
                box_edge = sample*diameter*scale
                draw.ellipse((x_pos, y_pos, x_pos + box_edge, y_pos + box_edge), fill=255)
        half_tone = half_tone.rotate(-angle, expand=1)
        width_half, height_half = half_tone.size
        xx=(width_half-im.size[0]*scale) / 2
        yy=(height_half-im.size[1]*scale) / 2
        half_tone = half_tone.crop((xx, yy, xx + im.size[0]*scale, yy + im.size[1]*scale))
        dots.append(half_tone)
        angle += 15
    return dots

def main():
    im = Image.open("tree.jpg")
    cmyk = gcr(im, 0)
    dots = halftone(im, cmyk, 10, 1)
    im.show()
    new = Image.merge('CMYK', dots)
    new.show()
  
if __name__=="__main__":
  main()
