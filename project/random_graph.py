import random

#Generate n vertices
def generate_vertices(n):
    keys = []
    for i in range(n):
        keys.append(i)
    rdn_graph = dict.fromkeys(keys)
    for i in rdn_graph.keys():
        rdn_graph[i] = []
    return rdn_graph

# Generate the edges between the vertices, where probability is the probability to create an edge
# between two vertices
def generate_edges(rdn_graph, probability):
    for i in rdn_graph.keys():
        for j in range(i+1, len(rdn_graph.keys())):
            if (random.random() <= probability): 
                rdn_graph[i].append(j)
                rdn_graph[j].append(i)
