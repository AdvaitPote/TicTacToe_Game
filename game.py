from bot import Bot
from board import Board

def start_game():
    board = Board()
    return board

def human_turn(board, turn):
    row = -1
    col = -1
    moves = {
        tuple([0, 0]): 1, tuple([0, 1]): 2, tuple([0, 2]): 3,
        tuple([1, 0]): 4, tuple([1, 1]): 5, tuple([1, 2]): 6,
        tuple([2, 0]): 7, tuple([2, 1]): 8, tuple([2, 2]): 9,
    }
    board.print()
    while (tuple([row, col]) not in list(moves)):
        try:
            row, col = input("Enter the row and column of your move: ").split()
            row = int(row)
            col = int(col)
            row -= 1
            col -= 1
            if board.is_legal(row, col):
                board.make_move(row, col, turn)
            else:
                print("Move not possible as provided coordinates lie outside the grid or already occupied")
                row = -1
                col = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')
    return 

def main():
    board = start_game()

    human_choice = ''
    bot_choice = ''
    while human_choice != 'X' and human_choice != 'O':
        human_choice = input('Choose X or O: ').upper()
        
    if human_choice == 'X':
        bot_choice = 'O'
        first = "human"

    else:
        bot_choice = 'X'
        first = "bot"

    bot = Bot(bot_choice)

    while (len(board.moves) < 9 and not board.game_over()):
        while first != "bot":
            human_turn(board, human_choice)
            # print(board.num_possible_moves)
            first = "bot"
        
        bot.select_move(board)
        if board.is_winner(bot_choice) or len(board.moves) == 9:
            break
        # print(board.num_possible_moves)
        human_turn(board, human_choice)
        # print(board.num_possible_moves)
        # print(board.moves)

    board.print()

    if board.is_winner("X"):
        print("X wins")
    elif board.is_winner("O"):
        print("O wins")
    else:
        print("DRAW")
    return

if __name__ == '__main__':
    main()
    
    


