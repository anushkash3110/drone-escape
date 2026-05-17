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

    # Cabin obstacle

    cabin = pygame.Rect(
        400,
        250,
        200,
        120
    )

    # Collision objects

    walls = [
        top_wall,
        left_wall,
        right_wall,
        bottom_wall,
        cabin
    ]

    # Line guidance path

    path_points = [

        (180, 550),
        (250, 550),

        (320, 520),
        (380, 470),

        (430, 420),

        (500, 420),
        (600, 380),

        (700, 300),

        (780, 220),
        (850, 140),

        (920, 60)
    ]

    return walls, cabin, path_points