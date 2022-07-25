WHITE = 0
GREY = 1
BLACK = 2
has_cycle = False
vertices_traversed = 0
colors = []
dfs_costs = []
vertices_traversed_to_reach = []
parents = []


def get_undirected_weighted_graph(number_of_verticies, number_of_edges):
    costs = [[] for _ in range(number_of_verticies + 1)]
    grph = [[] for _ in range(number_of_verticies + 1)]

    for i in range(number_of_edges):
        start, end, distance = map(int, input().split())
        grph[start].append(end)
        costs[start].append(distance)
        if start != end:
            grph[end].append(start)
            costs[end].append(distance)

    return [grph, costs]


def foo(x):
    global colors, dfs_costs, vertices_traversed_to_reach, parents
    colors = [0 for _ in range(x)]
    dfs_costs = [0 for _ in range(x)]
    vertices_traversed_to_reach = [0 for _ in range(x)]
    parents = [-1 for _ in range(x)]


def print_path(destination, source):
    unreachable = False
    path = []

    while destination != source:
        if destination == -1:
            unreachable = True
            break

        path.append(destination)
        destination = parents[destination]

    if not unreachable:
        print(len(path) + 1)
        print(source)

        while len(path) != 0:
            top = path[-1]
            path.pop()
            print(top)
    else:
        print(-1)


def DFS(graph, costs, source, cost, limit):
    global vertices_traversed
    colors[source] = GREY
    dfs_costs[source] += cost
    vertices_traversed_to_reach[source] = vertices_traversed
    vertices_traversed += 1

    if limit <= 0:
        return

    i = 0
    while i < len(graph[source]):
        neighbour = graph[source][i]
        if colors[neighbour] == WHITE:
            parents[neighbour] = source
            DFS(graph, costs, neighbour, dfs_costs[source] + costs[source][i], limit-1)

        i += 1

    colors[source] = BLACK


def IDS(graph, costs, source, destination, max_limit):
    i = 0
    while i <= max_limit:
        DFS(graph, costs, source, 0, i)

        if colors[destination] != WHITE:
            print(f"Iterative depth {i}")
            print(f"{dfs_costs[destination]}")
            print_path(destination, source)

            print(f"{vertices_traversed_to_reach[destination]}")
            break

        for k in range(len(colors)):
            colors[k] = WHITE
            dfs_costs[k] = 0
            vertices_traversed_to_reach[k] = 0
            parents[k] = -1

        i += 1


if __name__ == '__main__':
    vertices, edge = map(int, input().split())
    foo(vertices+1)

    g, c = get_undirected_weighted_graph(vertices, edge)

    src, des = map(int, input().split())
    IDS(graph=g, costs=c, source=src, destination=des, max_limit=500)

