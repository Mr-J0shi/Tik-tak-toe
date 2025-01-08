import tkinter as tk
from tkinter import messagebox
import time

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.player_names = {'X': 'Player X', 'O': 'Player O'}
        self.scores = {'X': 0, 'O': 0, 'Draws': 0}
        self.start_menu()

    def start_menu(self):
        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        tk.Label(self.menu_frame, text="Welcome to Pratyush Game", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.menu_frame, text="Enter Player X's Name:").pack()
        self.player_x_name = tk.Entry(self.menu_frame)
        self.player_x_name.pack()

        tk.Label(self.menu_frame, text="Enter Player O's Name:").pack()
        self.player_o_name = tk.Entry(self.menu_frame)
        self.player_o_name.pack()

        self.start_button = tk.Button(self.menu_frame, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.quit_button = tk.Button(self.menu_frame, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

    def start_game(self):
        if self.player_x_name.get():
            self.player_names['X'] = self.player_x_name.get()
        if self.player_o_name.get():
            self.player_names['O'] = self.player_o_name.get()

        self.menu_frame.destroy()
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.start_time = time.time()

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.scoreboard_frame = tk.Frame(self.root)
        self.scoreboard_frame.pack()
        self.update_scoreboard()

        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.game_frame, text=' ', width=10, height=3,
                                               command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

        self.timer_label = tk.Label(self.game_frame, text="Time: 0")
        self.timer_label.grid(row=3, columnspan=3)

        self.player_indicator = tk.Label(self.game_frame, text=f"{self.player_names[self.current_player]}'s Turn",
                                         font=("Helvetica", 12))
        self.player_indicator.grid(row=4, columnspan=3)

        self.restart_button = tk.Button(self.game_frame, text="Restart", command=self.restart_game)
        self.restart_button.grid(row=5, column=0)

        self.reset_scores_button = tk.Button(self.game_frame, text="Reset Scores", command=self.reset_scores)
        self.reset_scores_button.grid(row=5, column=1)

        self.quit_button = tk.Button(self.game_frame, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=5, column=2)

        self.update_timer()

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"{self.player_names[self.current_player]} wins!")
                self.scores[self.current_player] += 1
                self.restart_game()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.scores['Draws'] += 1
                self.restart_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.player_indicator.config(text=f"{self.player_names[self.current_player]}'s Turn")
        else:
            messagebox.showwarning("Tic-Tac-Toe", "Invalid move. Try again.")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def restart_game(self):
        self.game_frame.destroy()
        self.scoreboard_frame.destroy()
        self.start_game()

    def reset_scores(self):
        self.scores = {'X': 0, 'O': 0, 'Draws': 0}
        self.update_scoreboard()

    def quit_game(self):
        self.root.quit()

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"Time: {elapsed_time}")
        self.root.after(1000, self.update_timer)

    def update_scoreboard(self):
        self.scoreboard_frame.destroy()
        self.scoreboard_frame = tk.Frame(self.root)
        self.scoreboard_frame.pack()

        tk.Label(self.scoreboard_frame, text="Scoreboard", font=("Helvetica", 14)).pack()

        tk.Label(self.scoreboard_frame, text=f"{self.player_names['X']}: {self.scores['X']}").pack()
        tk.Label(self.scoreboard_frame, text=f"{self.player_names['O']}: {self.scores['O']}").pack()
        tk.Label(self.scoreboard_frame, text=f"Draws: {self.scores['Draws']}").pack()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
