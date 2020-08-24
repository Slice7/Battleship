from random import randint
from numpy import linalg
from os import system
from time import sleep


# Choose ship's row
def random_row(grid):
    return randint(0, len(grid) - 2)


# Choose ship's column
def random_col(grid):
    return randint(1, len(grid[0]) - 1)


# Print board
def print_board(grid):
    for row in grid:
        print(" ".join(row))


query = '''while True:
            try:
                guess_x, guess_y = map(int, input("Guess the coordinates x, y: ").split(','))
                while guess_x not in [1, 2, 3, 4, 5] or 5 - guess_y not in range(5):
                    print("Enter a pair of numbers between 1 and 5!")
                    guess_x, guess_y = map(int, input("Guess the coordinates x, y: ").split(','))
                break
            except ValueError:
                print("Enter a pair of numbers between 1 and 5!")'''

while True:

    # Create board
    board = []

    for a in range(5):
        board.append(["~"] * 5)

    for rows in board:
        rows.insert(0, str(5 - board.index(rows)))

    board.append(["0", "1", "2", "3", "4", "5"])

    # Place ship
    shipRow = random_row(board)
    shipCol = random_col(board)

    tries = 5

    print("\nTries remaining: {}".format(tries))
    print_board(board)
    print("")

    for i in range(tries):
        print("")
        exec(query)
        if 5 - guess_y == shipRow and guess_x == shipCol:
            if i == 0:
                if not randint(0, 3):
                    print("\nCongratulations! You got it on your first try!\nAre you cheating?\n")
                else:
                    print("\nCongratulations! You got it on your first try!\n")
            else:
                print("\nCongratulations! You sank my battleship!\n")

            board[shipRow][shipCol] = 'S'
            print_board(board)
            break

        else:
            while board[5 - guess_y][guess_x] == 'X':
                print("\nYou guessed that one already.\n")
                exec(query)
            else:
                tries -= 1
                if i == 0:
                    print("\nYou missed my battleship!")
                    bestGuess = True
                else:
                    if i == 4:
                        print("\nThat was your last try!")
                        print("\nGame Over!")
                        board[shipRow][shipCol] = 'S'
                        bestGuess = False
                    elif linalg.norm([shipRow - 5 + guess_y, shipCol - guess_x]) \
                            < linalg.norm([shipRow - 5 + bestGuess_y, shipCol - bestGuess_x]):
                        print("\nThat's your best guess!")
                        bestGuess = True
                    elif linalg.norm([shipRow - 5 + guess_y, shipCol - guess_x]) \
                            > linalg.norm([shipRow - 5 + bestGuess_y, shipCol - bestGuess_x]):
                        print("\nThat's not your best guess!")
                        bestGuess = False
                    else:
                        print("\nThat's tied for best guess!")
                        bestGuess = False

                if bestGuess:
                    bestGuess_x, bestGuess_y = guess_x, guess_y

                board[5 - guess_y][guess_x] = 'X'

        if i == 3:
            print("\nLast try!")
        elif 0 <= i < 3:
            print("\nTries remaining:", tries)
        print_board(board)

    # Play again?
    while True:
        answer = input("\nPlay again? (y/n): ")
        if answer.lower() in ("y", "n"):
            break
        print("Invalid input.")

    if answer.lower() == "y":
        print("\nStarting new game...")
        sleep(1.3)
        system('cls')
        continue

    else:
        break
