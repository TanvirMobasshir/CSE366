def is_safe(graph, v, color, c):
    i = 1
    while len(graph) > i:
        if graph[v][i] and c == color:
            return False

        i += 1

    return True


def graph_coloring(graph, m, color, v):
    if v == len(graph):
        return True

    c = 0
    while c < m:
        if is_safe(graph, v, color, c):
            color[v] = c

            if graph_coloring(graph, m, color, v + 1):
                return True

            color[v] = -1

        c += 1

    return False


def print_solution(color):
    i = 0
    while i < len(color):
        print(color[i])
        i += 1


def initialize_graph_coloring(graph, m):
    color = [-1 for _ in range(len(graph))]

    if not graph_coloring(graph, m, color, 1):
        print("NO")
        return

    print_solution(color)


if __name__ == '__main__':
    v, e = map(int, input().split())

    graph = [[0 for _ in range(v + 1)] for _ in range(v + 1)]

    i = 0
    while i < e:
        vertex, connected_vertex = map(int, input().split())
        graph[vertex][connected_vertex] = 1
        graph[connected_vertex][vertex] = 1

        i += 1

    m = int(input())

    print(graph)
    initialize_graph_coloring(graph, m)
