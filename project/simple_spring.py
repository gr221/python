import graph_class
import numpy as np

class Simple_spring(graph_class.Graph_random):
    def __init__(self, nr_vertices, edge_prob, c_1, c_2, c_3, c_4):
        super().__init__(nr_vertices, edge_prob)
        self.c_1 = c_1
        self.c_2 = c_2
        self.c_3 = c_3
        self.c_4 = c_4
        self.forces_repel = np.ndarray((self.nr_vertices, self.nr_vertices))
        self.forces_repel_vec = np.ndarray((self.nr_vertices, self.nr_vertices, 2))
        self.forces_attract = np.zeros((self.nr_vertices, self.nr_vertices))
        self.forces_attract_vec = np.zeros((self.nr_vertices, self.nr_vertices, 2))
        self.forces_complete_vec = np.zeros((self.nr_vertices, 2))

    def calc_repel_force(self):
        # Calculate the absolute value of the repellent forces where the force  
        # follows an inverse square law with respect to the distance betwwen the
        # vertices 
        for j in range(0, self.nr_vertices):
            self.forces_repel[j][j] = 0
            self.forces_repel_vec[j][j][:] = 0
            for i in range(j+1, self.nr_vertices):
                dist = self.distances[j][i] * self.distances[j][i]
                force = self.c_3/dist
                self.forces_repel[j][i] = force
                self.forces_repel[i][j] = force
                z = force / self.distances[j][i]
                # Every row is one vertex were you a x and y component of every other vertex [[[x_1,y_0]...]]
                self.forces_repel_vec[i][j][0] = -z*self.distances_vec[i][j][0]
                self.forces_repel_vec[i][j][1] = -z*self.distances_vec[i][j][1]
                self.forces_repel_vec[j][i][0] = -z*self.distances_vec[j][i][0]
                self.forces_repel_vec[j][i][1] = -z*self.distances_vec[j][i][1]

    def calc_attract_force(self):
        # Calculate the attractive forces where a logarithmic scale law is applied
        for i in range(0, self.nr_vertices):
            for j in self.rdn_graph[i]:
                if self.forces_attract[i][j] == 0:
                    dist = self.distances[i][j]
                    force = self.c_1*np.log10(dist/self.c_2)
                    self.forces_attract[i][j] = force
                    self.forces_attract[j][i] = force
                    z = force / self.distances[i][j]
                    self.forces_attract_vec[i][j][0] = z*self.distances_vec[i][j][0]
                    self.forces_attract_vec[i][j][1] = z*self.distances_vec[i][j][1]
                    self.forces_attract_vec[j][i][0] = z*self.distances_vec[j][i][0]
                    self.forces_attract_vec[j][i][1] = z*self.distances_vec[j][i][1]

    def calc_complete_force(self):
        for i in range(self.nr_vertices):
            for j in range(self.nr_vertices):
                self.forces_complete_vec[i][0] += self.forces_repel_vec[i][j][0]
                self.forces_complete_vec[i][0] += self.forces_attract_vec[i][j][0]
                self.forces_complete_vec[i][1] += self.forces_repel_vec[i][j][1]
                self.forces_complete_vec[i][1] += self.forces_attract_vec[i][j][1]

    def update_position(self):
        for i in range(self.nr_vertices):
            self.coordinates[i][0] += self.c_4 * self.forces_complete_vec[i][0]
            self.coordinates[i][1] += self.c_4 * self.forces_complete_vec[i][1]

    def complete_alg(self, N):
        for i in range(N):
            self.calc_repel_force()
            self.calc_attract_force()
            self.calc_complete_force()
            self.update_position()

def main():
    spring = Simple_spring(10, 0.2, 2, 1, 1, 0.1)
    spring.plot_graph()
    spring.complete_alg(200)
    spring.plot_graph()
    spring.complete_alg(200)
    spring.plot_graph()

if __name__=="__main__":
    main()
