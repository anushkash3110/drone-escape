import random

def autonomous_navigation(drone, walls):

    drone.move()

    drone_rect = drone.get_rect()

    for wall in walls:

        if drone_rect.colliderect(wall):

            drone.rotate(
                random.randint(90, 180)
            )