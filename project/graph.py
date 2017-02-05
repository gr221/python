import networkx as nx

rdn_graph = nx.gnp_random_graph(10,0.5)
graph_dict = dict()
for i in rdn_graph.nodes():
    graph_dict.update({i:rdn_graph.neighbors(i)})
    print(i, rdn_graph.neighbors(i))

