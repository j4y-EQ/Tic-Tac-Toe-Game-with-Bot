import os
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

bot_symbol = ""
bot_name = ""
player1_name = ""
player1_symbol = ""

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
        if 0 <= move <= 2:
            if board[0][move] == '.':
                return True
        elif 3 <= move <= 5:
            if board[1][move - 3] == '.':
                return True
        elif 6 <= move <= 8:
            if board[2][move - 6] == '.':
                return True
        return False

    def check_win(self):
        for case in win_cases:
            for coor in case:
                check = True
                if board[coor[0]][coor[1]] != self.player_symbol:
                    check = False
                    break
            if check is True:
                return check
        return check

    def player_input(self):
        while True:
            move = int(input(f'{self.player_name}\'s input: '))
            if self.can_move(move):
                if 0 <= move <= 2:
                    board[0][move] = self.player_symbol
                    break
                elif 3 <= move <= 5:
                    board[1][move - 3] = self.player_symbol
                    break

                elif 6 <= move <= 8:
                    board[2][move - 6] = self.player_symbol
                    break

            else:
                print('Invalid Input, try again!!')


class Bot:
    def __init__(self, bot_name, bot_symbol):
        self.bot_name = bot_name
        self.bot_symbol = bot_symbol

    def can_move(self, move):
        if 0 <= move <= 2:
            if board[0][move] == '.':
                return True
        elif 3 <= move <= 5:
            if board[1][move - 3] == '.':
                return True
        elif 6 <= move <= 8:
            if board[2][move - 6] == '.':
                return True
        return False

    def check_win(self, num):
        if num == 0:
            for case in win_cases:
                for coor in case:
                    check = True
                    if board[coor[0]][coor[1]] != self.bot_symbol:
                        check = False
                        break
                if check is True:
                    return check
            return check
        elif num == 1:
            for case in win_cases:
                for coor in case:
                    check = True
                    if board[coor[0]][coor[1]] != player1_symbol:
                        check = False
                        break
                if check is True:
                    return check
            return check

    def bot_move(self):
        for move in range(9):
            if self.can_move(move):
                if 0 <= move <= 2:
                    board[0][move] = self.bot_symbol
                elif 3 <= move <= 5:
                    board[1][move - 3] = self.bot_symbol
                elif 6 <= move <= 8:
                    board[2][move - 6] = self.bot_symbol

                win = self.check_win(0)
                if not win:
                    if 0 <= move <= 2:
                        board[0][move] = "."
                    elif 3 <= move <= 5:
                        board[1][move - 3] = "."
                    elif 6 <= move <= 8:
                        board[2][move - 6] = "."
                else:
                    return
        # #attacc
        for move in range(9):
            if self.can_move(move):
                if 0 <= move <= 2:
                    board[0][move] = player1_symbol
                elif 3 <= move <= 5:
                    board[1][move - 3] = player1_symbol
                elif 6 <= move <= 8:
                    board[2][move - 6] = player1_symbol

                win = self.check_win(1)
                if win:
                    if 0 <= move <= 2:
                        board[0][move] = self.bot_symbol
                        return
                    elif 3 <= move <= 5:
                        board[1][move - 3] = self.bot_symbol
                        return
                    elif 6 <= move <= 8:
                        board[2][move - 6] = self.bot_symbol
                        return
                else:
                    if 0 <= move <= 2:
                        board[0][move] = "."
                    elif 3 <= move <= 5:
                        board[1][move - 3] = "."
                    elif 6 <= move <= 8:
                        board[2][move - 6] = "."

        while True:
            move = randint(0, 8)
            if self.can_move(move):
                if 0 <= move <= 2:
                    board[0][move] = self.bot_symbol
                    break
                elif 3 <= move <= 5:
                    board[1][move - 3] = self.bot_symbol
                    break
                elif 6 <= move <= 8:
                    board[2][move - 6] = self.bot_symbol
                    break
            else:
                return


def check_done():
    for row in board:
        for num in row:
            if num == ".":
                return False
    return True


def print_refs():
    os.system("cls")
    print('Demo puzzle for location reference')
    for i in range(3):
        print(*demo[i], sep=' ')
    print('\n')
    print('XOX Puzzle')
    for i in range(3):
        print(*board[i], sep=' ')
    print('\n\n')


# START
while True:
    choice = input("Hello! Would you like to play against a player or a bot: ")
    if choice.upper() == 'BOT':
        break
    elif choice.upper() == 'PLAYER':
        break
if choice.upper() == "PLAYER":
    player1_name = input("What is player1's name?")
    player1_symbol = input("What is your symbol? 'X' or 'O'").upper()

    # check if user_input is "x" or "o"
    while True:
        if player1_symbol == "O":
            break
        if player1_symbol == "X":
            break
        player1_symbol = input("What is your symbol? 'X' or 'O'").upper()
        # print(player1_symbol)

    player1 = TikTakToe(player1_name, player1_symbol)
    player2_name = input("What is player2's name?")
    if player1_symbol == 'X':
        player2_symbol = 'O'
        print(f"{player2_name} you shall be {player2_symbol}.")
    else:
        player2_symbol = 'X'
        print(f"{player2_name} you shall be {player2_symbol}.")

    player2 = TikTakToe(player2_name, player2_symbol)

    print("GAME STARTED")
    print('Demo puzzle for location reference')
    for i in range(3):
        print(*demo[i], sep=' ')
    print('\n')
    print('XOX Puzzle')
    for i in range(3):
        print(*board[i], sep=' ')
    print('\n\n')

    turn = 0
    while turn < 9:

        if turn == 9:
            break
        player1.player_input()
        print_refs()
        turn += 1
        if player1.check_win():
            print(f"{player1.player_name} wins!")
            break

        player2.player_input()
        print_refs()
        turn += 1
        if player2.check_win():
            print(f"{player2.player_name} wins!")
            break
        # print(turn)
    else:
        print("Nobody won.")

elif choice.upper() == "BOT":
    player1_name = input("What is player1's name?")
    player1_symbol = input("What is your symbol? 'X' or 'O'").upper()

    # check if user_input is "x" or "o"
    while True:
        if player1_symbol == "O":
            break
        if player1_symbol == "X":
            break
        player1_symbol = input("What is your symbol? 'X' or 'O'").upper()
        # print(player1_symbol)

    player1 = TikTakToe(player1_name, player1_symbol)
    bot_name = input("What is the bot's name: ")
    if player1_symbol == 'X':
        bot_symbol = 'O'
    else:
        bot_symbol = 'X'
    print(f"{bot_name} shall be {bot_symbol}.")

    bot = Bot(bot_name, bot_symbol)

    for i in range(3):
        print(*demo[i], sep=' ')
    print('\n')
    print('XOX Puzzle')
    for i in range(3):
        print(*board[i], sep=' ')
    print('\n\n')
    while True:
        if not check_done():
            player1.player_input()
            print_refs()
            if player1.check_win():
                print(f"{player1.player_name} wins!")
                break

            bot.bot_move()

            print_refs()
            if bot.check_win(0):
                print(f"{bot_name} wins!")
                break

        else:
            print("Nobody won.")
            break
