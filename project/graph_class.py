import random
import numpy as np
import matplotlib.pyplot as plt

class Graph_random(object):
    def __init__(self, nr_vertices, edge_prob):
        super().__init__()
        self.rdn_graph = self.generate_vertices(nr_vertices)
        self.nr_vertices = nr_vertices
        self.generate_edges(self.rdn_graph, edge_prob)
        self.xlim = 3*nr_vertices
        self.ylim = 3*nr_vertices
        self.coordinates = self.rand_start_points()
        self.distances, self.distances_vec = self.graph_distances()

    #Generate n vertices
    def generate_vertices(self, n):
        keys = []
        for i in range(n):
            keys.append(i)
        rdn_graph = dict.fromkeys(keys)
        for i in rdn_graph.keys():
            rdn_graph[i] = []
        return rdn_graph

    # Generate the edges between the vertices, where probability is the probability to create an edge
    # between two vertices
    def generate_edges(self, rdn_graph, probability):
        for i in range(0, self.nr_vertices):
            for j in range(i+1, self.nr_vertices):
                if (random.random() <= probability):
                    rdn_graph[i].append(j)
                    rdn_graph[j].append(i)

    # Chooses random start points for the graph layout within xlim and ylim
    def rand_start_points(self):
        coordinates = np.ndarray((self.nr_vertices,2))
        for i in range(0, self.nr_vertices):
            # randint to test -> change to uniform later
            coordinates[i][0] = random.randint(-self.xlim, self.xlim)
            coordinates[i][1] = random.randint(-self.ylim, self.ylim)
        return coordinates

    # Calculates the distances between vertex1 and vertex2 and returns a tuple 
    # of the distance and the vector between the two from vertex 1 to vertex2
    def calc_dist(self, vert_1, vert_2):
        d_vec = []
        d_vec.append(-self.coordinates[vert_1][0] + self.coordinates[vert_2][0])
        d_vec.append(-self.coordinates[vert_1][1] + self.coordinates[vert_2][1])
        distance = np.sqrt(d_vec[0]*d_vec[0] + d_vec[1]*d_vec[1])
        return distance, d_vec

    # calculate all distances between the vertices in the graph and return the 
    # corresponding absolute values and vectors
    def graph_distances(self):
        distances = np.ndarray((self.nr_vertices, self.nr_vertices))
        distances_vec = np.ndarray((self.nr_vertices, self.nr_vertices, 2))
        for i in range(0, self.nr_vertices):
            for j in range(0, self.nr_vertices):
                tmp  = self.calc_dist(i, j)
                distances[i][j] = tmp[0]
                distances_vec[i][j] = tmp[1]
        return distances, distances_vec

    def plot_graph(self):
        labels = ['{0}'.format(i) for i in range(self.nr_vertices)]
        fig1 = plt.figure()
        ax = plt.axes(frameon=False)
        ax.set_axis_off()
        ax.scatter(self.coordinates[:,0], self.coordinates[:,1], s=200. )
        for label, x, y in zip(labels, self.coordinates[:,0], self.coordinates[:,1]):
            ax.annotate(label, xy=(x,y), xytext=(0, 20), textcoords='offset points')

        for i in range(0, self.nr_vertices):
            connected = self.rdn_graph[i]
            x_val = [self.coordinates[i][0]]
            y_val = [self.coordinates[i][1]]
            for j in connected:
                x_val.append(self.coordinates[j][0])
                y_val.append(self.coordinates[j][1])
                ax.plot(x_val, y_val, 'r-', linewidth=0.2)
                x_val.pop()
                y_val.pop()

        plt.show()

def main():
    graph = Graph_random(3, 0.1)
    print(graph.rdn_graph)
    print(graph.coordinates)
    print(graph.distances_vec)
    # graph.plot_graph()

if __name__=="__main__":
    main()
