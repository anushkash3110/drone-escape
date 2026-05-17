import pygame

from settings import *
from drone import Drone
from environment import create_environment
from navigation import autonomous_navigation

pygame.init()

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
walls, cabin = create_environment()

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Autonomous movement
    autonomous_navigation(
        drone,
        walls
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

    # Direction line
    import math

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