import sys
import os


def get_player_input():
    return (list(map(int, input().split())))


def Brett_Malen(brett):
    for r in brett:
        for c in r:
            print(c, end=" ")
        print()


def game_mechanic(player_input, playerwho, spielbeginn):
    move_x = player_input[0]
    move_y = player_input[1]
    try:
        if spielbeginn[move_x - 1][move_y - 1] == 'X' or spielbeginn[move_x - 1][move_y - 1] == 'O':
            print("\nDon't try to override your opponents move. Pretty sus...\n")
            playerwho -= 1
            return playerwho
        else:
            if playerwho % 2 == 0 and spielbeginn:
                spielbeginn[move_x - 1][move_y - 1] = 'X'
            else:
                spielbeginn[move_x - 1][move_y - 1] = 'O'
    except IndexError:
        print("\nOut of bounds. Please enter correct coordinates.\n ")
        playerwho -= 1
        return playerwho


def checkWin(spielbeginn):
    player1 = False
    player2 = False
    tie = False

    if spielbeginn[0][0] == 'X' and spielbeginn[0][1] == 'X' and spielbeginn[0][2] == 'X' or spielbeginn[1][
        0] == 'X' and spielbeginn[1][1] == 'X' and spielbeginn[1][2] == 'X' or spielbeginn[2][0] == 'X' and \
            spielbeginn[2][1] == 'X' and spielbeginn[2][2] == 'X' or spielbeginn[0][0] == 'X' and spielbeginn[1][
        0] == 'X' and spielbeginn[2][0] == 'X' or spielbeginn[0][1] == 'X' and spielbeginn[1][1] == 'X' and \
            spielbeginn[2][1] == 'X' or spielbeginn[0][2] == 'X' and spielbeginn[1][2] == 'X' and spielbeginn[2][
        2] == 'X' or spielbeginn[0][0] == 'X' and spielbeginn[1][1] == 'X' and spielbeginn[2][2] == 'X' or \
            spielbeginn[0][2] == 'X' and spielbeginn[1][1] == 'X' and spielbeginn[2][0] == 'X':
        player1 = True
    elif spielbeginn[0][0] == 'O' and spielbeginn[0][1] == 'O' and spielbeginn[0][2] == 'O' or spielbeginn[1][
        0] == 'O' and spielbeginn[1][1] == 'O' and spielbeginn[1][2] == 'O' or spielbeginn[2][0] == 'O' and \
            spielbeginn[2][1] == 'O' and spielbeginn[2][2] == 'O' or spielbeginn[0][0] == 'O' and spielbeginn[1][
        0] == 'O' and spielbeginn[2][0] == 'O' or spielbeginn[0][1] == 'O' and spielbeginn[1][1] == 'O' and \
            spielbeginn[2][1] == 'O' or spielbeginn[0][2] == 'O' and spielbeginn[1][2] == 'O' and spielbeginn[2][
        2] == 'O' or spielbeginn[0][0] == 'O' and spielbeginn[1][1] == 'O' and spielbeginn[2][2] == 'O' or \
            spielbeginn[0][2] == 'O' and spielbeginn[1][1] == 'O' and spielbeginn[2][0] == 'O':
        player2 = True
    elif spielbeginn[0][0] != '-' and spielbeginn[0][1] != '-' and spielbeginn[0][2] != '-' and spielbeginn[1][
        0] != '-' and spielbeginn[1][1] != '-' and spielbeginn[1][2] != '-' and spielbeginn[2][0] != '-' and \
            spielbeginn[2][1] != '-' and spielbeginn[2][2] != '-':
        tie = True

    if player1 == True:
        return "Player1"
    elif player2 == True:
        return "Player2"
    elif tie == True:
        return "Tie"


print("Tic Tac Toe")
print("v.1")
print("\nThis is a console game")
print("of tic-tac-toe game. Based on python.")
print("\nUse coordinates to enter your Tic or Tac.")
print("Player1(X) and Player2(O)\n")

spielbeginn = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-'],
]
Brett_Malen(spielbeginn)
player = 0
try:
    while True:
        if player % 2 == 0:
            print("Please enter your coordinates, Player1(X): ")
        else:
            print("Please enter your coordinates, Player2(O): ")

        while True:
            try:
                player_input = get_player_input()
                if player_input[0] < 1 or player_input[0] > 3 and player_input[1] < 1 or player_input[1] > 3:
                    pass
            except (IndexError, ValueError):
                print("\nDid you enter correctly? \n")
            else:
                break
        play = game_mechanic(player_input, player, spielbeginn)
        if play == player - 1:
            player -= 1
        Brett_Malen(spielbeginn)
        condition = checkWin(spielbeginn)
        if condition:
            break
        else:
            player += 1

    if condition == "Player1":
        print(f"Congrats, {condition}")
    elif condition == "Player2":
        print(f"Congrats, {condition}")
    else:
        print(f"It is a tie. Game over!")
except KeyboardInterrupt:
    print("Game has been ended by the user prematurely.")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
