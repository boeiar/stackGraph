#https://aitechtrend.com/step-by-step-guide-to-using-graphviz-for-graph-visualization-in-python/

from graphviz import Graph, Digraph

dot = """
    node [shape=circle, style=filled, color=lightblue];
    edge [color=gray, penwidth=2];

    A [label="Node A"];
    B [label="Node B", color=red];
    C [label="Node C", shape=rectangle];
    D [label="Node D", style=dashed];

    A -> B;
    B -> C [color=blue];
    B -> D;
"""

g = Digraph(format='png')
g.engine = 'dot'
g.body.append(dot)
g.render('example', view=True)
