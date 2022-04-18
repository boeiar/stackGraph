from xml.etree import ElementTree as ET
import json
tree = ET.parse('callGraphfg.xml')
root = tree.getroot()

def xml_to_dict_recursive(root):
    if len(list(root)) == 0:
        return {root.tag:root.text}
    else:
        return {root.tag:list(map(xml_to_dict_recursive, list(root)))}

dfromr = xml_to_dict_recursive(root)

with open('callGraph_x2d.json','w') as outfile:
    json.dump(dfromr, outfile)
