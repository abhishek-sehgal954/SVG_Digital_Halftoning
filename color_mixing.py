
import svgwrite
import webbrowser
import os

dwg = svgwrite.Drawing('test.svg',profile='full',size=('70cm','70cm'),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')
dwg.add( dwg.rect(insert=(550, 550), size=(500, 500), fill='magenta',style="mix-blend-mode: multiply;"))
dwg.add( dwg.rect(insert=(750, 600), size=(500, 500),fill='cyan',style="mix-blend-mode: multiply;" ))
dwg.add( dwg.rect(insert=(600, 750), size=(500, 500),fill='yellow',style="mix-blend-mode: multiply;" ))
dwg.save()
browser=webbrowser.get('firefox')
browser.open_new('file://' + os.path.realpath("test.svg")) 