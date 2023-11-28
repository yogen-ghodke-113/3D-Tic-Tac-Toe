import numpy as np


def test_heu():
    board = np.zeros((8, 8), dtype=str)
    for i in range(8):
        for j in range(8):
            board[i][j] = "."

    board[0][0] = "X"
    board[2][0] = "X"
    board[3][0] = "X"
    points = heuristic(board)
    print(points)


def heuristic(board, turn):
    best_point = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != ".":
                player = board[i][j]
                if turn == "O":
                    if i == 0 or i == 4:
                        if board[i + 1][j] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 2][j] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if i == 1 or i == 5:
                        if board[i + 1][j] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 2][j] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if i == 2 or i == 6:
                        if board[i + 1][j] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                    if j == 0 or j == 4:
                        if board[i][j + 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i][j + 2] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if j == 1 or j == 5:
                        if board[i][j + 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i][j + 2] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if j == 2 or j == 6:
                        if board[i][j + 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                    if (i == 0 and j == 0) or (i == 0 and j == 4) or (i == 4 and j == 0) or (i == 4 and j == 4):
                        if board[i + 1][j + 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 2][j + 2] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if (i == 1 and j == 1) or (i == 1 and j == 5) or (i == 5 and j == 1) or (i == 5 and j == 5):
                        if board[i + 1][j + 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 2][j + 2] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if (i == 2 and j == 2) or (i == 2 and j == 6) or (i == 6 and j == 2) or (i == 6 and j == 6):
                        if board[i + 1][j + 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                    if (i == 0 and j == 3) or (i == 0 and j == 7) or (i == 4 and j == 3) or (i == 4 and j == 7):
                        if board[i + 1][j - 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 2][j - 2] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if (i == 1 and j == 2) or (i == 1 and j == 6) or (i == 5 and j == 2) or (i == 5 and j == 6):
                        if board[i + 1][j - 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 2][j - 2] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                    if (i == 2 and j == 1) or (i == 2 and j == 5) or (i == 6 and j == 1) or (i == 6 and j == 5):
                        if board[i + 1][j - 1] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                    if i <= 3 and j <= 3:
                        if board[i][j + 4] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 4][j] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                        if i == 0:
                            if board[i + 1][j + 4] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 6][j] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                            if j == 0:
                                if board[i + 1][j + 5] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 6][j + 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                            if j == 3:
                                if board[i + 1][j + 3] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 6][j - 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                        if i == 3:
                            if board[i - 1][j + 4] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 2][j] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                            if j == 0:
                                if board[i - 1][j + 5] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 2][j + 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                            if j == 3:
                                if board[i - 1][j + 3] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 2][j - 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                        if j == 0:
                            if board[i][j + 5] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 4][j + 2] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                        if j == 3:
                            if board[i][j + 3] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 4][j - 2] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                    if i <= 3 and (j > 3 and j <= 7):
                        if board[i + 4][j - 4] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                            if board[i + 4][j] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                        if i == 1:
                            if board[i + 5][j - 4] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 6][j] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                            if j == 5:
                                if board[i + 5][j - 3] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 6][j + 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                            if j == 6:
                                if board[i + 5][j - 5] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 6][j - 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                        if i == 2:
                            if board[i + 3][j - 4] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 2][j] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                            if j == 5:
                                if board[i + 3][j - 3] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 2][j + 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                            if j == 6:
                                if board[i + 3][j - 5] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                                    if board[i + 2][j - 2] == player:
                                        if player == "X":
                                            best_point -= 1
                                        elif player == "O":
                                            best_point += 1
                        if j == 5:
                            if board[i + 4][j - 3] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 4][j + 2] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                        if j == 6:
                            if board[i + 4][j - 5] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                                if board[i + 4][j - 2] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                    if j <= 3 and (i > 3 and i <= 7):
                        if board[i][j + 4] == player:
                            if player == "X":
                                best_point -= 1
                            elif player == "O":
                                best_point += 1
                        if i == 6:
                            if board[i + 1][j + 4] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                            if j == 2:
                                if board[i + 1][j + 5] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                            if j == 1:
                                if board[i + 1][j + 3] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                        if i == 5:
                            if board[i - 1][j + 4] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                            if j == 2:
                                if board[i - 1][j + 5] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                            if j == 1:
                                if board[i - 1][j + 3] == player:
                                    if player == "X":
                                        best_point -= 1
                                    elif player == "O":
                                        best_point += 1
                        if j == 2:
                            if board[i][j + 5] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1
                        if j == 1:
                            if board[i][j + 3] == player:
                                if player == "X":
                                    best_point -= 1
                                elif player == "O":
                                    best_point += 1

                elif turn == "X":
                    if i == 0 or i == 4:
                        if board[i + 1][j] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 2][j] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if i == 1 or i == 5:
                        if board[i + 1][j] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 2][j] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if i == 2 or i == 6:
                        if board[i + 1][j] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                    if j == 0 or j == 4:
                        if board[i][j + 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i][j + 2] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if j == 1 or j == 5:
                        if board[i][j + 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i][j + 2] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if j == 2 or j == 6:
                        if board[i][j + 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                    if (i == 0 and j == 0) or (i == 0 and j == 4) or (i == 4 and j == 0) or (i == 4 and j == 4):
                        if board[i + 1][j + 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 2][j + 2] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if (i == 1 and j == 1) or (i == 1 and j == 5) or (i == 5 and j == 1) or (i == 5 and j == 5):
                        if board[i + 1][j + 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 2][j + 2] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if (i == 2 and j == 2) or (i == 2 and j == 6) or (i == 6 and j == 2) or (i == 6 and j == 6):
                        if board[i + 1][j + 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                    if (i == 0 and j == 3) or (i == 0 and j == 7) or (i == 4 and j == 3) or (i == 4 and j == 7):
                        if board[i + 1][j - 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 2][j - 2] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if (i == 1 and j == 2) or (i == 1 and j == 6) or (i == 5 and j == 2) or (i == 5 and j == 6):
                        if board[i + 1][j - 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 2][j - 2] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                    if (i == 2 and j == 1) or (i == 2 and j == 5) or (i == 6 and j == 1) or (i == 6 and j == 5):
                        if board[i + 1][j - 1] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                    if i <= 3 and j <= 3:
                        if board[i][j + 4] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 4][j] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                        if i == 0:
                            if board[i + 1][j + 4] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 6][j] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                            if j == 0:
                                if board[i + 1][j + 5] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 6][j + 2] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                            if j == 3:
                                if board[i + 1][j + 3] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 6][j - 1] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                        if i == 3:
                            if board[i - 1][j + 4] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 2][j] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                            if j == 0:
                                if board[i - 1][j + 5] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 2][j + 2] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                            if j == 3:
                                if board[i - 1][j + 3] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 2][j - 2] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                        if j == 0:
                            if board[i][j + 5] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 4][j + 2] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                        if j == 3:
                            if board[i][j + 3] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 4][j - 2] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                    if i <= 3 and (j > 3 and j <= 7):
                        if board[i + 4][j - 4] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                            if board[i + 4][j] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                        if i == 1:
                            if board[i + 5][j - 4] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 6][j] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                            if j == 5:
                                if board[i + 5][j - 3] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 6][j + 2] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                            if j == 6:
                                if board[i + 5][j - 5] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 6][j - 2] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                        if i == 2:
                            if board[i + 3][j - 4] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 2][j] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                            if j == 5:
                                if board[i + 3][j - 3] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 2][j + 2] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                            if j == 6:
                                if board[i + 3][j - 5] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                                    if board[i + 2][j - 2] == player:
                                        if player == "X":
                                            best_point += 1
                                        elif player == "O":
                                            best_point -= 1
                        if j == 5:
                            if board[i + 4][j - 3] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 4][j + 2] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                        if j == 6:
                            if board[i + 4][j - 5] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                                if board[i + 4][j - 2] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                    if j <= 3 and (i > 3 and i <= 7):
                        if board[i][j + 4] == player:
                            if player == "X":
                                best_point += 1
                            elif player == "O":
                                best_point -= 1
                        if i == 6:
                            if board[i + 1][j + 4] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                            if j == 2:
                                if board[i + 1][j + 5] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                            if j == 1:
                                if board[i + 1][j + 3] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                        if i == 5:
                            if board[i - 1][j + 4] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                            if j == 2:
                                if board[i - 1][j + 5] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                            if j == 1:
                                if board[i - 1][j + 3] == player:
                                    if player == "X":
                                        best_point += 1
                                    elif player == "O":
                                        best_point -= 1
                        if j == 2:
                            if board[i][j + 5] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
                        if j == 1:
                            if board[i][j + 3] == player:
                                if player == "X":
                                    best_point += 1
                                elif player == "O":
                                    best_point -= 1
    return best_point
