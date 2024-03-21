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
    board = state.state
    board[move[0]][move[1]] = move[2]
    return State(board)

def terminal(state: State):
    board = state.state
    for i in range(3):
        if (len(list(filter((lambda x: x == 'X'), board[i]))) == 3) or (len(list(filter((lambda x : x == 'O'), board[i]))) == 3):
            return True
        elif board[0][i] == board[1][i] == board[2][i] == 'X' or board[0][i] == board[1][i] == board[2][i] == 'O':
            return True
    if (board[0][0] == board[1][1] == board[2][2] == 'X' or board[0][0] == board[1][1] == board[2][2] == 'O') or (board[2][0] == board[1][1] == board[0][2] == 'X' or board[2][0] == board[1][1] == board[0][2] == 'O'):
        return True
    return False

if __name__ == '__main__':
    s0 = State()