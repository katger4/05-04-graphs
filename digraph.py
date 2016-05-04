import networkx as nx
import matplotlib.pyplot as plt
nodes = ['A','B','C','D','E']
edges= [('A','B'), ('B','C'), ('B','D'), ('C','E'), ('D','A'), ('A','E')]
# digraph = (nodes, edges)
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

nx.draw(G,pos=nx.spring_layout(G),node_color="pink",edge_color='#89cff0')
plt.show()
# print(G.edges())