# ui.py
import tkinter as tk
from gamelogic import Game

class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = Game()
        self.buttons = []
        self.create_ui()

    def create_ui(self):
        # 3x3 grid of buttons
        for i in range(9):
            btn = tk.Button(
                self.root, text=" ", font=("Helvetica", 32), width=5, height=2,
                command=lambda idx=i: self.click(idx)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Reset button
        reset_btn = tk.Button(
            self.root, text="Reset Game", font=("Helvetica", 14),
            command=self.reset_game, bg="lightblue"
        )
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", pady=10)

    def click(self, idx):
        if self.game.board[idx] != " ":
            return  # Ignore if already filled

        # Player move
        self.game.board[idx] = "X"
        self.buttons[idx]["text"] = "X"

        winner = self.game.check_winner()
        if winner:
            self.show_winner_popup(winner)
            return

        # AI move
        ai_move = self.game.best_ai_move()
        if ai_move is not None:
            self.game.board[ai_move] = "O"
            self.buttons[ai_move]["text"] = "O"

        winner = self.game.check_winner()
        if winner:
            self.show_winner_popup(winner)

    def show_winner_popup(self, winner):
        popup = tk.Toplevel(self.root)
        popup.attributes('-fullscreen', True)  # Full-screen
        popup.configure(bg='black')

        if winner == "Draw":
            text = "It's a Draw!"
        else:
            text = f"{winner} Wins!"

        label = tk.Label(popup, text=text, font=("Helvetica", 72, "bold"), fg="yellow", bg="black")
        label.pack(expand=True)

        btn = tk.Button(popup, text="Play Again", font=("Helvetica", 24),
                        command=lambda: [popup.destroy(), self.reset_game()], bg="lightgreen")
        btn.pack(pady=50)

    def reset_game(self):
        self.game = Game()
        for btn in self.buttons:
            btn.config(text=" ", bg="SystemButtonFace")


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeUI(root)
    root.mainloop()
