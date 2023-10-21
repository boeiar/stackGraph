import xml.etree.ElementTree as ET
tree = ET.parse('../CallGraph.xml')
root = tree.getroot()

for mcc in root.findall("maxCallChains/maxCallChain"):
    print('top:', mcc.find("top").text)
    print('fcn\t\tstack')
    for e in mcc.findall("entry"):
        print(e.find("function").text, '\t\t', e.find("stack").text)
