import pygame
import math

from settings import *
from drone import Drone
from environment import create_environment
from vision import follow_line

pygame.init()

screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)

pygame.display.set_caption(
    "Drone Escape Simulator"
)

clock = pygame.time.Clock()

# Drone

drone = Drone()

# Environment

walls, cabin, path_points = create_environment()

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Autonomous navigation

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

    # Draw exit

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

    # Draw continuous navigation line

    pygame.draw.lines(
        screen,
        BLACK,
        False,
        path_points,
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

    # Drone direction indicator

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

    pygame.display.update()

pygame.quit()