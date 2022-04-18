import xml.etree.ElementTree as ET
import json

from copy import copy

def dictify(r,root=True):
    if root:
        return {r.tag : dictify(r, False)}
    d=copy(r.attrib)
    if r.text:
        d["_text"]=r.text
    for x in r.findall("./*"):
        if x.tag not in d:
            d[x.tag]=[]
        d[x.tag].append(dictify(x,False))
    return d

tree = ET.parse('callGraphfg.xml')
root = tree.getroot()
dictroot = dictify(root)

with open('callGraph.json','w') as outfile:
    json.dump(dictroot, outfile)
