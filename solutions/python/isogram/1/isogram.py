
def is_isogram(string: str) -> bool:

    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"
    word_letters = []

    for letter in string.lower():
        if letter in eng_alphabet:
            word_letters.append(letter)

    no_duplicates_word_letters = set(word_letters)

    if len(no_duplicates_word_letters) == len(word_letters):
        return True

    return False