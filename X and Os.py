def createboard():
    return ["| |" for _ in range(9)]
player = "X"

def move(square, numonboard, player):
    if 0 <= numonboard < 9:
        if square[numonboard] == "| |":
            square[numonboard] = f"|{player}|"
        else:
            print("invalid block")
    else:
        print("invalid number")


def check_win(square, player):
    win_combos = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal \
        [2, 4, 6]  # Diagonal /
    ]

    for combo in win_combos:
        if all(square[i] == f"|{player}|" for i in combo):
            return True
    return False

def is_draw(square):
    return all(bruh != "| |" for bruh in square)

def printboard(square):
    for i in range(0, 9, 3):
        print(square[i], square[i+1], square[i+2])

square = createboard()
printboard(square)

while True:
    numonboard = input(f"What number do you want from 0 - 8? You are currently {player}: ")
    move(square, int(numonboard), player)
    printboard(square)
    if check_win(square, player):
        print(f"Player {player} wins!")
        break
    elif is_draw(square):
        print("It's a draw!")
        break

    player = "X" if player == "O" else "O"
