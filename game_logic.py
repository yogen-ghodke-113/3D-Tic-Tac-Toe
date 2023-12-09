import tkinter as tk
from tkinter import messagebox
import numpy as np
import alpha_beta
import goal

class TicTacToe3DUI:
    def __init__(self, master):
        self.master = master
        self.master.title("3D Tic Tac Toe")
        self.game_board = np.zeros((8, 8), dtype=str)
        self.initialize_board()

        self.buttons = [[None for _ in range(8)] for _ in range(8)]

        for i in range(8):
            for j in range(8):
                self.buttons[i][j] = tk.Button(master, text="", width=5, height=2, command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

        self.depth = 4
        self.flag = 1  # 1 for computer, 0 for user
        self.random_num = 0

    def initialize_board(self):
        for i in range(8):
            for j in range(8):
                self.game_board[i][j] = "."

    def print_board(self):
        for i in range(8):
            for j in range(8):
                self.buttons[i][j].config(text=self.game_board[i][j])

    def make_move(self, row, col):
        if self.game_board[row][col] == ".":
            if self.flag == 0:
                self.game_board[row][col] = "X"
                final_result = goal.is_goal(self.game_board)
                if final_result != "D":
                    self.print_board()
                    messagebox.showinfo("Game Over", f"{final_result} has won!!")
                    self.reset_game()
                self.flag = 1
                self.computer_move()
            self.print_board()

    def computer_move(self):
        if self.random_num > 0:
            rand_x = np.random.randint(0, 7)
            rand_y = np.random.randint(0, 7)
            while self.game_board[rand_x][rand_y] != ".":
                rand_x = np.random.randint(0, 7)
                rand_y = np.random.randint(0, 7)
            self.game_board[rand_x][rand_y] = "O"
            self.print_board()
            self.random_num -= 1
        else:
            board = alpha_beta.Minimax(self.game_board, "O", self.depth)
            final_result = goal.is_goal(board)
            if final_result != "D":
                self.print_board()
                messagebox.showinfo("Game Over", f"{final_result} has won!!")
                self.reset_game()
            self.game_board = board
            self.print_board()

    def reset_game(self):
        self.initialize_board()
        self.print_board()
        self.flag = 1
        self.random_num = 0

def main():
    root = tk.Tk()
    app = TicTacToe3DUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
