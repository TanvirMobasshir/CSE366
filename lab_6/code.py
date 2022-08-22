graph = []
color = []


def is_safe(v, c):
    global graph, color
    i = 1
    while i < len(graph):
        if graph[v][i] == color[i] and c == color[i]:
            return False

        i += 1

    return True


def graph_coloring(m, v):
    global graph, color

    if v == len(graph):
        return True

    c = 0
    while c < m:
        if is_safe(v, c):
            color[v] = c

            if graph_coloring(m, v + 1):
                return True

            color[v] = -1

        c += 1

    return False


def print_solution():
    global color

    i = 1
    while i < len(color):
        print(color[i])
        i += 1


def initialize_graph_coloring(m):
    global graph, color

    color = [-1 for _ in range(len(graph))]
    if not graph_coloring(m, 1):
        print("NO")
        return

    print_solution()


if __name__ == '__main__':
    global graph, color

    v, e = map(int, input().split())
    graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    vertex, connectec_vertex = map(int, input().split())

    i = 0
    while i < e:
        vertex, connectec_vertex = map(int, input().split())
        graph[vertex][connectec_vertex] = 1
        graph[connectec_vertex][vertex] = 1

        i += 1

    m = int(input())

    initialize_graph_coloring(m)
