import copy


class Board:
    def __init__(self, tiles_orientation, level, parent, value_of_f_function):
        self.data = tiles_orientation
        self.level = level
        self.parent = parent
        self.f = value_of_f_function

    def generate_child_nodes(self):
        x, y = find(self.data, 'X')

        new_tile_positions = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in new_tile_positions:
            child = self.move_tile(x, y, i[0], i[1])

            if child:
                child_node = Board(child, self.level + 1, self, 0)
                children.append(child_node)

        return children

    def move_tile(self, x1, y1, x2, y2):
        if 0 <= x2 < len(self.data) and 0 <= y2 < len(self.data):
            temp_puz = copy.deepcopy(self.data)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def __str__(self):
        s = ''

        for i in self.data:
            for j in i:
                s += f'{j} '
            s += '\n'

        return s


def find(matrix, x):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if matrix[i][j] == x:
                return i, j


def enter_matrix(n):
    matrix = []
    for i in range(0, n):
        temp = input().split(' ')
        matrix.append(temp)
    return matrix


def f_function(start, goal):
    return h_function(start.data, goal) + start.level


def h_function(start, goal):
    temp = 0
    for i in range(0, len(start)):
        for j in range(0, len(start)):
            if start[i][j] != 'X':
                x, y = find(goal, start[i][j])
                temp += (abs(x - i) + abs(y - j))

    return temp


def a_star_search(initial_state, goal_state):
    initial_state = Board(
        tiles_orientation=initial_state,
        level=0,
        parent=None,
        value_of_f_function=0
    )
    initial_state.f = f_function(initial_state, goal_state)

    q = [initial_state]

    memoization = {}

    last = initial_state

    while True:
        current = q[0]

        del q[0]

        if memoization.get(str(current.data)) is not None:
            continue

        last = current

        memoization[str(current.data)] = True

        if h_function(current.data, goal_state) == 0:
            break

        for i in current.generate_child_nodes():
            i.f = f_function(i, goal_state)
            q.append(i)

        q.sort(key=lambda x: x.f_function, reverse=False)

    path = [last]

    while last.parent is not None:
        last = last.parent
        path.append(last)

    path.reverse()

    for c, i in enumerate(path):
        print(f'step #{c + 1}')
        print(i)


if __name__ == '__main__':
    print('Initial:')
    start = enter_matrix(3)

    print('Goal:')
    goal = enter_matrix(3)

    a_star_search(start, goal)
