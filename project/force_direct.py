import random_graph
import random
import matplotlib.pyplot as plt
import numpy as np

# Chooses random start points for the graph layout within xlim and ylim
def rand_start_points(graph, xlim, ylim):
    coordinates = np.ndarray((len(graph.keys()),2))
    for i in sorted(graph.keys()):
        # randint to test -> change to uniform later
        coordinates[i][0] = random.randint(-xlim, xlim)
        coordinates[i][1] = random.randint(-ylim, ylim)
    return coordinates

# Calculates the distances between vertex1 and vertex2 and returns a tuple 
# of the distance and the vector between the two from vertex 1 to vertex2
def calc_dist(coordinates, vert_1, vert_2):
    d_vec = []
    d_vec.append(-coordinates[vert_1][0] + coordinates[vert_2][0])
    d_vec.append(-coordinates[vert_1][1] + coordinates[vert_2][1])
    distance = np.sqrt(d_vec[0]*d_vec[0] + d_vec[1]*d_vec[1])
    return distance, d_vec

# calculate all distances between the vertices in the graph and return the 
# corresponding absolute values and vectors
def graph_distances(graph, coordinates):
    distances = np.ndarray((len(graph.keys()), len(graph.keys())))
    distances_vec = np.ndarray((len(graph.keys()), len(graph.keys()),2))
    for i in sorted(graph.keys()):
        for j in sorted(graph.keys()):
            tmp  = calc_dist(coordinates, i, j)
            distances[i][j] = tmp[0]
            distances_vec[i][j] = tmp[1]
    return distances, distances_vec


def calc_attractive_force(graph, coordinates, distances, distances_vec, c_1, c_2):
    forces = np.ndarray((len(graph.keys()),2))
    for i in graph.keys():
        print("jo")

# def spring_alg(graph, coordinates, iterations):
#     for i in range(0, iterations):

def main():
    #The Limits of the coordinate system
    xlim = 10
    ylim = 10
    #Generate the random graph
    graph = random_graph.generate_vertices(3)
    random_graph.generate_edges(graph, 0.3)
    #Define the random start coordinates for visualization
    coordinates = rand_start_points(graph, xlim, ylim)
    distances, distances_vec = graph_distances(graph, coordinates)

    # plt.plot(coordinates[:,0], coordinates[:,1], 'o')
    # plt.show()

if __name__=="__main__":
    main()
