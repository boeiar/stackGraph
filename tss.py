#
#https://pypi.org/project/graphviz/
import xml.etree.ElementTree as ET
import graphviz  # doctest: +NO_EXE

dt = graphviz.Digraph(comment='ssmallGraph')

tree = ET.parse('ssmallGraph.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)
for f in root.findall('./functions/function'):
    id = f.find('id').text
    dt.node(id, f.find('name').text)
    for callee in f.findall('callee'):
        dt.edge(id, callee.text)
    
print(dt.source)
#dot.render('doctest-output/round-table.gv').replace('\\', '/')
dt.render('doctest-output/round-table.gv', view=True)

