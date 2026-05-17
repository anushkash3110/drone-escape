import pygame
import math
import random

class Drone:

    def __init__(self):

        self.x = 150
        self.y = 550

        self.angle = 0

        self.speed = 4

    def move(self):

        self.x += math.cos(math.radians(self.angle)) * self.speed
        self.y -= math.sin(math.radians(self.angle)) * self.speed

    def rotate_random(self):

        self.angle += random.randint(90, 180)

    def get_rect(self):

        return pygame.Rect(
            self.x - 15,
            self.y - 15,
            30,
            30
        )