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
    fdict[id] = name

mccs=root.findall('.//maxCallChains/maxCallChain')
for mcc in mccs:
#    topNode = mcc.find('./entry/top').text
#    graph.node(topNode, fdict[topNode].text)
    previous_f = None
    for f in mcc.findall('./entry/function'):
        graph.node(f.text, fdict[f.text])
        if (None != previous_f):
            graph.edge(previous_f.text, f.text)
        previous_f = f
graph.render('t.dot', view=True)
