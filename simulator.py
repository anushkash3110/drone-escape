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
    "Autonomous Drone Escape Simulator"
)

clock = pygame.time.Clock()

# Drone

drone = Drone()

# Environment

walls, cabin, fake_paths, exit_path = create_environment()

# Timer

start_time = pygame.time.get_ticks()

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Background

    screen.fill((248, 248, 248))

    # Draw walls

    for wall in walls:

        pygame.draw.rect(
            screen,
            (30, 30, 30),
            wall
        )

    # Exit opening

    pygame.draw.rect(
        screen,
        (170, 210, 170),
        (
            WIDTH - EXIT_GAP,
            0,
            EXIT_GAP,
            WALL_THICKNESS
        )
    )

    # Time

    elapsed = (
        pygame.time.get_ticks() - start_time
    ) / 1000

    # Phase 1 — Scanning

    if elapsed < 5:

        for path in fake_paths:

            pygame.draw.lines(
                screen,
                (210, 225, 210),
                False,
                path,
                3
            )

    # Phase 2 — Final path

    else:

        pygame.draw.lines(
            screen,
            (160, 190, 160),
            False,
            exit_path,
            5
        )

        # Drone follows path

        follow_line(
            drone,
            exit_path,
            walls
        )

    # Drone shadow

    pygame.draw.circle(
        screen,
        (180, 180, 180),
        (
            int(drone.x + 4),
            int(drone.y + 4)
        ),
        16
    )

    # Drone body

    pygame.draw.circle(
        screen,
        BLUE,
        (
            int(drone.x),
            int(drone.y)
        ),
        15
    )

    # Direction indicator

    end_x = drone.x + math.cos(
        math.radians(drone.angle)
    ) * 28

    end_y = drone.y - math.sin(
        math.radians(drone.angle)
    ) * 28

    pygame.draw.line(
        screen,
        RED,
        (drone.x, drone.y),
        (end_x, end_y),
        3
    )

    pygame.display.update()

pygame.quit()