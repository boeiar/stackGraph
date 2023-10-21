#
#https://docs.python.org/3.10/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET
tree = ET.parse('tut.xml')
root = tree.getroot()
print(f'root.tag: {root.tag}');
print(f'root.attrib: {root.attrib}');

print('child.tag\t\tchild.attrib')
for child in root:
    print(child.tag, '\t\t', child.attrib)

print('neighbor.attrib')
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print('name \t\t rank')    
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, '\t\t', rank)    
