def is_armstrong_number(number):
    str_number = str(number)
    nums_list = []
    for digit in str_number:
        result = int(digit) ** len(str_number)
        nums_list.append(result)
    if sum(nums_list) == number:
        return True
    else:
        return False