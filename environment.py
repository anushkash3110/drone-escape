import pygame
from settings import *


def create_environment():

    # Walls

    top_wall = pygame.Rect(
        0,
        0,
        WIDTH - EXIT_GAP,
        WALL_THICKNESS
    )

    left_wall = pygame.Rect(
        0,
        0,
        WALL_THICKNESS,
        HEIGHT
    )

    right_wall = pygame.Rect(
        WIDTH - WALL_THICKNESS,
        WALL_THICKNESS,
        WALL_THICKNESS,
        HEIGHT
    )

    bottom_wall = pygame.Rect(
        0,
        HEIGHT - WALL_THICKNESS,
        WIDTH,
        WALL_THICKNESS
    )

    # Center obstacle

    cabin = pygame.Rect(
        380,
        250,
        220,
        140
    )

    walls = [
        top_wall,
        left_wall,
        right_wall,
        bottom_wall,
        cabin
    ]

    # Fake scanning paths

    fake_paths = [

        [(150, 560), (200, 530), (260, 500)],

        [(150, 560), (170, 470), (200, 390)],

        [(150, 560), (260, 560), (360, 560)],

        [(150, 560), (240, 520), (340, 460)],

        [(150, 560), (300, 560), (360, 520)],

    ]

    # Correct exit path

    exit_path = [

    # Start

    (150, 560),
    (240, 560),
    (320, 560),

    # Move upward

    (320, 500),
    (320, 420),

    # Move beside obstacle

    (320, 220),

    # Curve toward exit

    (420, 170),
    (560, 130),

    (720, 100),
    (860, 80),

    # Fully outside room

    (1040, -40)
]

    return walls, cabin, fake_paths, exit_path