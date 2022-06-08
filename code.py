def create_undirected_graph(number_of_edges):
    grph = []

    for m in range(1, number_of_edges + 1):
        grph.append([])

    for i in range(number_of_edges):
        start, end = map(int, input().split())
        grph[start].append(end)
        if start != end:
            grph[end].append(start)

    return grph


def bfs(number_of_verticies, grph, src, des):
    distances = [None]
    queue = []
    for j in range(number_of_verticies):
        distances.append(-1)

    distances[src] = 0
    queue.append(src)
    print(distances)
    print()

    while len(queue) != 0:
        vertex = queue[0]

        for k in range(len(grph[vertex])):
            print(f'k: {k}')
            print(grph[vertex][k])
            if distances[grph[vertex][k]] == -1:
                distances[grph[vertex][k]] = distances[vertex] + 1
                queue.append(grph[vertex][k])
            else: print("no action")
            print(distances)
            print(f'queue: {queue}')
            print()

        queue.pop(0)

    return


if __name__ == '__main__':
    verticies, edges = map(int, input().split())
    graph = create_undirected_graph(edges)
    source, destination = map(int, input().split())

    print(graph)

    bfs(verticies, graph, source, destination)
