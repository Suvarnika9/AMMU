import tkinter as tk
from tkinter import messagebox

# Game setup
coins = {
    "Penny": 0.01,
    "Nickel": 0.05,
    "Dime": 0.10,
    "Quarter": 0.25
}

class MoneySorterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Sorter Game")
        self.score = 0

        self.create_widgets()
        self.new_coin()

    def create_widgets(self):
        self.info_label = tk.Label(self.root, text="Sort the coin into the correct bin!", font=("Arial", 14))
        self.info_label.pack(pady=10)

        self.coin_label = tk.Label(self.root, text="", font=("Arial", 24))
        self.coin_label.pack(pady=20)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        for coin_name in coins:
            btn = tk.Button(self.buttons_frame, text=coin_name, width=10,
                            command=lambda name=coin_name: self.check_answer(name))
            btn.pack(side=tk.LEFT, padx=5)

        self.score_label = tk.Label(self.root, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

    def new_coin(self):
        import random
        self.current_coin_name = random.choice(list(coins.keys()))
        self.coin_label.config(text=f"What is this? {self.current_coin_name}")

    def check_answer(self, selected_bin):
        if selected_bin == self.current_coin_name:
            self.score += 1
            messagebox.showinfo("Correct!", "Well done!")
        else:
            self.score -= 1
            messagebox.showerror("Oops!", "Wrong bin!")

        self.score_label.config(text=f"Score: {self.score}")
        self.new_coin()

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = MoneySorterGame(root)
    root.mainloop()
