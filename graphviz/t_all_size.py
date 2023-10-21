import math
from graphviz import Graph, Digraph
import xml.etree.ElementTree as ET
tree = ET.parse('mod_copy_of_CallGraph.xml')
root = tree.getroot()

graph = Digraph(format='png')
graph.engine = 'dot'

fdict = {} 
fs=root.findall('.//functions/function')
for f in fs:
    id = f.find('./id').text
    name = f.find('./name').text
    stack = f.find('./stack').text
    size = str( int(stack) / len(fs))
    callees = f.findall('./callee')
    fdict[id] = name
    graph.node(id,name, shape='rectangle', height=size, style="filled", color = "#80808020", fixedsize="shape")
    for c in  callees:
        graph.edge(id, c.text)

graph.render('t.dot', view=True)

