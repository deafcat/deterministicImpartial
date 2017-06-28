import networkx as nx

G= nx.DiGraph()
G.add_nodes_from([1,2,3])
print(G.nodes())
G.add_edge(1,2)
G.add_edge(2,1)
print(G.edges())
nx.set_node_attributes(G,'winner',{1: True, 2: False, 3:False})
print(G.nodes())
print(G.node[1]['winner'])
