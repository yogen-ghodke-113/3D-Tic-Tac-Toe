import tkinter as tk
from tkinter import messagebox


class TicTacToeUI:
    def __init__(self, master):
        self.master = master
        self.master.title("3D Tic Tac Toe")
        self.master.state("zoomed")  # Open the window maximized
        self.master.geometry("400x400")

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
            self.show_game_board()

        else:
            messagebox.showinfo("Game Started", "Computer starts first!")

    def show_rules(self):
        # Display rules or open a new window with rules here
        messagebox.showinfo("Rules", "Your rules here.")

    def show_game_board(self):

        def button_click(button_names):
            x, y, z = map(int, button_names[7:])  # Extracting x, y, z from the button name
            result_text = f"x = {x} , y = {y}, z = {z}"
            right_heading_label.config(text=result_text)
            self.update_board()

        # Destroy existing widgets in the main window
        for widget in self.master.winfo_children():
            widget.destroy()

        button_text_first_part = [str(i) for i in range(1, 17)]
        button_text_second_part = [str(i) for i in range(17, 33)]
        button_text_third_part = [str(i) for i in range(33, 49)]
        button_text_fourth_part = [str(i) for i in range(49, 65)]

        # Creates cells for the 4x4 grid in layer 1 of the 3d tic tac toe board (Cells 1-16)
        a = 0
        for row in range(0, 4):
            for col in range(4):
                button_name = f"button_{row + 1}{col + 1}1"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=button_text_first_part[a], width=3, height=1, name=button_name,
                                   command=lambda name=button_name: button_click(name))
                button.grid(row=row, column=col, padx=5, pady=5)
                a += 1

        # Adds divider between the first and second layer
        for col in range(4):
            label = tk.Label(self.master, text=".", width=1, height=1)
            label.grid(row=4, column=col)

        # Creates cells for the 4x4 grid in layer 2 of the 3d tic tac toe board (Cells 17-32)
        a = 0
        for row in range(5, 9):
            for col in range(4):
                button_name = f"button_{row - 4}{col + 1}2"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=button_text_second_part[a], width=3, height=1, name=button_name,
                                   command=lambda name=button_name: button_click(name))
                button.grid(row=row, column=col, padx=5, pady=5)
                a += 1

        # Adds divider between the second and third layer
        for col in range(4):
            label = tk.Label(self.master, text=".", width=1, height=1)
            label.grid(row=9, column=col)

        # Creates cells for the 4x4 grid in layer 3 of the 3d tic tac toe board (Cells 33-48)
        a = 0
        for row in range(10, 14):
            for col in range(4):
                button_name = f"button_{row - 9}{col + 1}3"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=button_text_third_part[a], width=3, height=1, name=button_name,
                                   command=lambda name=button_name: button_click(name))
                button.grid(row=row, column=col, padx=5, pady=5)
                a += 1

        # Adds divider between the third and fourth layer
        for col in range(4):
            label = tk.Label(self.master, text=".", width=1, height=1)
            label.grid(row=14, column=col)

        # Creates cells for the 4x4 grid in layer 4 of the 3d tic tac toe board (Cells 49-64)
        a = 0
        for row in range(15, 19):
            for col in range(4):
                button_name = f"button_{row - 14}{col + 1}4"  # Using f-string to create the button identifier
                button = tk.Button(self.master, text=button_text_fourth_part[a], width=3, height=1, name=button_name,
                                   command=lambda name=button_name: button_click(name))
                button.grid(row=row, column=col, padx=5, pady=5)
                a += 1

        right_heading_label = tk.Label(self.master, text="...................", font=("Helvetica", 14))
        right_heading_label.grid(row=0, column=5, rowspan=2, padx=10, pady=10, sticky="N")
        right_heading_label.pack_forget()

        right_heading_label = tk.Label(self.master, text="Heading on the Right", font=("Helvetica", 14))
        right_heading_label.grid(row=0, column=6, rowspan=2, padx=10, pady=10, sticky="N")

        right_heading_label = tk.Label(self.master, text=".........Rt", font=("Helvetica", 14))
        right_heading_label.grid(row=3, column=6, rowspan=2, padx=10, pady=10, sticky="N")

    def update_board(self):
        import numpy as np
        # game_board = np.zeros((8, 8), dtype=str)
        game_board = np.random.randint(0, 10, size=(8, 8))
        print(game_board)
        # the first batch
        for row in range(4):
            for col in range(4):
                button_name = f"button_{row+1}{col+1}1"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row][col])
                button.config(text=new_text)

        for row in range(4):
            for col in range(4):
                button_name = f"button_{row+1}{col+1}2"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row][col+4])
                button.config(text=new_text)

        for row in range(4):
            for col in range(4):
                button_name = f"button_{row+1}{col+1}3"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row+4][col])
                button.config(text=new_text)

        for row in range(4):
            for col in range(4):
                button_name = f"button_{row+1}{col+1}4"
                button = self.master.nametowidget(button_name)
                new_text = str(game_board[row+4][col+4])
                button.config(text=new_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()
