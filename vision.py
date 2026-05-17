import math

def follow_line(drone, path_points):

    target_point = None

    min_distance = float("inf")

    # Find closest path point

    for point in path_points:

        px, py = point

        distance = math.sqrt(

            (px - drone.x) ** 2 +
            (py - drone.y) ** 2

        )

        if distance < min_distance:

            min_distance = distance

            target_point = point

    # Move toward point

    if target_point:

        target_x, target_y = target_point

        dx = target_x - drone.x
        dy = target_y - drone.y

        # Calculate target angle

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

        # Smooth rotation

        drone.angle += angle_difference * 0.08

        # Move drone

        drone.move()