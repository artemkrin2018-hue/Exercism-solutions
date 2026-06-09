def steps(number: int) -> int:

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    operations = 0

    while number != 1:
        if number % 2 == 0:
            number = number // 2
            operations += 1
        elif number % 2 == 1:
            number = number * 3 + 1
            operations += 1

    return operations