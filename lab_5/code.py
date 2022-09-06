import copy

inf = 99999999

next_board = None


def search(condition, contestant):

    return max_value(condition, -inf, +inf, True) if contestant == 'max' else min_value(condition, -inf, +inf, True)


def max_value(condition, alpha, beta, first_move):
    test_terminal_state = is_terminal_condition(condition)

    if test_terminal_state['status']:
        return test_terminal_state

    global next_board

    v = {
        'status': False,
        'winner': None,
        'utility': -inf,
        'state': condition
    }

    successors = genrate_children(condition, 'max')

    for s in successors:
        rslt = min_value(s, alpha, beta, False)

        if rslt['utility'] > v['utility']:
            if first_move:
                next_board = s

            v = rslt

        if v['utility'] >= beta:
            return v

        alpha = max(alpha, v['utility'])

    return v


def min_value(condtion, alpha, beta, first_move):
    test_terminal_state = is_terminal_condition(condtion)

    if test_terminal_state['status']:
        return test_terminal_state

    global next_board

    v = {
        'status': False,
        'winner': None,
        'utility': inf,
        'state': condtion
    }

    successors = genrate_children(condtion, 'min')

    for s in successors:
        rslt = max_value(s, alpha, beta, False)

        if rslt['utility'] < v['utility']:
            if first_move:
                next_board = s

            v = rslt

        if v['utility'] <= alpha:
            return v

        beta = min(beta, v['utility'])

    return v


def genrate_children(condition, contestant):
    next_moves = []

    for i in range(len(condition)):
        for j in range(len(condition[i])):
            if condition[i][j] == '_':
                new_board = copy.deepcopy(condition)
                new_board[i][j] = 'x' if contestant == 'max' else 'o'
                next_moves.append(new_board)

    return next_moves


def is_terminal_condition(condtion):
    rslt = {
        'status': False,
        'winner': None,
        'utility': None,
        'state': condtion
    }

    for i in range(3):
        if condtion[0][i] != '_' and condtion[0][i] == condtion[1][i] == condtion[2][i]:
            rslt['status'] = True
            rslt['winner'] = condtion[0][i]
            rslt['utility'] = 1 if condtion[0][i] == 'x' else -1
            return rslt

    for i in range(3):
        if condtion[i] == ['x', 'x', 'x'] or condtion[i] == ['o', 'o', 'o']:
            rslt['status'] = True
            rslt['winner'] = condtion[0][0]
            rslt['utility'] = 1 if condtion[0][0] == 'x' else -1
            return rslt

    if condtion[0][0] != '_' and condtion[0][0] == condtion[1][1] == condtion[2][2]:
        rslt['status'] = True
        rslt['winner'] = condtion[0][0]
        rslt['utility'] = 1 if condtion[0][0] == 'x' else -1
        return rslt

    if condtion[0][2] != '_' and condtion[0][2] == condtion[1][1] == condtion[2][0]:
        rslt['status'] = True
        rslt['winner'] = condtion[0][2]
        rslt['utility'] = 1 if condtion[0][2] == 'x' else -1
        return rslt

    for i in range(3):
        for j in range(3):
            if condtion[i][j] == '_':
                return rslt

    rslt['status'] = True
    rslt['winner'] = '_'
    rslt['utility'] = 0
    return rslt


if __name__ == '__main__':

    print('Board = ')

    state = []
    for i in range(0, 3):
        temp = input().split(' ')
        state.append(temp)

    player = str(input('Player = ')).lower()

    result = search(state, player)

    if result['utility'] == 0:
        print('Draw')

    elif result['utility'] == 1:
        print('Winner is Max')

    else:
        print('Winner is Min')

    if result['utility'] != 0:
        print('Next board can be')

        for i in next_board:
            for j in i:
                print(f'{j} ', end='')
            print()