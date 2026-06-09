def convert(number: int):

    final_answer = []

    if number % 3 == 0:
        sound1 = "Pling"
        final_answer.append(sound1)
    else:
        pass

    if number % 5 == 0:
        sound2 = "Plang"
        final_answer.append(sound2)
    else:
        pass

    if number % 7 == 0:
        sound3 = "Plong"
        final_answer.append(sound3)
    else:
        pass

    if len(final_answer) == 0:
        return str(number)
    else:
        final_sound = ""
        for sound in final_answer:
            final_sound += sound
        return final_sound