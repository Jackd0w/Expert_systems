import graphviz

dot = graphviz.Digraph('Sattelite-ontology')

dot.node('A', 'Sattelite')
dot.node('B', 'Relay')
dot.node('C', 'PhotoElement')
dot.node('D', 'InfraElement')
dot.node('E', 'Signal')
dot.node('H', 'CUP')
dot.edge('A', 'B', label="Has")
dot.edge('A', 'C', label="Has")
dot.edge('A', 'D', label="Has")
dot.edge('H', 'E', label="Sends")
dot.edge('E', 'B', label="Receives")
dot.edge('E', 'C', label="Activate")
dot.edge('E', 'D', label="Activate")



dot.render(directory='doctest-output').replace('\\', '/')