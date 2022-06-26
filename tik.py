import os

demo = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

xox = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


class TikTakToe:
    def __init__(self, player_name, player_symbol):
        self.player_name = player_name
        self.player_symbol = player_symbol

    def win_cases(self):
        # Horizontal Cases
        for i in range(3):
            if xox[i][0] == xox[i][1] == xox[i][2] == self.player_symbol:
                return True
            # Vertical Cases
            if xox[0][i] == xox[1][i] == xox[2][i] == self.player_symbol:
                return True
        # Diagonal case
        if xox[0][0] == xox[1][1] == xox[2][2] == self.player_symbol:
            return True
        if xox[2][0] == xox[1][1] == xox[0][2] == self.player_symbol:
            return True

    def player_input(self):
        x = int(input(f'{self.player_name}\'s input: '))

        if 1 <= x <= 3:
            if xox[0][x - 1] == '.':
                xox[0][x - 1] = self.player_symbol
                return True
            else:
                print("Input in another location!")
                return False
        elif 4 <= x <= 6:
            if xox[1][x - 4] == '.':
                xox[1][x - 4] = self.player_symbol
                return True
            else:
                print("Input in another location!")
                return False
        elif 7 <= x <= 9:
            if xox[2][x - 7] == '.':
                xox[2][x - 7] = self.player_symbol
                return True
            else:
                print("Input in another location!")
                return False
        else:
            print('Invalid Input, try again!!')
            return False


def print_refs():
    os.system("cls")
    print('Demo puzzle for location reference')
    for i in range(3):
        print(*demo[i], sep=' ')
    print('\n')
    print('XOX Puzzle')
    for i in range(3):
        print(*xox[i], sep=' ')
    print('\n\n')


# START


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
    print(*xox[i], sep=' ')
print('\n\n')

turn = 0
while turn < 9:
    while True:
        if turn == 9:
            break
        if player1.player_input():
            print_refs()
            turn += 1
            break
    if player1.win_cases():
        print(f"{player1.player_name} wins!")
        break
    while True:
        if turn == 9:
            break
        if player2.player_input():
            print_refs()
            turn += 1
            break
    if player2.win_cases():
        print(f"{player2.player_name} wins!")
        break
    # print(turn)
else:
    print("Nobody won.")
