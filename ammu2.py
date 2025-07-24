import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.width = 500
        self.height = 500
        self.cell_size = 20  # size of each segment

        self.direction = 'Right'
        self.score = 0

        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        # Initialize snake: list of (x,y) tuples
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = None

        self.create_food()
        self.draw_snake()
        self.root.bind("<Key>", self.change_direction)

        self.game_loop()

    def create_food(self):
        while True:
            x = random.randint(0, (self.width - self.cell_size) // self.cell_size) * self.cell_size
            y = random.randint(0, (self.height - self.cell_size) // self.cell_size) * self.cell_size
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def draw_snake(self):
        self.canvas.delete("all")

        # Draw food
        self.canvas.create_rectangle(self.food[0], self.food[1],
                                     self.food[0] + self.cell_size,
                                     self.food[1] + self.cell_size,
                                     fill="red", outline="")

        # Draw snake
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size,
                                         fill="green", outline="")

        # Draw score
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", font=("Arial", 14))

    def change_direction(self, event):
        key = event.keysym
        opposites = {'Left':'Right', 'Right':'Left', 'Up':'Down', 'Down':'Up'}
        if key in ['Left', 'Right', 'Up', 'Down']:
            if opposites[key] != self.direction:  # prevent reverse
                self.direction = key

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == 'Left':
            head_x -= self.cell_size
        elif self.direction == 'Right':
            head_x += self.cell_size
        elif self.direction == 'Up':
            head_y -= self.cell_size
        elif self.direction == 'Down':
            head_y += self.cell_size

        new_head = (head_x, head_y)

        # Check collisions
        if (head_x < 0 or head_x >= self.width or
            head_y < 0 or head_y >= self.height or
            new_head in self.snake):
            self.game_over()
            return False

        self.snake.insert(0, new_head)

        # Check if food eaten
        if new_head == self.food:
            self.score += 1
            self.create_food()
        else:
            self.snake.pop()  # remove tail

        return True

    def game_loop(self):
        if self.move_snake():
            self.draw_snake()
            self.root.after(100, self.game_loop)  # speed of snake
        else:
            pass  # game over, no loop continuation

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(self.width//2, self.height//2,
                                text=f"Game Over!\nScore: {self.score}",
                                fill="white", font=("Arial", 24))


if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
