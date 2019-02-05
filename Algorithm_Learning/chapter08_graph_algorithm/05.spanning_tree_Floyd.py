SIZE = 7
NUMBER = 6
INFINITE = 99999  # infinite

Graph_Matrix = [[0] * SIZE for row in range(SIZE)]  # graph array
distance = [[0] * SIZE for row in range(SIZE)]  # path array


# build the graph
def BuildGraph_Matrix(Path_Cost):
    for i in range(1, SIZE):
        for j in range(1, SIZE):
            if i == j:
                Graph_Matrix[i][j] = 0  # set diagonal as 0

            else:
                Graph_Matrix[i][j] = INFINITE

    # save graph to the edge
    i = 0
    while i < SIZE:
        Start_Point = Path_Cost[i][0]
        End_Point = Path_Cost[i][1]
        Graph_Matrix[Start_Point][End_Point] = Path_Cost[i][2]
        i += 1


# print out the graph
def shortestPath(vertex_total):
    # initialize the length of graph array
    for i in range(1, vertex_total + 1):
        for j in range(1, vertex_total + 1):
            distance[i][j] = Graph_Matrix[j][i]
            distance[j][i] = Graph_Matrix[j][i]

    # use Floyd algorithm to find the shortest path for each vertexs
    for k in range(1, vertex_total + 1):
        for i in range(1, vertex_total + 1):
            for j in range(1, vertex_total + 1):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]


Path_Cost = [[1, 2, 20], [2, 3, 30], [2, 4, 25], [3, 5, 28], [4, 5, 32], [4, 6, 95], [5, 6, 67]]
BuildGraph_Matrix(Path_Cost)
print('------------------------------------------')
print(' the distance for each vertexs : ')
print('------------------------------------------')
shortestPath(NUMBER)  # calculate the shortest path for each vertexs
print('\tvertex1\tvertex2\tvertex3\tvertex4\tvertex5\tvertex6')
for i in range(1, NUMBER + 1):
    print('vertex_%d ' % i, end='')
    for j in range(1, NUMBER + 1):
        print('%5d' % distance[i][j], end='\t')
    print()

print('------------------------------------------')
print()
