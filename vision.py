import math


current_target_index = 0


def follow_line(drone, path_points):

    global current_target_index

    if current_target_index >= len(path_points):
        return

    target_x, target_y = path_points[current_target_index]

    dx = target_x - drone.x
    dy = target_y - drone.y

    distance = math.sqrt(dx**2 + dy**2)

    # Move to next point

    if distance < 25:

        current_target_index += 1

        if current_target_index >= len(path_points):
            return

        target_x, target_y = path_points[current_target_index]

        dx = target_x - drone.x
        dy = target_y - drone.y

    # Calculate angle

    target_angle = math.degrees(
        math.atan2(-dy, dx)
    )

    angle_difference = target_angle - drone.angle

    # Normalize angle

    if angle_difference > 180:
        angle_difference -= 360

    if angle_difference < -180:
        angle_difference += 360

    # Smooth turning

    drone.angle += angle_difference * 0.07

    # Move drone

    drone.move()