class Graph:

    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph = []

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    # The main function that finds shortest distances from src to
    # all other vertices using Bellman-Ford algorithm. The function
    # also detects negative weight cycle
    def BellmanFord(self, src):
        re = [float("Inf")] * self.V
        re[src] = 0
        for _ in range(self.V-1):
            for u,v,w in self.graph:
                if re[u] != float("Inf") and re[u] + w < re[v]:
                    re[v] = re[u] + w
        for u, v, w in self.graph:
            if re[u] != float("Inf") and re[u] + w < re[v]:
                print("Graph contains negative weight cycle")
                return

        # print all distance
        self.printArr(re)

# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # function call
    g.BellmanFord(0)