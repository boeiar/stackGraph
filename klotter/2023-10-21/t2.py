from pathlib import Path
import sys
import xml.etree.ElementTree as ET
tree = ET.parse('../CallGraph.xml')
root = tree.getroot()

graphName = root.tag
with open(Path(sys.argv[0]).with_suffix('.dot'),'w') as ofh:
    print(f'digraph {root.tag}', '{', file=ofh) 
    for mcc in root.findall("maxCallChains/maxCallChain"):
        oldnode = 'call_graphs_start'
        for e in mcc.findall("entry"):
            newnode = e.find("function").text
            print(f'\t {oldnode} ->  {newnode} ;', file=ofh)
            oldnode = newnode
    print('}', file=ofh)
