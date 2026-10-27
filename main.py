import tkinter as tk
import random
import math


# game settings

WIDTH = 600
HEIGHT = 500

PLAYER_SPEED = 9
METEOR_SPEED = 4
METEOR_MAX_SPEED = 8

# main window

root = tk.Tk()
root.title("Qamro's NEON DODGE")
root.resizable(False, False)

canvas = tk.Canvas(
    root,
    width=WIDTH,
    height=HEIGHT,
    bg="#050514",
    highlightthickness=0
)

canvas.pack()



# game variables

player_x = WIDTH // 2
player_y = HEIGHT - 80

left_pressed = False
right_pressed = False

meteors = []
particles = []
stars = []

