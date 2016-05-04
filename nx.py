# #import the module
# import networkx as nx #aliased
# from networkx import Graph #for local access (instead of having to refer to nx.Graph())

# #make the graph
# G = Graph() #undirected graph

# #access nodes/edges
# print( G.nodes() ) #list of nodes
# print( G.edges() ) #list of edges

# #add nodes
# G.add_node('A')
# G.add_node('B')
# G.add_nodes_from(['C','D'])

# #add edges
# G.add_edge('A','B')
# G.add_edges_from([('B','C'), ('B','D'), ('D','A')]
# G.add_edges_from([('C','E'), ('A','E')]) #creates node E

###################example2
import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt

H = Graph()

H.add_edges_from([
   ('Alice',"Bob"), ('Alice','Charles'), 
   ('Bob', 'Gertrude'), ('Charles','Debbie'), 
   ('Charles', 'Gertrude'), ('Debbie','Edward'),
   ('Debbie','Gertrude'),('Edward','Gertrude'),
   ('Edward','Gertrude'),('Gertrude','Herbert'),
   ('Herbert','Fred')
])

# print("Nodes:")
# for node in H.nodes_iter(): #iterable of nodes - go thru nodes in a list (dont need to convert to list then iter)
#    print(node)

# print("\nEdges:")
# for edge in H.edges_iter():
#    print(edge)

nx.draw(H,pos=nx.spring_layout(H),node_color="pink",edge_color='#89cff0',with_labels=True, node_size=2500, node_shape="o", font_family="verdana", font_size=10, font_color='#3F3F3F', width=2.0)
# plt.show()

def print_depth_first_search(G, start, target):
   """Depth-first search of Graph G,
      starting at Node start, ending at Node target
   """
   #keep track of these 3 things:
   found = False
   to_visit = []
   visited = []
   to_visit.append(start) #start at start
   while(len(to_visit) > 0):
      current = to_visit.pop(0) #visit next node on list
      print("Visiting "+str(current))
      visited.append(current)

      if current == target: #found target
         found = True; break

      for node in G.neighbors(current): #go through neighbors
         if not node in visited and node not in to_visit:
            to_visit.insert(0, node) #add to front (stack)

   if not found:
      print("Target not reachable in graph")

print_depth_first_search(H, "Edward", "Gertrude")
# Visiting Edward
# Visiting Gertrude

def print_breadth_first_search(G, start, target):
   """Breadth-first search of Graph G,
      starting at Node start, ending at Node target
   """
   found = False
   to_visit = []
   visited = []
   to_visit.append(start) #start at start
   while(len(to_visit) > 0):
      current = to_visit.pop(0) #visit next node on list
      print("Visiting "+str(current))
      visited.append(current)

      if current == target: #found target
         found = True; break

      for node in G.neighbors(current): #go through neighbors
         if not node in visited and node not in to_visit:
            to_visit.append(node) #add to end (queue)

   if not found:
      print("Target not reachable in graph")

# print_breadth_first_search(H, "Edward", "Gertrude")
    # Visiting Edward
    # Visiting Debbie
    # Visiting Gertrude