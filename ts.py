#
#https://pypi.org/project/graphviz/
import graphviz  # doctest: +NO_EXE
dot = graphviz.Digraph(comment='smallGraph')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
print(dot.source)
dot.render('doctest-output/round-table.gv').replace('\\', '/')
dot.render('doctest-output/round-table.gv', view=True)
