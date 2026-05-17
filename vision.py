import math

current_target_index = 0

def follow_line(drone, exit_path, walls):

    global current_target_index

    if current_target_index >= len(exit_path):
        return

    target_x, target_y = exit_path[current_target_index]

    dx = target_x - drone.x
    dy = target_y - drone.y

    distance = math.sqrt(dx**2 + dy**2)

    # Go to next point

    if distance < 20:

        current_target_index += 1

        if current_target_index >= len(exit_path):
            return

        target_x, target_y = exit_path[current_target_index]

        dx = target_x - drone.x
        dy = target_y - drone.y

    # Target angle

    target_angle = math.degrees(
        math.atan2(-dy, dx)
    )

    angle_difference = (
        target_angle - drone.angle
    )

    # Normalize angle

    if angle_difference > 180:
        angle_difference -= 360

    if angle_difference < -180:
        angle_difference += 360

    # Very smooth turning

    drone.angle += angle_difference * 0.04

    # Smooth slow speed

    drone.speed = 1.5

    # Save old position

    old_x = drone.x
    old_y = drone.y

    # Move

    drone.move()

    drone_rect = drone.get_rect()

    # Collision handling

    for wall in walls:

        if drone_rect.colliderect(wall):

            # Soft recovery

            drone.x = old_x
            drone.y = old_y

            # Slight angle correction

            drone.angle += 2