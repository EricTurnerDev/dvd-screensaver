import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

x = 0
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 2
    if x > 800:
        x = 0

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (int(x), 300), 50)
    pygame.display.flip()

pygame.quit()
