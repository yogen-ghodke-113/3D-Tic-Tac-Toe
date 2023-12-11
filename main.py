import tkinter as tk
from tkinter import messagebox

import alpha_beta
import goal


class TicTacToeUI:
    def __init__(self, master):
        self.master = master
        self.master.title("3D Tic Tac Toe")
        self.master.state("zoomed")  # Open the window maximized
        self.master.geometry("400x400")
        self.button_clicked_var = tk.StringVar()
        self.button_clicked_var.set("")

        # Heading
        self.heading_label = tk.Label(self.master, text="3D Tic Tac Toe", font=("Helvetica", 20, "bold"))
        self.heading_label.pack(pady=10)

        # Difficulty Selection
        self.difficulty_label = tk.Label(self.master, text="Select Difficulty", font=("Helvetica", 14))
        self.difficulty_label.pack(pady=10)

        # Difficulty Buttons
        self.easy_button = tk.Button(self.master, text="Easy", command=lambda: self.start_game("easy"), bg="yellow",
                                     width=10, height=2)
        self.easy_button.pack(pady=5)

        self.difficult_button = tk.Button(self.master, text="Difficult", command=lambda: self.start_game("difficult"),
                                          bg="yellow", width=10, height=2)
        self.difficult_button.pack(pady=5)

        self.insane_button = tk.Button(self.master, text="Insane", command=lambda: self.start_game("insane"),
                                       bg="yellow", width=10, height=2)
        self.insane_button.pack(pady=5)

        # Rules Button
        self.rules_button = tk.Button(self.master, text="Rules", command=self.show_rules, bg="yellow", width=10,
                                      height=2)
        self.rules_button.place(x=20, y=350)

        self.button_click_stack = []

    def start_game(self, difficulty):
        if difficulty == "easy":
            depth = 2
        elif difficulty == "difficult":
            depth = 4
        elif difficulty == "insane":
            depth = 6
        else:
            depth = 4  # Default depth if difficulty is not recognized

        # Show initial message box
        initial_message = f"Difficulty selected: {difficulty}\nDepth of the Alpha-Beta Procedure has been set to: {depth}"
        user_starts_first = messagebox.askyesno("Game Started",
                                                initial_message + "\n\nWould you like to make the first move?",
                                                icon='question')

        if user_starts_first:
            messagebox.showinfo("Game Started", "User starts first!")
            self.show_game_board(True)

        else:
            messagebox.showinfo("Game Started", "Computer starts first!")
            self.show_game_board(False)

    def print_board(self, game_board):
        print(game_board)

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

    def show_rules(self):
        rules_text = """
        3D Tic Tac Toe Rules:

        No. of Players = 2
        Grid : 4x4x4
        Markers : User = X and CPU = O
        Win condition : 4 in a row (horizontal, vertical, diagonal, planar / 3D)    
        Turns: Alternating, one marker per turn
        No blocking: Cannot overwrite opponent's move

        """

        # Create a new Toplevel window
        rules_window = tk.Toplevel(self.master)
        rules_window.title("Rules")

        # Create a label with the rules text and set the font size
        rules_label = tk.Label(rules_window, text=rules_text, font=("Helvetica", 14))
        rules_label.pack(padx=10, pady=10)

    def update_board(self, game_board):
        import numpy as np
        # game_board = np.zeros((8, 8), dtype=str)
        # game_board = np.random.randint(0, 10, size=(8, 8))
        print(game_board)
        # the first batch
        for row in range(4):
            for col in range(4):
                button_name = f"button_{row + 1}{col + 1}1"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row][col])
                button.config(text=new_text)

        for row in range(4):
            for col in range(4):
                button_name = f"button_{row + 1}{col + 1}2"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row][col + 4])
                button.config(text=new_text)

        for row in range(4):
            for col in range(4):
                button_name = f"button_{row + 1}{col + 1}3"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row + 4][col])
                button.config(text=new_text)

        for row in range(4):
            for col in range(4):
                button_name = f"button_{row + 1}{col + 1}4"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row + 4][col + 4])
                button.config(text=new_text)

    def extract_button_coordinates(self, button_names):
        x, y, z = map(int, button_names[7:])  # Extracting x, y, z from the button name
        self.button_click_stack.append([x, y, z])
        self.button_clicked_var.set("clicked")  # Set the variable to signal that the button is clicked
        # result_text = f"x = {x} , y = {y}, z = {z}"
        # right_heading_label.config(text=result_text)
        # self.board()

    def make_label_invisible(self, label):
        # Get the current foreground color of the label
        fg_color = label.cget("foreground")
        # Set the foreground color to be the same as the background color (making it invisible)
        label.configure(foreground=self.master.cget("background"))

    def show_game_board(self, Flag):
        # Destroy existing widgets in the main window
        for widget in self.master.winfo_children():
            widget.destroy()

        # Creates cells for the 4x4 grid in layer 1 of the 3d tic tac toe board (Cells 1-16)
        a = 0
        for row in range(0, 4):
            for col in range(4):
                button_name = f"button_{row + 1}{col + 1}1"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=".", width=3, height=1, name=button_name,
                                   command=lambda name=button_name: self.extract_button_coordinates(name))
                button.grid(row=row, column=col, padx=5, pady=5)
                a += 1

        # Adds divider between the first and second layer
        for col in range(4):
            label = tk.Label(self.master, text="", width=1, height=2)
            label.grid(row=4, column=col)

        # Creates cells for the 4x4 grid in layer 2 of the 3d tic tac toe board (Cells 17-32)
        for row in range(5, 9):
            for col in range(4):
                button_name = f"button_{row - 4}{col + 1}2"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=".", width=3, height=1, name=button_name,
                                   command=lambda name=button_name: self.extract_button_coordinates(name))
                button.grid(row=row, column=col, padx=5, pady=5)

        # Adds divider between the second and third layer
        for col in range(4):
            label = tk.Label(self.master, text="", width=1, height=2)
            label.grid(row=9, column=col)

        # Creates cells for the 4x4 grid in layer 3 of the 3d tic tac toe board (Cells 33-48)
        for row in range(10, 14):
            for col in range(4):
                button_name = f"button_{row - 9}{col + 1}3"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=".", width=3, height=1, name=button_name,
                                   command=lambda name=button_name: self.extract_button_coordinates(name))
                button.grid(row=row, column=col, padx=5, pady=5)

        # Adds divider between the third and fourth layer
        for col in range(4):
            label = tk.Label(self.master, text="", width=1, height=2)
            label.grid(row=14, column=col)

        # Creates cells for the 4x4 grid in layer 4 of the 3d tic tac toe board (Cells 49-64)
        for row in range(15, 19):
            for col in range(4):
                button_name = f"button_{row - 14}{col + 1}4"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=".", width=3, height=1, name=button_name,
                                   command=lambda name=button_name: self.extract_button_coordinates(name))
                button.grid(row=row, column=col, padx=5, pady=5)

        invisible_label = tk.Label(self.master, text="...................", font=("Helvetica", 14))
        invisible_label.grid(row=0, column=5, rowspan=2, padx=10, pady=10, sticky="N")
        self.make_label_invisible(invisible_label)

        right_heading_label = tk.Label(self.master, text="3D TIC TAC TOE GAME BOARD ", font=("Times New Roman", 22))
        right_heading_label.grid(row=0, column=6, rowspan=2, padx=10, pady=10, sticky="N")

        descr_label = tk.Label(self.master, text="CPU = O, User = X ", font=("Helvetica", 18))
        descr_label.grid(row=4, column=6, rowspan=2, padx=10, pady=10, sticky="N")

        instr_label = tk.Label(self.master, text=".........Rt", font=("Helvetica", 16))
        instr_label.grid(row=8, column=6, rowspan=2, padx=10, pady=10, sticky="N")

        # assembling the game board
        import numpy as np
        game_board = np.zeros((8, 8), dtype=str)
        for i in range(8):
            for j in range(8):
                game_board[i][j] = "."

        self.update_board(game_board)
        print(game_board)

        result_declared = False

        instr_label.config(text="It's your turn click a button to make a move.")
        random_num = 0
        depth = 3

        while True:
            if Flag:
                while True:
                    # Wait for the button click
                    self.master.wait_variable(self.button_clicked_var)
                    # Get the user's input
                    user_x, user_y, user_matrix = self.button_click_stack[-1]
                    # Update the instruction label
                    # instr_label.config(text=f"Your input: {user_x}, {user_y}, {user_matrix}")

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
                        instr_label.config(text=f"Selected cell is already used! Try a different move.")
                        print("\nSelected index is already used!\n")
                        # Reset the button click variable
                        self.button_clicked_var.set("")
                        continue
                if game_board[user_x][user_y] == ".":
                    game_board[user_x][user_y] = "X"
                    print("\nUser's move:")
                    final_result = goal.is_goal(game_board)
                    if final_result != "D":
                        self.update_board(game_board)
                        print(game_board)
                        instr_label.config(text=f"{final_result} has won the Game !!")
                        print(final_result, " has won!!")
                        result_declared = True
                        return
                    self.update_board(game_board)
                    print(game_board)
            Flag = True

            # computer's turn
            if random_num > 0:
                rand_x = np.random.randint(0, 7)
                rand_y = np.random.randint(0, 7)
                while game_board[rand_x][rand_y] != ".":
                    rand_x = np.random.randint(0, 7)
                    rand_y = np.random.randint(0, 7)
                print("Computer's move:")
                game_board[rand_x][rand_y] = "O"
                self.update_board(game_board)
                print(game_board)
                random_num -= 1
            else:
                board = alpha_beta.Minimax(game_board, "O", depth)
                print("Computer's move:")
                final_result = goal.is_goal(board)
                if final_result != "D":
                    self.update_board(game_board)
                    print(game_board)
                    instr_label.config(text=f"{final_result} has won the Game !!")
                    print(final_result, " has won!!")
                    result_declared = True
                    return
                self.update_board(game_board)
                print(game_board)

            print("its here 1")
            # Reset the button click variable
            if result_declared:
                break
            self.button_clicked_var.set("")

        print("its here 2")
        instr_label.config(text=f"Your input: {user_x}, {user_y}, {user_matrix}")
        # instr_label.config(text=f"{final_result} has won the Game !!")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()
