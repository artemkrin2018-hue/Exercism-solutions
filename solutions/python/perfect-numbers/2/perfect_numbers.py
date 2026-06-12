def classify(number: int) -> str:

    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    whole_dividers = []

    for integer in range(1, number):
        if number % integer == 0:
            whole_dividers.append(integer)

    if sum(whole_dividers) == number:
        return "perfect"
    if sum(whole_dividers) > number:
        return "abundant"
    
    return "deficient"