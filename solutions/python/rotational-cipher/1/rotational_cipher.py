
def rotate(text: str, key: int) -> str:

    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = ""
    upper_indexes = []
    counter = 0

    for letter in text:
        if letter.isupper():
            upper_indexes.append(counter)
        counter += 1

    for value in text:

        if not value.isalpha():
            output += value

        else:

            index_number = int(eng_alphabet.find(value.lower()))

            if index_number + key < len(eng_alphabet):
                output += eng_alphabet[index_number + key]
            else:
                output += eng_alphabet[index_number + key - len(eng_alphabet)]

    for letter in output:
        if output.find(letter) in upper_indexes:
            output = output.replace(letter, letter.upper(), 1)

    return output