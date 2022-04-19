#
#https://pypi.org/project/graphviz/
import graphviz
import xml.etree.ElementTree as ET
import sys

dt = graphviz.Digraph(comment='smallGraph')

tree = ET.parse('callGraphfg.xml')
root = tree.getroot()
fcnroot = root

graphRoots = root.findall('.//root/..')


cts = {}
def subtree(sroots):
    #print(f'sroots: {sroots}')
    for r in sroots:
        #print(f"r: {r} r.tag: {r.tag} r.find('./id').text: {r.find('./id').text}")
        xps = './callee'
        for cle in r.findall(xps):
            #print(f'cle: {cle} {cle.text}')
            xps =  f"./functions/function/[id='{cle.text}']"
            subts = fcnroot.findall(xps)
            subtree(subts)
            for n in subts:
                dt.node(n.find('./id').text, n.find('./name').text)
            dt.edge(r.find('./id').text, cle.text)

subtree(graphRoots)

dt.render('tjyb.gv', view=True)
