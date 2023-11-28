import numpy as np
import goal
import alpha_beta


# printing the game board
def print_board(game_board):
    # the first batch
    for i in range(4):
        print("\n")
        for j in range(4):
            print(game_board[i][j], end="  ")

    print("\n")
    # the second batch
    for i in range(4):
        print("\n")
        for j in range(4, 8):
            print(game_board[i][j], end="  ")

    print("\n")

    # the third batch
    for i in range(4, 8):
        print("\n")
        for j in range(4):
            print(game_board[i][j], end="  ")
    print("\n")
    # the fourth batch
    for i in range(4, 8):
        print("\n")
        for j in range(4, 8):
            print(game_board[i][j], end="  ")
    print("\n")

    print("___________________")
    print("\n")


def main():
    # assembling the game board
    game_board = np.zeros((8, 8), dtype=str)
    for i in range(8):
        for j in range(8):
            game_board[i][j] = "."
    selection = 3

    # Get user input for difficulty level
    difficulty = input("Select difficulty level (easy, difficult, insane): ").lower()
    print()

    if difficulty == "easy":
        depth = 2

    elif difficulty == "difficult":
        depth = 4

    elif difficulty == "insane":
        depth = 6

    else:
        print("Invalid input. Difficulty level set to difficult by default.")
        depth = 4

    print("Depth of the Alpha-Beta Procedure has been set to : ", depth, "\n")

    if selection == 3:
        random_num = 0
        flag_2 = 0
        beginner = eval(input("Who starts first?! \n1.Computer \n2.User\n"))
        if beginner == 1:
            flag = 1
        elif beginner == 2:
            flag = 0
        else:
            print("Invalid input! User starts first by default.")
            flag = 0

        while True:
            if flag_2 == 0:
                print_board(game_board)
                flag_2 = 1
            if flag == 0:
                # run time calculation
                while True:
                    try:
                        user_x, user_y, user_matrix = eval(input("Enter co-ordinates x,y,z : "))
                        user_y, user_x = user_y - 1, user_x - 1

                        if user_matrix == 3:
                            user_x = user_x + 4
                        elif user_matrix == 2:
                            user_y = user_y + 4
                        elif user_matrix == 4:
                            user_x = user_x + 4
                            user_y = user_y + 4

                        if game_board[user_x][user_y] == ".":
                            break
                        else:
                            print("\nSelected index is already used!\n")

                    except TypeError:
                        print("\nInvalid input! Try again.\n")

                if game_board[user_x][user_y] == ".":
                    game_board[user_x][user_y] = "X"
                    print("\nUser's move:")
                    final_result = goal.is_goal(game_board)
                    if final_result != "D":
                        print_board(game_board)
                        print(final_result, " has won!!")
                        return
                    print_board(game_board)

            flag = 0
            # computer's turn
            if random_num > 0:
                rand_x = np.random.randint(0, 7)
                rand_y = np.random.randint(0, 7)
                while game_board[rand_x][rand_y] != ".":
                    rand_x = np.random.randint(0, 7)
                    rand_y = np.random.randint(0, 7)
                print("Computer's move:")
                game_board[rand_x][rand_y] = "O"
                print_board(game_board)
                random_num -= 1
            else:
                board = alpha_beta.Minimax(game_board, "O", depth)
                print("Computer's move:")
                final_result = goal.is_goal(board)
                if final_result != "D":
                    print_board(board)
                    print(final_result, " has won!!")
                    return
                print_board(board)


main()
