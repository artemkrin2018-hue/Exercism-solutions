def square(number: int):
    if 0 < number < 65:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    nums = []
    for x in range(1, 65):
        nums.append(2 ** (x - 1))
    f_amount = 0
    for num in nums:
        f_amount += num
    return f_amount