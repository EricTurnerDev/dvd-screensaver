import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Fullscreen display
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
#screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED, vsync=1)
#screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)

pygame.display.set_caption("DVD Screensaver")

# Hide the mouse cursor
pygame.mouse.set_visible(False)

# Logo dimensions (more square-like)
logo_width, logo_height = 150, 100

# Fonts
pygame.font.init()
font_large = pygame.font.SysFont(['Arial Black', 'Arial', 'Sans'], 50, bold=True)
font_small = pygame.font.SysFont(['Arial', 'Sans'], 20, bold=True)

COLOR_PALETTE = [
    (255, 0, 0),      # Red
    (0, 255, 0),      # Green
    (65, 131, 196),   # Blue-ish
    #(0, 0, 255),      # Blue
    #(255, 255, 0),    # Yellow
    #(255, 0, 255),    # Magenta
    #(0, 255, 255),    # Cyan
    #(255, 128, 0),    # Orange
    #(128, 0, 255),    # Purple
    (128, 255, 0)     # Lime
]

# Initial background color
bg_color = random.choice(COLOR_PALETTE)

# Create the logo Surface
logo = pygame.Surface((logo_width, logo_height), pygame.SRCALPHA)

# Initial position (use floats for smooth motion)
x = float(random.randint(0, WIDTH - logo_width))
y = float(random.randint(0, HEIGHT - logo_height))

# Speed in pixels per second
speed_x = random.choice([-1, 1]) * 250  # slightly slower for realism
speed_y = random.choice([-1, 1]) * 250

# Store initial mouse position
prev_mouse_pos = pygame.mouse.get_pos()

clock = pygame.time.Clock()
prev_time = time.time()

running = True
while running:
    # Delta time in seconds
    current_time = time.time()
    dt = current_time - prev_time
    prev_time = current_time

    # Limit FPS
    clock.tick(120)

    # Check mouse movement
    current_mouse_pos = pygame.mouse.get_pos()
    if current_mouse_pos != prev_mouse_pos:
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            running = False

    # Move with delta time
    x += speed_x * dt
    y += speed_y * dt

    hit_corner = False

    if x <= 0:
        x = 0
        speed_x = abs(speed_x)
        hit_corner = True
    elif x + logo_width >= WIDTH:
        x = WIDTH - logo_width
        speed_x = -abs(speed_x)
        hit_corner = True

    if y <= 0:
        y = 0
        speed_y = abs(speed_y)
        hit_corner = True
    elif y + logo_height >= HEIGHT:
        y = HEIGHT - logo_height
        speed_y = -abs(speed_y)
        hit_corner = True

    if hit_corner:
        bg_color = random.choice(COLOR_PALETTE)

    # Draw the logo
    logo.fill((0, 0, 0, 0))
    pygame.draw.rect(logo, bg_color, (0, 0, logo_width, logo_height), border_radius=12)

    text_dvd = font_large.render("DVD", True, (0, 0, 0))
    text_video = font_small.render("VIDEO", True, (255, 255, 255))

    # Position: DVD upper center, VIDEO just below
    logo.blit(text_dvd, text_dvd.get_rect(center=(logo_width // 2, logo_height // 2 - 15)))
    logo.blit(text_video, text_video.get_rect(center=(logo_width // 2, logo_height // 2 + 25)))

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(logo, (round(x), round(y)))
    pygame.display.flip()

pygame.quit()
sys.exit()
