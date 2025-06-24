import pyglet
import random
import time

# === CONFIG ===
LOGO_WIDTH = 150
LOGO_HEIGHT = 150
SPEED = 250
COLOR_PALETTE = [
    (255, 0, 0),
    (65, 131, 196),
    (128, 255, 0)
]

# === WINDOW ===
window = pyglet.window.Window(
    fullscreen=True,
    vsync=True,
    caption="DVD Screensaver"
)
window.set_mouse_visible(False)

WINDOW_WIDTH = window.width
WINDOW_HEIGHT = window.height

# === INITIAL STATE ===
bg_color = random.choice(COLOR_PALETTE)

x = random.uniform(0, WINDOW_WIDTH - LOGO_WIDTH)
y = random.uniform(0, WINDOW_HEIGHT - LOGO_HEIGHT)

dx = random.choice([-1, 1]) * SPEED
dy = random.choice([-1, 1]) * SPEED

# === FONTS ===
dvd_label = pyglet.text.Label(
    "DVD",
    font_name='Arial Black',
    font_size=40,
    anchor_x='center',
    anchor_y='center',
    color=(0, 0, 0, 255)
)

video_label = pyglet.text.Label(
    "VIDEO",
    font_name='Arial',
    font_size=20,
    anchor_x='center',
    anchor_y='center',
    color=(255, 255, 255, 255)
)

# === RECTANGLE ===
from pyglet import shapes
logo_rect = shapes.Rectangle(
    x, y, LOGO_WIDTH, LOGO_HEIGHT, color=bg_color
)

# === FLAGS ===
startup_time = time.time()
GRACE_PERIOD = 1.0  # seconds

# === UPDATE ===
def update(dt):
    global x, y, dx, dy, bg_color

    x += dx * dt
    y += dy * dt

    hit_edge = False

    if x <= 0:
        x = 0
        dx = abs(dx)
        hit_edge = True
    elif x + LOGO_WIDTH >= WINDOW_WIDTH:
        x = WINDOW_WIDTH - LOGO_WIDTH
        dx = -abs(dx)
        hit_edge = True

    if y <= 0:
        y = 0
        dy = abs(dy)
        hit_edge = True
    elif y + LOGO_HEIGHT >= WINDOW_HEIGHT:
        y = WINDOW_HEIGHT - LOGO_HEIGHT
        dy = -abs(dy)
        hit_edge = True

    if hit_edge:
        bg_colors = [c for c in COLOR_PALETTE if c != bg_color]
        new_color = random.choice(bg_colors)
        logo_rect.color = new_color
        global bg_color
        bg_color = new_color

    logo_rect.x = x
    logo_rect.y = y

# === DRAW ===
@window.event
def on_draw():
    window.clear()
    logo_rect.draw()

    # Draw DVD label with rotation to fake italic
    dvd_label.x = x + LOGO_WIDTH // 2
    dvd_label.y = y + LOGO_HEIGHT // 2 + 15
    #dvd_label.rotation = 10  # slight slant
    dvd_label.draw()

    # Draw normal VIDEO label
    video_label.x = x + LOGO_WIDTH // 2
    video_label.y = y + LOGO_HEIGHT // 2 - 25
    video_label.draw()

# === EXIT ===
@window.event
def on_key_press(symbol, modifiers):
    window.close()

@window.event
def on_mouse_motion(x, y, dx, dy):
    if time.time() - startup_time > GRACE_PERIOD:
        window.close()

@window.event
def on_mouse_press(x, y, button, modifiers):
    window.close()

# === RUN ===
pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()
