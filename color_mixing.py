import svgwrite
import webbrowser
import os

dwg = svgwrite.Drawing('test.svg',profile='full',viewBox=("0 0 1500 1500"),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')
blend = dwg.defs.add(dwg.filter(id="B4" ,filterUnits="objectBoundingBox", x="0%", y="0%", width="100%", height="100%"))
blend.feBlend(in_='SourceGraphic', mode='screen')
dwg.add( dwg.rect(insert=(550, 550), size=(500, 500), fill='magenta'))
dwg.add( dwg.rect(insert=(750, 600), size=(500, 500), opacity='0.5',fill='cyan',filter='url(#B4)' ))
dwg.add( dwg.rect(insert=(600, 750), size=(500, 500), opacity='0.5',fill='yellow',filter='url(#B4)' ))
dwg.save()
browser=webbrowser.get('firefox')
browser.open_new('file://' + os.path.realpath("test.svg")) 

