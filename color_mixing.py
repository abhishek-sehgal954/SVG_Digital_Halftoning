import svgwrite

progname = 'example_filter_on_group'

def create_svg(name):

    svg_size_w = 900
    svg_size_h = 1500
    title_size = 20
    y = 0
    title = name + ': example of filter on a group'

    dwg = svgwrite.Drawing(name,profile='full',viewBox=("0 0 3000 3000"),id='f-multiply-opacity',preserveAspectRatio='xMinYMin meet')
    blur6_filter = dwg.defs.add(dwg.filter(id="B4" ,filterUnits="objectBoundingBox", x="0%", y="0%", width="100%", height="100%"))
    blur6_filter.feBlend(in_='SourceGraphic', mode='screen')
    dwg.add( dwg.rect(insert=(550, 550), size=(500, 500), fill='magenta'))
    dwg.add( dwg.rect(insert=(750, 600), size=(500, 500), opacity='0.5',fill='cyan',filter='url(#B4)' ))
    dwg.add( dwg.rect(insert=(600, 750), size=(500, 500), opacity='0.5',fill='yellow',filter='url(#B4)' ))
    dwg.save()

if __name__ == '__main__':
    create_svg(progname + '.svg')