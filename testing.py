import unittest
from main import State, terminal, player, actions

class TestTerminal(unittest.TestCase):
    def test_diagonal1(self):
        self.assertTrue(terminal(State([['X', '#', '#'],['#', 'X', '#'],['#', '#', 'X']])))
        self.assertTrue(terminal(State([['O', '#', '#'],['#', 'O', '#'],['#', '#', 'O']])))
    
    def test_diagonal2(self):
        self.assertTrue(terminal(State([['#', '#', 'X'],['#', 'X', '#'],['X', '#', '#']])))
        self.assertTrue(terminal(State([['#', '#', 'O'],['#', 'O', '#'],['O', '#', '#']])))
    
    def test_firstColumn(self):
        self.assertTrue(terminal(State([['X', '#', '#'],['X', '#', '#'],['X', '#', '#']])))
        self.assertTrue(terminal(State([['O', '#', '#'],['O', '#', '#'],['O', '#', '#']])))

    def test_secondColumn(self):
        self.assertTrue(terminal(State([['#', 'X', '#'],['#', 'X', '#'],['#', 'X', '#']])))
        self.assertTrue(terminal(State([['#', 'O', '#'],['#', 'O', '#'],['#', 'O', '#']])))

    def test_thirdColumn(self):
        self.assertTrue(terminal(State([['#', '#', 'X'],['#', '#', 'X'],['#', '#', 'X']])))
        self.assertTrue(terminal(State([['#', '#', 'O'],['#', '#', 'O'],['#', '#', 'O']])))
    
    def test_firstRow(self):
        self.assertTrue(terminal(State([['X', 'X', 'X'],['#', '#', '#'],['#', '#', '#']])))
        self.assertTrue(terminal(State([['O', 'O', 'O'],['#', '#', '#'],['#', '#', '#']])))
    
    def test_secondRow(self):
        self.assertTrue(terminal(State([['#', '#', '#'],['X', 'X', 'X'],['#', '#', '#']])))
        self.assertTrue(terminal(State([['#', '#', '#'],['O', 'O', 'O'],['#', '#', '#']])))

    def test_thirdRow(self):
        self.assertTrue(terminal(State([['#', '#', '#'],['#', '#', '#'],['X', 'X', 'X']])))
        self.assertTrue(terminal(State([['#', '#', '#'],['#', '#', '#'],['O', 'O', 'O']])))

    def test_equalBoards(self):
        self.assertFalse(terminal(State([['X', 'O', 'X'], ['O', 'X', 'X'], ['O', 'X', 'O']])))
        self.assertFalse(terminal(State([['O', 'X', 'O'], ['X', 'X', 'O'], ['X', 'O', 'X']])))
        self.assertFalse(terminal(State([['X', 'O', 'O'], ['O', 'X', 'X'], ['X', 'X', 'O']])))
        self.assertFalse(terminal(State([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']])))
        self.assertFalse(terminal(State([['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']])))
class TestPlayer(unittest.TestCase):
    def test_player_true1(self):
        self.assertTrue(player(State([['X', 'O', '#'],['#', 'X', '#'],['#', 'X', 'O']])) ==  'O')
    
    def test_player_true2(self):
        self.assertTrue(player(State([['O', 'X', '#'],['X', 'O', 'O'],['#', 'X', 'X']])) == 'O')
    
    def test_player_true3(self):
        self.assertTrue(player(State([['X', '#', '#'], ['#', '#', '#'], ['#', '#', '#']])) == 'O')

    def test_player_true4(self):
        self.assertTrue(player(State([['#', 'X', '#'], ['#', '#', '#'], ['#', '#', '#']])) == 'O')

    def test_player_true5(self):
        self.assertTrue(player(State([['#', '#', 'X'], ['#', '#', '#'], ['#', '#', '#']])) == 'O')

    def test_player_true6(self):
        self.assertTrue(player(State([['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']])) == 'X')
    
    def test_player_false1(self):
        self.assertFalse(player(State([['X', 'O', 'X'], ['#', '#', 'X'], ['O', 'X', 'O']])) == 'X')

    def test_player_false2(self):
        self.assertFalse(player(State([['O', 'X', 'O'], ['#', 'X', 'O'], ['X', 'O', 'X']])) == 'O')

class TestActions(unittest.TestCase):
    def test_actions_empty_board(self):
        state = State()
        expected_actions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        self.assertEqual(actions(state), expected_actions)

    def test_actions_some_moves_made(self):
        state = State([['#', '#', 'X'], ['#', 'O', '#'], ['O', '#', 'X']])
        expected_actions = [(0, 0), (0, 1), (1, 0), (1, 2), (2, 1)]
        self.assertEqual(actions(state), expected_actions)

    def test_actions_full_board(self):
        state = State([['X', 'O', 'X'], ['O', 'X', 'O'], ['X', 'X', 'O']])
        expected_actions = []
        self.assertEqual(actions(state), expected_actions)
    
    def test_actions_alternating_moves(self):
        state = State([['X', '#', 'O'], ['#', 'X', '#'], ['#', 'O', 'X']])
        expected_actions = [(0, 1), (1, 0), (1, 2), (2, 0)]
        self.assertEqual(actions(state), expected_actions)

    def test_actions_almost_full_board(self):
        state = State([['X', 'O', 'X'], ['O', 'X', 'O'], ['X', '#', 'O']])
        expected_actions = [(2, 1)]
        self.assertEqual(actions(state), expected_actions)
if __name__ == '__main__':
    unittest.main()
