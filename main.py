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

game_over = False
frame = 0



# create stars


for _ in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    speed = random.uniform(0.5, 2.5)
    size = random.choice([1, 1, 2])
    
    stars.append({
        "x": x,
        "y": y,
        "speed": speed,
        "size": size
    })


# player

def draw_player():
    canvas.delete("player")
    
    x = player_x
    y = player_y
    
    # glow
    canvas.create_oval(
        x - 25,
        y -25,
        x + 25,
        y + 25,
        fill="#101040",
        outLine="",
        tags="player"
    )
    
    # ship
    
    canvas.create_polygon(
        x,
        y - 30,
        x - 22,
        y + 20,
        x,
        y + 10,
        x + 22,
        y + 20,
        fill="#00ffff",
        outLine="",
        tags="player"
    )
    
    
    # Magenta engine flame
    
    canvas.create_polygon(
        x - 6, y + 12,
        x, y + 32 + random.randint(0, 6),
        x + 6, y + 12,
        fill="#ff00ff",
        outline="",
        tags="player"
    )
