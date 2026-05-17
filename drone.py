import pygame
import math

class Drone:

    def __init__(self):

        self.x = 150
        self.y = 550

        self.angle = 0

        self.speed = 4

    def move(self):

        self.x += math.cos(
            math.radians(self.angle)
        ) * self.speed

        self.y -= math.sin(
            math.radians(self.angle)
        ) * self.speed

    def rotate(self, amount):

        self.angle += amount

    def get_rect(self):

        return pygame.Rect(
            self.x - 15,
            self.y - 15,
            30,
            30
        )