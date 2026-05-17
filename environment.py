import pygame
from settings import *

def create_environment():

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

    cabin = pygame.Rect(
        400,
        250,
        200,
        120
    )

    walls = [
        top_wall,
        left_wall,
        right_wall,
        bottom_wall,
        cabin
    ]

    return walls, cabin