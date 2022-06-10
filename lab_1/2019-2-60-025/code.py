def get_undirected_graph(number_of_verticies, number_of_edges):
    grph = []
    for m in range(number_of_verticies + 1):
        grph.append([])

    for i in range(number_of_edges):
        start, end = map(int, input().split())
        grph[start].append(end)
        if start != end:
            grph[end].append(start)

    return grph


def bfs(grph, src, des):
    queue = [src]

    distances = [-1] * len(grph)
    parent = [-1] * len(grph)

    distances[src] = 0
    explored_node = [-1] * len(grph)
    explored_node[src] = 1
    count = 1

    while queue:
        vertex = queue[0]
        queue.pop(0)

        for k in range(len(grph[vertex])):
            if count < len(grph)-1:
                if explored_node[grph[vertex][k]] == -1:
                    count += 1
                    explored_node[grph[vertex][k]] = count
            if distances[grph[vertex][k]] == -1:
                parent[grph[vertex][k]] = vertex
                distances[grph[vertex][k]] = distances[vertex] + 1

                queue.append(grph[vertex][k])

    # noinspection PyTypeChecker
    explored_node[0] = None

    print(distances[des])

    current = des
    paths = []

    while parent[current] != -1:
        step = str(parent[current]) + ' ' + str(current)
        paths.append(step)
        current = parent[current]

    s = len(paths) - 1
    while s >= 0:
        print(paths[s])
        s -= 1

    return explored_node


def exploration_tree(node_exploration_order):
    order = {0: None}
    for i in range(1, len(node_exploration_order)):
        order[i] = -1
    for i in node_exploration_order:
        if i:
            order[i] = node_exploration_order.index(i)

    print("Explored nodes in order: ", end=' ')
    for i in range(len(node_exploration_order)):
        if order[i]:
            print(order[i], end=' ')

    print()

    for i in range(len(node_exploration_order)):
        if i != 0:
            print(f'node: {i}, exploration order: {node_exploration_order[i]}')

    return


if __name__ == '__main__':
    verticies, edges = map(int, input().split())
    graph = get_undirected_graph(verticies, edges)
    source, destination = map(int, input().split())
    print()
    explored_nodes = bfs(graph, source, destination)
    print()
    exploration_tree(explored_nodes)
