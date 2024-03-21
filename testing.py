import unittest
from main import State, terminal

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

if __name__ == '__main__':
    unittest.main()
