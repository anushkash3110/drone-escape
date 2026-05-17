import pygame
import math

from settings import *
from drone import Drone
from environment import create_environment
from vision import follow_line

# Initialize pygame

pygame.init()

# Create window

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Drone Escape Simulator"
)

clock = pygame.time.Clock()

# Create drone

drone = Drone()

# Create environment

walls, cabin, path_points = create_environment()

# Main loop

running = True

while running:

    clock.tick(60)

    # Window close event

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Follow line

    follow_line(
        drone,
        path_points
    )

    # Background

    screen.fill(WHITE)

    # Draw walls

    for wall in walls:

        pygame.draw.rect(
            screen,
            BLACK,
            wall
        )

    # Draw exit gap

    pygame.draw.rect(
        screen,
        GREEN,
        (
            WIDTH - EXIT_GAP,
            0,
            EXIT_GAP,
            WALL_THICKNESS
        )
    )

    # Draw line guidance points

    for point in path_points:

        pygame.draw.circle(
            screen,
            GREEN,
            point,
            8
        )

    # Draw drone

    pygame.draw.circle(
        screen,
        BLUE,
        (
            int(drone.x),
            int(drone.y)
        ),
        15
    )

    # Drone direction line

    end_x = drone.x + math.cos(
        math.radians(drone.angle)
    ) * 30

    end_y = drone.y - math.sin(
        math.radians(drone.angle)
    ) * 30

    pygame.draw.line(
        screen,
        RED,
        (drone.x, drone.y),
        (end_x, end_y),
        3
    )

    # Update display

    pygame.display.update()

# Quit pygame

pygame.quit()