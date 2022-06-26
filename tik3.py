from random import randint

tab = [num for num in range(10)]
demo = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

win_cases = [
    # Coordinates, (index row, index in row)
    # Vertical Cases
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    # Horizontal Cases
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    # Diagonal Cases
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]

]


class TikTakToe:
    def __init__(self, player_name="", player_symbol=""):
        self.player_name = player_name
        self.player_symbol = player_symbol

    def can_move(self, move):
        first_num = 0
        last_num = 2
        i = 0
        j = 0
        for _ in range(3):
            if first_num <= move <= last_num:
                if board[i][move - j] == '.':
                    return True
            j += 3
            first_num += 3
            last_num += 3
            i += 1

    def check_win(self, symbol):
        for case in win_cases:
            for coor in case:
                win = True
                if board[coor[0]][coor[1]] != symbol:
                    win = False
                    break
            if win is True:
                return win

    def player_input(self):
        while True:
            move = int(input(f'{self.player_name}\'s input: '))
            if self.can_move(move):
                self.movement(move, self.player_symbol)
                break
            else:
                print('Invalid input. Try again!')

    def movement(self, move, symbol):
        first_num = 0
        last_num = 2
        i = 0
        j = 0
        for _ in range(3):
            if first_num <= move <= last_num:
                board[i][move - j] = symbol
                return
            j += 3
            first_num += 3
            last_num += 3
            i += 1

    def remove_movement(self, move):
        first_num = 0
        last_num = 2
        i = 0
        j = 0
        for _ in range(3):
            if first_num <= move <= last_num:
                board[i][move - j] = "."
                return
            j += 3
            first_num += 3
            last_num += 3
            i += 1

    def bot_move(self, o_symbol):
        for move in range(9):
            if self.can_move(move):
                self.movement(move, self.player_symbol)
                if not self.check_win(self.player_symbol):
                    self.remove_movement(move)
                else:
                    return

        # Defend
        for move in range(9):
            if self.can_move(move):
                self.movement(move, o_symbol)
                if self.check_win(o_symbol):
                    self.movement(move, self.player_symbol)
                    return
                else:
                    self.remove_movement(move)

        ran_move = randint(0, 9)
        if self.can_move(ran_move):
            self.movement(ran_move, self.player_symbol)
            return


def print_board():
    for i in range(3):
        print(*demo[i], sep=' ')
    print('\n')
    print('XOX Puzzle')
    for i in range(3):
        print(*board[i], sep=' ')
    print('\n\n')


turn = 0
p_name = input("What is your name: ")
while True:
    p_symbol = input("What is your symbol? \"X\" or \"O\": ").upper()
    if p_symbol != "X":
        if p_symbol != "O":
            print("Please input X or O.")
        else:
            break
    else:
        break

done = True
while done:
    choice = input("Would you like to play against a bot or a player? : ").upper()
    if choice == "BOT":
        player = TikTakToe(p_name, p_symbol)
        if p_symbol == "X":
            b_symbol = "O"
        else:
            b_symbol = "X"
        bot = TikTakToe("Bot", b_symbol)
        print_board()
        while True:
            if turn < 9:
                player.player_input()
                print_board()
                if player.check_win(player.player_symbol):
                    print(f"{p_name} wins!")
                    break
                turn += 1
            else:
                print("Oh no! Nobody won. Goodluck next time!")
                break
            if turn < 9:
                bot.bot_move(player.player_symbol)
                print_board()
                if bot.check_win(bot.player_symbol):
                    print("Bot wins!")
                    break
                turn += 1
            else:
                print("Oh no! Nobody won. Goodluck next time!")
                break
        done = False

    elif choice == "PLAYER":
        player1 = TikTakToe(p_name, p_symbol)
        p2_name = input("What is player 2's name: ")
        if p_symbol == "X":
            p2_symbol = "O"
        else:
            p2_symbol = "X"
        player2 = TikTakToe(p2_name, p2_symbol)
        turn = 0
        print_board()
        while True:
            if turn < 9:
                player1.player_input()
                print_board()
                if player1.check_win(player1.player_symbol):
                    print(f"{p_name} wins!")
                    break
                turn += 1
            else:
                print("Oh no! Nobody won. Goodluck next time!")
                break
            if turn < 9:
                player2.player_input()
                print_board()
                if player2.check_win(player2.player_symbol):
                    print(f"{p2_name} wins!")
                    break
                turn += 1
            else:
                print("Oh no! Nobody won. Goodluck next time!")
                break
        done = False
    else:
        print("Invalid input. Try again.")

