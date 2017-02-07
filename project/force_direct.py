import random_graph
import random
import matplotlib.pyplot as plt
import numpy as np

def rand_start_points(graph, xlim, ylim):
    # coordinates = dict.fromkeys(graph.keys())
    # for i in sorted(coordinates.keys()):
        # coordinates[i] = [random.uniform(-xlim, xlim), random.uniform(ylim, -ylim)]
    coordinates = np.ndarray((len(graph.keys()),2))
    for i in sorted(graph.keys()):
        # np.append(coordinates, [random.uniform(-xlim, xlim), random.uniform(ylim, -ylim)])
        print(i)
        coordinates[i][0] = random.uniform(-xlim, xlim)
        coordinates[i][1] = random.uniform(-ylim, ylim)
    return coordinates

# def spring_alg(graph, coordinates):
#     iterations = 10
#     for i in range(0, iterations)

def main():
    #The Limits of the coordinate system
    xlim = 100
    ylim = 100
    #Generate the random graph
    graph = random_graph.generate_vertices(10)
    random_graph.generate_edges(graph, 0.3)
    #Define the random start coordinates for visualization
    coordinates = rand_start_points(graph, xlim, ylim)

    # plt.plot(coordinates[:,0], coordinates[:,1], 'o')
    # plt.show()

if __name__=="__main__":
    main()
