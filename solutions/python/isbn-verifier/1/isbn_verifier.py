
def is_valid(isbn: str) -> bool:

    formated_isbn = isbn.replace("-", "")

    if len(formated_isbn) != 10:
        return False

    allowed_symbols = "1234567890X"

    for value in formated_isbn:
        if value.upper() not in allowed_symbols:
            return False

    isbn_values = [str(value) for value in formated_isbn]

    for value in isbn_values[0:9:]:
        if value.upper() == "X":
            return False

    if isbn_values[9] == "X":
        isbn_values[9] = "10"

    value_counter = 0
    multiplier_counter = 10
    final_number = 0

    for value in isbn_values:
        number = int(isbn_values[value_counter]) * multiplier_counter
        value_counter += 1
        multiplier_counter -= 1
        final_number += number

    if final_number % 11 == 0:
        return True

    return False