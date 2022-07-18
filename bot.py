from cmath import inf
import random
from shutil import move
from board import Board
import copy

class Choice():
    def __init__(self, move, value, depth):
        self.move = move
        self.value = value
        self.depth = depth
    
    def __str__(self):
        return (str(self.move) + ": " + str(self.value))

class Bot():
    def __init__(self, turn):
        self.turn = turn
        if turn == 'X':
            self.complement = 'O'
        else:
            self.complement = 'X'

    def minimax(self, board, is_max, player, depth):

        complement = ''
        if (player=='X'):
            complement = 'O'
        else:
            complement = 'X'

        if board.is_winner(self.turn):
            return Choice(board.moves[-1], 1, depth)
        elif board.is_winner(self.complement):
            return Choice(board.moves[-1], -1, depth)
        elif len(board.moves) == 9:
            return Choice(board.moves[-1], 0, depth)

        possible_choices = []
        possible_moves = board.possible_moves()
        for i in range(len(possible_moves)):
            row = possible_moves[i][0]
            col = possible_moves[i][1]
            newboard = copy.deepcopy(board)
            newboard.make_move(row, col, player)
            result = self.minimax(newboard, not is_max, complement, depth - 1)
            result.move = [row, col]
            possible_choices.append(result)

        max_choice = None
        max_value = -100
        min_choice = None
        min_value = 100

        for i in range(len(possible_choices)):
            choice = possible_choices[i]
            if (is_max and choice.value > max_value):
                max_choice = choice
                max_value = choice.value
            elif (not is_max and choice.value < min_value):
                min_choice = choice
                min_value = choice.value
        
        if is_max:
            return max_choice
        else:
            return min_choice

        # if player == self.turn:
        #     best = [-1, -1, -inf]
        # else:
        #     best = [-1, -1, +inf] 

        # if player == 'X':
        #     complement = 'O'
        # else:
        #     complement = 'X'

        # if depth == 0 or board.game_over:
        #     if board.is_winner(self.turn):
        #         score = 1
        #         return [-1, -1, 1]
        #     elif board.is_winner(self.complement):
        #         score = -1
        #         return [-1, -1, -1]
        #     elif len(board.possible_moves()) == 0:
        #         score = 0
        #         return [-1, -1, 0]

        # for cell in board.possible_moves():
        #     x, y = cell[0], cell[1]
        #     # board.grid[x][y] = player
        #     # board.moves.append([x, y])
        #     newboard = copy.deepcopy(board)
        #     newboard.make_move(x, y, player)
        #     score = self.minimax(newboard, complement, depth - 1)
        #     # board.grid[x][y] = '-'
        #     # board.moves.remove([x, y])
        #     score[0], score[1] = x, y

        #     if player == self.turn:
        #         if score[2] > best[2]:
        #             best = score  # max value
        #     else:
        #         if score[2] < best[2]:
        #             best = score  # min value

        # return best


    def select_move(self, board):
        depth = len(board.possible_moves()) 
        if depth == 0 or board.game_over():
            return
        candidates = board.possible_moves()
        # move = random.choice(candidates)
        if len(board.possible_moves())!=9:
            choice = self.minimax(board, True, self.turn, 0)
            # print(choice)
            board.make_move(choice.move[0], choice.move[1], self.turn)
        else:
            choice = Choice([random.choice([0, 1, 2]), random.choice([0, 1, 2])], None, None)
            board.make_move(choice.move[0], choice.move[1], self.turn)
        # board.make_move(move[0], move[1], self.turn)
        return