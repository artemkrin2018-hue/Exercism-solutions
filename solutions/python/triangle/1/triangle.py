def is_valid_triangle(sides) -> bool:

    if len(sides) != 3 or any(s <= 0 for s in sides):
        return False

    a, b, c = sides
    return (a + b > c) and (a + c > b) and (b + c > a)


def equilateral(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[2] == sides[0]


def scalene(sides):
    if not is_valid_triangle(sides):
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]