import xml.etree.ElementTree as ET

tree = ET.parse('tut.xml')
root = tree.getroot()

sq = "'"                        # single quote
sl = "============="            # separator line

# Top-level elements
print('root.findall(".")')
print(root.findall("."))
print(sl)

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
print('root.findall("./country/neighbor")')
print(root.findall("./country/neighbor"))
print(sl)

# Nodes with name='Singapore' that have a 'year' child
print('root.findall(".//year/..[@name=' + sq + 'Singapore' + sq + ']")')
print(root.findall(".//year/..[@name='Singapore']"))
print(sl)

# 'year' nodes that are children of nodes with name='Singapore'
print('root.findall(".//*[@name='+ sq + 'Singapore' + sq + ']/year")')
print(root.findall(".//*[@name='Singapore']/year"))
print(sl)

# All 'neighbor' nodes that are the second child of their parent
print('root.findall(".//neighbor[2]")')
print(root.findall(".//neighbor[2]"))
print(sl)
