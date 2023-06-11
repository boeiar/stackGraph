import xml.etree.ElementTree as ET
tree = ET.parse('copy_of_CallGraph.xml')
root = tree.getroot()

fdict = {} 
fs=root.findall('.//functions/function')
for f in fs:
    fdict[f.find('./id').text] = f.find('./name').text

mccs=root.findall('.//maxCallChains/maxCallChain')
for mcc in mccs:
    print("")
    for fc in mcc.findall('./entry/function'):
        print(fdict[fc.text])
