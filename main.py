import random
print("Welcome to Tic Tac Toe Game")
print("---------------------------")

possible_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

rows = 3
cols = 3

def print_game_board():
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", game_board[x][y], end=" |")
    print("\n+---+---+---+")

def modify_array(num, turn):
    num -= 1
    game_board[num // 3][num % 3] = turn

def check_winner(brd):
    lines = [
        # rows
        [brd[0][0], brd[0][1], brd[0][2]],
        [brd[1][0], brd[1][1], brd[1][2]],
        [brd[2][0], brd[2][1], brd[2][2]],
        # cols
        [brd[0][0], brd[1][0], brd[2][0]],
        [brd[0][1], brd[1][1], brd[2][1]],
        [brd[0][2], brd[1][2], brd[2][2]],
        # diagonals
        [brd[0][0], brd[1][1], brd[2][2]],
        [brd[0][2], brd[1][1], brd[2][0]]
    ]
    for line in lines:
        if line == ["X", "X", "X"]:
            print("X has won")
            return "X"
        if line == ["O", "O", "O"]:
            print("O has won")
            return "O"
    return None

leave_loop = False
turn_counter = 0

while not leave_loop:
    # Player turn
    if turn_counter % 2 == 0:
        print_game_board()
        try:
            number_picked = int(input("\nChoose a number [1-9]: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if number_picked not in possible_numbers:
            print("Invalid input. Please try again.")
            continue
        modify_array(number_picked, "X")
        possible_numbers.remove(number_picked)
        turn_counter += 1
    # Computer turn
    else:
        cpu_choice = random.choice(possible_numbers)
        print("\nCpu Choice:", cpu_choice)
        modify_array(cpu_choice, "O")
        possible_numbers.remove(cpu_choice)
        turn_counter += 1

    winner = check_winner(game_board)
    if winner or not possible_numbers:
        print_game_board()
        if not winner:
            print("It's a draw!")
        leave_loop = True