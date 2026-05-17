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

# Main loop
running = True

while running:

    clock.tick(60)

    # Save old position
    old_x = x
    old_y = y

    # Exit window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard input
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

    # WALLS

    # Top wall with exit gap
    top_wall = pygame.Rect(
        0,
        0,
        WIDTH - exit_gap,
        wall_thickness
    )

    # Left wall
    left_wall = pygame.Rect(
        0,
        0,
        wall_thickness,
        HEIGHT
    )

    # Right wall
    right_wall = pygame.Rect(
        WIDTH - wall_thickness,
        wall_thickness,
        wall_thickness,
        HEIGHT
    )

    # Bottom wall
    bottom_wall = pygame.Rect(
        0,
        HEIGHT - wall_thickness,
        WIDTH,
        wall_thickness
    )

    # Cabin obstacle
    cabin = pygame.Rect(
        400,
        250,
        200,
        120
    )

    # Draw walls
    pygame.draw.rect(screen, BLACK, top_wall)
    pygame.draw.rect(screen, BLACK, left_wall)
    pygame.draw.rect(screen, BLACK, right_wall)
    pygame.draw.rect(screen, BLACK, bottom_wall)

    # Draw exit
    pygame.draw.rect(
        screen,
        GREEN,
        (WIDTH - exit_gap, 0, exit_gap, wall_thickness)
    )

    # Draw cabin
    pygame.draw.rect(screen, GRAY, cabin)

    # Drone collision rectangle
    drone_rect = pygame.Rect(
        x - 15,
        y - 15,
        30,
        30
    )

    # Collision objects
    walls = [
        top_wall,
        left_wall,
        right_wall,
        bottom_wall,
        cabin
    ]

    # Collision detection
    for wall in walls:

        if drone_rect.colliderect(wall):

            x = old_x
            y = old_y

    # Draw drone
    pygame.draw.circle(
        screen,
        BLUE,
        (int(x), int(y)),
        15
    )

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