import tkinter as tk
import random

# CONSTANTS
GAME_WIDTH = 1000
GAME_HEIGHT = 500
DELAY_MS = 100
SPACE_SIZE = 20
BODY_PARTS = 5
SNAKE_COLOR = "#FF0000"
FOOD_COLOR = "#00FF00"
BACKGROUND_COLOR = "#000000"
INITIAL_DIRECTION = "Right"

COLS = GAME_WIDTH // SPACE_SIZE
ROWS = GAME_HEIGHT // SPACE_SIZE
TOTAL_CELLS = COLS * ROWS

OPPOSITES = {"left": "right", "right": "left", "up": "down", "down": "up"}

#Game state (start_game / restrat_game)
window = None
canvas = None
label = None
snake = None
food = None
score = 0
direction = INITIAL_DIRECTION
next_direction = INITIAL_DIRECTION
game_running = False


# CLASSES
class Snake:
    def __init__(self):
        self.coordinats = []
        self.squares = []

        start_x = (COLS // 2) * SPACE_SIZE
        start_y = (ROWS // 2) * SPACE_SIZE

        # Head first, body trailing to the left (snake starts moving right)
        for i in range(BODY_PARTS):
            self.coordinats.append([start_x - i * SPACE_SIZE, start_y])

        for x, y in self.coordinats:
            square = canvas.create_rectangle(
                x, y, x + SPACE_SIZE, y + SPACE_SIZE,
                fill=SNAKE_COLOR, tag="snake"
            )
            self.squares.append(square)


class Food:
    def __init__(self, x, y):
        self.coordinates = [x, y]
        canvas.create_oval(
            x, y, x + SPACE_SIZE, y + SPACE_SIZE,
            fill=FOOD_COLOR, tag="food"
        )

# FUNCTIOS
def create_food():


def next_turn():


def change_direction():


def check_collision():


def game_over():


def reset_state():


def restart_game():


def start_game():
