Graph vs. chart
    A set of elements and the relations between those elements.
    A set of nodes (a.k.a. vertices) and the edges between those elements.
    A network.
Where do we use graphs?
    Social Network (person = node; edge = relationships)
    Transportation Networks
    Biological Networks
    Information Networks
Graph Types:
    Undirected Graph            A--B
    Directed Graph              A-->B
    Multi-Graph (directed)      A<-->B A<--
    Weighted Graph (directed)   A-10->B-20->C
                                ^-----25----/
Graphs in Code: To use a graph in code, we just need a list of nodes and a list of edges!
    nodes = ['A','B','C','D','E']
    edges= [('A','B'), ('B','C'), ('B','D'), 
            ('C','E'), ('D','A'), ('A','E')]
    digraph = (nodes, edges)

    class Graph:
       def __init__(self, nodes=None, edges=None):
          self.nodes = []
          self.edges = []

       def add_node(name):
          self.nodes.append(name)

       def add_edge(node, node):
          self.edges.append( (node, node) )

Adjacency: who is connected to whom
    Nodes that have an edge between them are adjacent (or "neighbors")
        G['A'] #neighbors of 'A'
        G.adj #adjacency dict
        #dict of dict of dicts
    A nodes degree is the number of edges it has (neighbors in simple graph)
        #degree of 'A'
        G.degree('A')

Adjacency Matrix - a table: embed as lists of lists or lists of dicts
    G.add_edge("A","B",weight =5, label ='besties')
    G['B']
    G.adj['B'] --> {A:{"weight":5, "label":'besties'}. 'C':{}. 'D': {}}
    G.adj #adjacency dict
    #row-dict of col-dicts of edge-dicts

    G.adj['A']['B'] #edge from A to B
    G['A']['B']     #edge from A to B --> {weight:5,label:'besties'}

    G['A']['D'] #KeyError, no such edge!

Connectivity:
    A list of adjacent nodes define a path through a graph
        #call method on module
        nx.has_path(G, 'A', 'C') --> True or False

    If there is a path between two nodes, they are connected (there is some sequence of adjacency that will get you from one node to another)

    A graph is connected if there is a path between every pair of nodes.
        nx.is_connected(G)

        #number of `components`
        nx.number_connected_components(G)

Cycles: A path of length > 1 that starts and ends at the same node is called a cycle
Trees: A graph without any cycles... is a tree!

Searching:
    Brute Force Method: Start at the beginning. Check a connected node. Then another. Then another. If you get to a dead-end, turn around.
    Depth-First Search (Stack-based: deep, then broad)
    Breadth-First Search (Queue-based: broad, then deep)

Traversals in Code
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
In NX:
    #list of edges in DFS
    nx.dfs_edges(G, 'A')
    #list of edges in BFS
    nx.bfs_edges(G, 'A')

Spanning Trees: tree that is a portion of your graph

A DFS or BFS finds a path...
 ...but which path is the shortest?

Floyd-Warshall Algorithm: An algorithm for finding the shortest path between "all-pairs" of nodes
    #initialize dist as dict of dicts 
    # each value is a dictionary of distances to the key
    # {1:{1:0, 2:inf, ...}, 2:{1:inf, 2:0, ...}, ...}
    for w in G: #each possible intermediate
       for u in G: #each start
          for v in G: #each destination destination
             #if distance u-w-v is shorter than u-v
             #save the new shorter distance
             if dist[u][w] + dist[w][v] < dist[u][v]:
                dist[u][v] = dist[u][w] + dist[w][v]

Force-Directed Layouts
    Use a simulation of physical forces to determine where to position nodes.
    Nodes: treat as same-charged magnets that "push" away from each other (Columbs Law)
    Edges: treat as springs that "pull" adjacent nodes together (Hookes Law)

Fruchterman-Reingold Algorithm
    #pseudocode

    #nodes repel each other
    for each node 'v'
      for each other node 'u'
        plan to move 'v' away from 'u' based on the distance between them

    #edges attract connected nodes
    for each edge
      plan to move nodes towards each other based on the distance between them

    #actually move the nodes
    for each node
      take the amount calculated to move, and apply it to the nodes
      make sure the nodes stay on the screen