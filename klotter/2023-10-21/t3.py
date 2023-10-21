from pathlib import Path
import sys
import xml.etree.ElementTree as ET
tree = ET.parse('../CallGraph.xml')
root = tree.getroot()

graphName = root.tag
functions = root.find("functions")
with open(Path(sys.argv[0]).with_suffix('.dot'),'w') as ofh:
    print(f'digraph {root.tag}', '{', file=ofh) 
    for mcc in root.findall("maxCallChains/maxCallChain"):
        oldnode = 'call_graphs_start'
        for e in mcc.findall("entry"):
            newnodeNumber = e.find("function").text
            newnodeName = functions.find(f"*[id='{newnodeNumber}']").find("name").text
            #newnode = f"{newnodeName} ({newnodeNumber})"
            newnode = newnodeName
            print(f'\t {oldnode} ->  {newnode} ;', file=ofh)
            oldnode = newnode
    print('}', file=ofh)
