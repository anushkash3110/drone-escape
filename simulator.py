import pygame
import math

# Initialize pygame
pygame.init()

# Screen size
WIDTH = 1000
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drone Escape Simulator")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (120, 120, 120)

clock = pygame.time.Clock()

# Drone settings
x = 150
y = 550
angle = 0

speed = 4
rotation_speed = 3

# Wall settings
wall_thickness = 20
exit_gap = 140

# Main loop control
running = True

while running:

    clock.tick(60)

    # Exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard controls
    keys = pygame.key.get_pressed()

    # Rotate left
    if keys[pygame.K_LEFT]:
        angle += rotation_speed

    # Rotate right
    if keys[pygame.K_RIGHT]:
        angle -= rotation_speed

    # Move forward
    if keys[pygame.K_UP]:
        x += math.cos(math.radians(angle)) * speed
        y -= math.sin(math.radians(angle)) * speed

    # Move backward
    if keys[pygame.K_DOWN]:
        x -= math.cos(math.radians(angle)) * speed
        y += math.sin(math.radians(angle)) * speed

    # Fill background
    screen.fill(WHITE)

    # TOP WALL with exit gap
    pygame.draw.rect(
        screen,
        BLACK,
        (0, 0, WIDTH - exit_gap, wall_thickness)
    )

    # LEFT WALL
    pygame.draw.rect(
        screen,
        BLACK,
        (0, 0, wall_thickness, HEIGHT)
    )

    # RIGHT WALL
    pygame.draw.rect(
        screen,
        BLACK,
        (WIDTH - wall_thickness, wall_thickness, wall_thickness, HEIGHT)
    )

    # BOTTOM WALL
    pygame.draw.rect(
        screen,
        BLACK,
        (0, HEIGHT - wall_thickness, WIDTH, wall_thickness)
    )

    # EXIT AREA
    pygame.draw.rect(
        screen,
        GREEN,
        (WIDTH - exit_gap, 0, exit_gap, wall_thickness)
    )

    # Cabin obstacle
    cabin = pygame.Rect(400, 250, 200, 120)
    pygame.draw.rect(screen, GRAY, cabin)

    # Drone body
    pygame.draw.circle(screen, BLUE, (int(x), int(y)), 15)

    # Direction line
    end_x = x + math.cos(math.radians(angle)) * 30
    end_y = y - math.sin(math.radians(angle)) * 30

    pygame.draw.line(
        screen,
        RED,
        (x, y),
        (end_x, end_y),
        3
    )

    # Update screen
    pygame.display.update()

pygame.quit()