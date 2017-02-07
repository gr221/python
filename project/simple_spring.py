import graph_class
import numpy as np

class Simple_spring(Graph_random):
    def __init__(self, nr_vertices, edge_prob):
        super().__init__(nr_vertices, edge_prob)
