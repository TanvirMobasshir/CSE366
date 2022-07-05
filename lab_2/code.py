import sys


class Element:
    vertex = None
    distance = None

    def __init__(self, v, d):
        self.vertex = v
        self.distance = d


def get_undirected_weighted_graph(number_of_verticies, number_of_edges):
    grph = [[] for i in range(number_of_verticies + 1)]
    wghts = [[] for i in range(number_of_verticies + 1)]

    for i in range(number_of_edges):
        start, end, distance = map(int, input().split())
        grph[start].append(end)
        wghts[start].append(distance)
        if start != end:
            grph[end].append(start)
            wghts[end].append(distance)

    return [grph, wghts]


def print_paths(parents, destination, source):
    unreachable = False

    path = []

    while destination != source:
        if destination == -1:
            unreachable = True
            break

        path.append(destination)
        destination = parents[destination]

    if not unreachable:
        print(len(path)+1)
        print(source)

        while len(path) != 0:
            top = path[0]
            path.pop(-1)
            print(top)
    else:
        print(-1)


def dijkstra(graph, weights, source, destination):
    max_int = sys.maxsize

    distances = [max_int for i in range(len(graph))]
    visited = [False for i in range(len(graph))]
    parents = [-1 for i in range(len(graph))]
    final_visited = [0 for i in range(len(graph))]

    distances[source] = 0

    pq = [Element(source, 0)]

    while len(pq) != 0:
        vertex = pq[0].vertex
        pq.pop(0)

        if visited[vertex]:
            continue

        count = 0
        for i in visited:
            if i:
                count += 1

        explored_nodes = count
        final_visited[vertex] = explored_nodes
        visited[vertex] = True

        i = 0
        while i < len(graph[vertex]):
            neighbour = graph[vertex][i]
            distance = weights[vertex][i]

            if distances[vertex] + distance < distances[neighbour]:
                parents[neighbour] = vertex
                distances[neighbour] = distances[vertex] + distance
                pq.append(Element(neighbour, distances[neighbour]))

            i += 1

    print(distances[destination])
    print_paths(parents, destination, source)
    print(final_visited[destination])

    return


if __name__ == '__main__':
    vertices, edge = map(int, input().split())
    g, w = get_undirected_weighted_graph(vertices, edge)

    src, des = map(int, input().split())
    dijkstra(graph=g, weights=w, source=src, destination=des)
