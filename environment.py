import pygame

from settings import *

def create_environment():

    # Top wall

    top_wall = pygame.Rect(
        0,
        0,
        WIDTH - EXIT_GAP,
        WALL_THICKNESS
    )

    # Left wall

    left_wall = pygame.Rect(
        0,
        0,
        WALL_THICKNESS,
        HEIGHT
    )

    # Right wall

    right_wall = pygame.Rect(
        WIDTH - WALL_THICKNESS,
        WALL_THICKNESS,
        WALL_THICKNESS,
        HEIGHT
    )

    # Bottom wall

    bottom_wall = pygame.Rect(
        0,
        HEIGHT - WALL_THICKNESS,
        WIDTH,
        WALL_THICKNESS
    )

    # Center cabin obstacle

    cabin = pygame.Rect(
        380,
        250,
        220,
        140
    )

    # Collision objects

    walls = [
        top_wall,
        left_wall,
        right_wall,
        bottom_wall,
        cabin
    ]

    # Navigation path

    path_points = [

        (150, 560),
        (220, 560),
        (300, 560),

        (360, 520),
        (360, 450),

        (360, 400),
        (360, 330),

        (650, 330),

        (760, 260),
        (850, 180),

        (920, 80)
    ]

    return walls, cabin, path_points