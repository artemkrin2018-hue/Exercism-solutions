"""Exercise 'All Your Base' in Exercism"""

def rebase(input_base: int, digits: list, output_base: int) -> list:

    """This function converts a sequence of digits in one base, representing a number,
    into a sequence of digits in another base, representing the same number.

    Parameters:
        input_base (int): base of a number that is being converted.
        digits (list): sequence of digits to be converted.
        output_base (int): base to be converted into.

    Returns:
        list: final sequence of digits (number) in a new system.
    """

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # проверка на одинаковые системы исчисления
    if input_base == output_base:
        return digits

    decimal_sys_nums = []
    power = len(digits) - 1

    # формула перевода из системы "X" в decimal
    for value in digits:
        num = int(value) * (input_base ** power)
        decimal_sys_nums.append(num)
        power -= 1

    # итоговое число в decimal как integer
    decimal_sys_num = sum(decimal_sys_nums)

    # итоговое число в decimal как list
    final_num_as_list = [int(i) for i in str(decimal_sys_num)]

    # проверка на decimal
    if output_base == 10:
        return final_num_as_list

    # перевод из decimal в систему "X"
    new_sys_nums = []
    num = decimal_sys_num // output_base
    remainder = decimal_sys_num % output_base
    new_sys_nums.append(remainder)
    while num > 0:
        remainder = num % output_base
        num = num // output_base
        new_sys_nums.append(remainder)

    return new_sys_nums[::-1]