SIZE = 7
NUMBER = 6
INFINITE = 99999  # infinite

Graph_Matrix = [[0] * SIZE for row in range(SIZE)]  # the graph array
distance = [0] * SIZE  # the dist array of path


def BuildGraph_Matrix(Path_Cost):
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            if i == j:
                Graph_Matrix[i][j] = 0  # the diagonal is 0
            else:
                Graph_Matrix[i][j] = INFINITE

        # save edge to the graph
        i = 0
        while i < SIZE:
            Start_Point = Path_Cost[i][0]
            End_Point = Path_Cost[i][1]
            Graph_Matrix[Start_Point][End_Point] = Path_Cost[i][2]
            i += 1


# shortest distance satisfy, single point to the whole vertex
def shortestPath(vertext1, vertex_total):
    shortest_vertex = 1  # record the shortest distance from the vertex
    goal = [0] * SIZE  # descide whether the vertex should be record
    for i in range(1, vertex_total + 1):
        goal[i] = 0
        distance[i] = Graph_Matrix[vertext1][i]

    goal[vertext1] = 1
    distance[vertext1] = 0
    print()

    for i in range(1, vertex_total):
        shortest_distance = INFINITE
        for j in range(1, vertex_total + 1):
            if goal[j] == 0 and shortest_distance > distance[j]:
                shortest_distance = distance[j]
                shortest_vertex = j

        goal[shortest_vertex] = 1
        # calculate the shortest distance from vertex_1 to other vertexs
        for j in range(vertex_total + 1):
            if goal[j] == 0 and distance[shortest_vertex] + Graph_Matrix[shortest_vertex][j] < distance[j]:
                distance[j] = distance[shortest_vertex] + Graph_Matrix[shortest_vertex][j]


# main process
global Path_Cost
Path_Cost = [[1, 2, 29], [2, 3, 30], [2, 4, 35], [3, 5, 28], [3, 6, 87], [4, 5, 42], [4, 6, 75], [5, 6, 97]]

BuildGraph_Matrix(Path_Cost)
shortestPath(1, NUMBER)  # looking for the shortest path
print('-------------------------------------------')
print('the vertex 1 to each vertex distance result')
print('-------------------------------------------')
for j in range(1, SIZE):
    print('vertex 1 to vertex %2d shortest path is %3d' % (j, distance[j]))
print('-------------------------------------------')
print()
