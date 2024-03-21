import copy
class State():
    def __init__(self, state=[['#', '#', '#'],['#', '#', '#'],['#', '#', '#']]):
        self.state = state
    def __str__(self) -> str:
        return f"{self.state[0]}\n{self.state[1]}\n{self.state[2]}"

def actions(state: State):
    moves = []
    for i in range(3):
        for j in range(3):
            if (state.state[i][j] == '#'):
                moves.append((i,j))
    return moves

def player(state: State):
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if state.state[i][j] == 'X':
                x += 1
            elif state.state[i][j] == 'O':
                o += 1
    return 'X' if x == o else 'O'

def result (state: State, move: tuple[int, int, str]):
    board = copy.deepcopy(state.state)
    board[move[0]][move[1]] = move[2]
    return State(board)

def terminal(state: State):
    board = copy.deepcopy(state.state)
    for i in range(3):
        if (len(list(filter((lambda x: x == 'X'), board[i]))) == 3) or (len(list(filter((lambda x : x == 'O'), board[i]))) == 3):
            return True
        elif board[0][i] == board[1][i] == board[2][i] == 'X' or board[0][i] == board[1][i] == board[2][i] == 'O':
            return True
    if (board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'O') or (board[2][0] == board[1][1] == board[0][2] == 'X' or board[2][0] == board[1][1] == board[0][2] == 'O'):
        return True
    if len(actions(state)) == 0:
        return True
    return False

def score(state: State):
    board = copy.deepcopy(state.state)
    for i in range(3):
        if (len(list(filter((lambda x: x == 'X'), board[i]))) == 3):
            return 1
        elif (len(list(filter((lambda x: x == 'O'), board[i]))) == 3):
            return -1
        elif board[0][i] == board[1][i] == board[2][i] == 'X':
            return 1
        elif board[0][i] == board[1][i] == board[2][i] == 'O':
            return -1
    if (board[0][0] == board[1][1] == board[2][2] == 'X') or (board[2][0] == board[1][1] == board[0][2] == 'X'):
        return 1
    elif (board[0][0] == board[1][1] == board[2][2] == 'O') or (board[2][0] == board[1][1] == board[0][2] == 'O'):
        return -1
    else:
        return 0

def maxValue(state: State, alpha=-float('inf'), beta=float('inf')):
    if terminal(state):
        return score(state)
    v = -float('inf')
    #l = len(actions(state))
    for a in actions(state):
        v = max(v, minValue(result(state, a + ('X',)), alpha, beta))
        if v >= beta:
            break
        alpha= max(alpha, v)
    return v

def minValue(state: State, alpha=-float('inf'), beta=float('inf')):
    if terminal(state):
        return score(state)
    v = float('inf')
    #l = len(actions(state))
    for a in actions(state):
        v = min(v,maxValue(result(state, a + ('O',)), alpha, beta))
        if v <= alpha:
            break
        beta = max(beta, v)
    return v

def AI(state: State):
    a = actions(state)
    mini = float('inf')
    best = None
    for action in a:
        maxv = maxValue(result(state, action + ('O',)))
        if maxv < mini:
            mini = maxv
            best = action
    return result(state, best + ('O',))

if __name__ == '__main__':
    s0 = State([['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']])
    state = s0
    print(state)
    while True:
        print("Player Turn")
        row = int(input("Row: "))
        col = int(input("Col: "))
        state = result(state, (row, col, 'X'))
        if terminal(state):
            print("Player Winns") if score(state) == 1 else print("Tie!")
            break
        print(state)
        print("AI Turn:")
        state = AI(state)
        print(state)
        if terminal(state):
            print("AI Winns") if score(state) == -1 else print("Tie!")
            break


    #print(result(s0, best + ('O',)))