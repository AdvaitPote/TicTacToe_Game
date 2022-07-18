import copy
from fcntl import FD_CLOEXEC

class Board():
    def __init__(self):
        self.dimension = 3
        self.grid = [["-" for j in range(self.dimension)] for i in range(self.dimension)]
        self.moves = []
    
    def print(self):
        for row in range(self.dimension):
            for col in range(self.dimension):
                print(self.grid[row][col], end=" ")
            print("\n")
            
    def is_legal(self, row, col):
        if (self.grid[row][col]=="-"):
            return True
        return False

    def num_possible_moves(self):
        num_moves = 0
        for rows in range(self.dimension):
            for cols in range(self.dimension):
                if self.is_legal(rows, cols):
                    num_moves += 1
        return num_moves

    def possible_moves(self):
        moves = []
        for rows in range(self.dimension):
            for cols in range(self.dimension):
                if self.is_legal(rows, cols):
                    moves.append([rows, cols])
        return moves

    def make_move(self, row, col, player):
        self.grid[row][col] = player
        self.moves.append([row, col])
        return

    def is_winner(self, player):
        # checking rows
        for row in range(self.dimension):
            if len(set(self.grid[row])) == 1:
                element = set(self.grid[row]).pop()
                if element == player:
                    # set(self.grid[row]).add(player)
                    return True
                elif element == "-":
                    # set(self.grid[row]).add("-")
                    return False
        
        # checking columns
        for cols in range(self.dimension):
            unique_values = set()
            for row in range(self.dimension):
                unique_values.add(self.grid[row][cols])
            if len(unique_values) == 1:
                element = unique_values.pop()
                if element == player:
                    # unique_values.add(player)
                    return True
                elif element == "-":
                    # unique_values.add("-")
                    return False

        # checking diagonals
        forward_diag = set()
        for row in range(self.dimension):
            forward_diag.add(self.grid[self.dimension-row-1][row])
        if len(forward_diag) == 1:
            element = forward_diag.pop()
            if element == player:
                # forward_diag.add(player)
                return True
            elif element == "-":
                # forward_diag.add("-")
                return False

        backward_diag = set()
        for row in range(self.dimension):
            backward_diag.add(self.grid[row][row])
        if len(backward_diag) == 1:
            element = backward_diag.pop()
            if element == player:
                # backward_diag.add(player)
                return True
            elif element == "-":
                # backward_diag.add("-")
                return False

        return False

    def game_over(self):
        return len(self.moves) == 9 or self.is_winner('X') or self.is_winner('O')

    def __deepcopy__(self, memodict={}):
        dp = Board()
        dp.grid = copy.deepcopy(self.grid) 
        dp.moves = copy.deepcopy(self.moves)
        return dp  
    
        

        