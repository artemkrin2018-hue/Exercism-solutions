import math

def score(x: float, y: float) -> float:

    x = abs(x)
    y = abs(y)

    outer_circle_radius = 10.00
    middle_circle_radius = 5.00
    inner_circle_radius = 1.00

    distance_squared = (pow(x, 2) + pow(y, 2))
    distance_from_zero = math.sqrt(distance_squared)

    if distance_from_zero > outer_circle_radius:
        return 0
    if middle_circle_radius < distance_from_zero <= outer_circle_radius:
        return 1
    if inner_circle_radius < distance_from_zero <= middle_circle_radius:
        return 5
    else:
        return 10