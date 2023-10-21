from graphviz import Graph, Digraph
import xml.etree.ElementTree as ET
tree = ET.parse('copy_of_CallGraph.xml')
root = tree.getroot()

graph = Digraph(format='png')
graph.engine = 'dot'

def dotrow(id,name):
    res  = '\t'
    res += id
    res += ' [label="'
    res += name
    res += '"];'
    return res

fdict = {} 
fs=root.findall('.//functions/function')
for f in fs:
    id = f.find('./id').text
    name = f.find('./name').text
    callees = f.findall('./callee')
    fdict[id] = name
    graph.node(id,name)
    for c in  callees:
        graph.edge(id, c.text)

graph.render('t.dot', view=True)

