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
        self.easy_button = tk.Button(self.master, text="Easy", command=lambda: self.start_game("easy"), bg="yellow", width=10, height=2)
        self.easy_button.pack(pady=5)

        self.difficult_button = tk.Button(self.master, text="Difficult", command=lambda: self.start_game("difficult"), bg="yellow", width=10, height=2)
        self.difficult_button.pack(pady=5)

        self.insane_button = tk.Button(self.master, text="Insane", command=lambda: self.start_game("insane"), bg="yellow", width=10, height=2)
        self.insane_button.pack(pady=5)

        # Rules Button
        self.rules_button = tk.Button(self.master, text="Rules", command=self.show_rules, bg="yellow", width=10, height=2)
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
        user_starts_first = messagebox.askyesno("Game Started", initial_message + "\n\nWould you like to make the first move?", icon='question')

        if user_starts_first:
            messagebox.showinfo("Game Started", "User starts first!")
            self.show_game_board()

        else:
            messagebox.showinfo("Game Started", "Computer starts first!")

    def show_rules(self):
        # Display rules or open a new window with rules here
        messagebox.showinfo("Rules", "Your rules here.")

    def show_game_board(self):
        # Destroy existing widgets in the main window
        for widget in self.master.winfo_children():
            widget.destroy()

        # Create a 4x4 grid repeated vertically with double line breaks between each four rows
        a = 0
        for i in range(4):
            # Create 4x4 buttons for each row
            for row in range(4):
                for col in range(4):
                    button = tk.Button(self.master, text=str(a), width=3, height=1)
                    button.grid(row=(i * 4) + row, column=col, padx=5, pady=5)
                    a += 1


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()
