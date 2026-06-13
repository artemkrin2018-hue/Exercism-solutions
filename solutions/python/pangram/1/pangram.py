def is_pangram(sentence):

    eng_alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in eng_alphabet:
        if letter not in sentence.lower():
            return False

    return True