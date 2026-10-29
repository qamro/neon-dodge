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



# Draw the moving starfield
def draw_stars():
    canvas.delete("stars")

    for star in stars:
        star["y"] += star["speed"]

        if star["y"] > HEIGHT:
            star["y"] = 0
            star["x"] = random.randint(0, WIDTH)

        canvas.create_oval(
            star["x"],
            star["y"],
            star["x"] + star["size"],
            star["y"] + star["size"],
            fill="#282849",
            outline="",
            tags="stars"
        )
        


# Create a meteor
def spawn_meteor():
    radius = random.randint(13, 25)
    x = random.randint(radius, WIDTH - radius)

    meteors.append({
        "x": x,
        "y": -radius,
        "radius": radius,
        "speed": min(
            METEOR_SPEED + frame // 1500,
            METEOR_MAX_SPEED
        )
    })


# draw all meteors

def draw_meteors():
    canvas.delete("meteor")

    for meteor in meteors:
        x = meteor["x"]
        y = meteor["y"]
        r = meteor["radius"]

        # outer glow
        canvas.create_oval(
            x - r - 5, y - r - 5,
            x + r + 5, y + r + 5,
            fill="#251025",
            outline="#70204e",
            width=2,
            tags="meteor"
        )

        # pink body
        canvas.create_oval(
            x - r, y - r,
            x + r, y + r,
            fill="#ff386b",
            outline="#ff80aa",
            width=2,
            tags="meteor"
        )

        # orange center
        canvas.create_oval(
            x - r * 0.55, y - r * 0.55,
            x + r * 0.55, y + r * 0.55,
            fill="#ff962e",
            outline="",
            tags="meteor"
        )



# update meteor positions

def update_meteors():
    global meteors

    for meteor in meteors:
        meteor["y"] += meteor["speed"]

    meteors = [
        meteor for meteor in meteors
        if meteor["y"] - meteor["radius"] < HEIGHT
    ]



# check whether the player hits a meteor

def check_collision():
    for meteor in meteors:
        dx = player_x - meteor["x"]
        dy = player_y - meteor["y"]

        distance = math.sqrt(dx * dx + dy * dy)

        if distance < meteor["radius"] + 12:
            return True

    return False


# display score

def draw_score():
    canvas.delete("score")

    canvas.create_text(
        20, 20,
        anchor="nw",
        text=f"SCORE: {frame * 10}",
        fill="#24f5e9",
        font=("Courier", 20, "bold"),
        tags="score"
    )
