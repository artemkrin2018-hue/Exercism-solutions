"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card: str) -> int | ValueError:
    """Determine the scoring value of a card.

    Parameters:
        card (str): The given card.

    Returns:
        int: The value of a given card.  See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.
    """

    match card:
        case "A":
            return 1
        case "J" | "Q" | "K":
            return 10
        case "10":
            return 10
        case "9":
            return 9
        case "8":
            return 8
        case "7":
            return 7
        case "6":
            return 6
        case "5":
            return 5
        case "4":
            return 4
        case "3":
            return 3
        case "2":
            return 2
        case _:
            return ValueError("Invalid card")


def higher_card(card_one: str, card_two: str):
    """Determine which card has a higher value in the hand.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 1
        3.  '2' - '10' = numerical value.

    Returns:
        str or tuple: The resulting tuple contains both cards if they are of equal value.
    """

    card_values = {"A": 1, "J": 10, "Q": 10, "K": 10,
                   "10": 10, "9": 9, "8": 8, "7": 7,
                   "6": 6, "5": 5, "4": 4, "3": 3,
                   "2": 2}

    if card_values[card_one] == card_values[card_two]:
        return card_one, card_two
    if card_values[card_one] > card_values[card_two]:
        return card_one
    else:
        return card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate the most advantageous value for an upcoming ace card.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        int: Either 1 or 11, which is the value of the upcoming ace card.
    """

    card_values = {"A": 11, "K": 10, "Q": 10, "J": 10,
                   "10": 10, "9": 9, "8": 8, "7": 7,
                   "6": 6, "5": 5, "4": 4, "3": 3,
                   "2": 2}

    if card_values[card_one] + card_values[card_two] <= 10:
        return 11
    else:
        return 1


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    Parameters:
        card_one (str): First card dealt in the hand.  See below for values.
        card_two (str): Second card dealt in the hand. See below for values.

        1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
        2.  'A' (ace card) = 11 (if already in hand)
        3.  '2' - '10' = numerical value.

    Returns:
        bool: Is the hand is a blackjack (two cards worth 21).
    """

    card_values = {"A": 11, "K": 10, "Q": 10, "J": 10,
                   "10": 10, "9": 9, "8": 8, "7": 7,
                   "6": 6, "5": 5, "4": 4, "3": 3,
                   "2": 2}
    
    if card_values[card_one] + card_values[card_two] == 21:
        return True
    else:
        return False


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two hands.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    
    card_values = {"A": 11, "K": 10, "Q": 10, "J": 10,
                   "10": 10, "9": 9, "8": 8, "7": 7,
                   "6": 6, "5": 5, "4": 4, "3": 3,
                   "2": 2}
    
    if card_values[card_one] == card_values[card_two] and card_one != "10" and card_two != "10":
        return True
    else:
        return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    Parameters:
        card_one (str): First card in the hand.
        card_two (str): Second card in the hand.

    Returns:
        bool: Can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    card_values = {"A": 1, "K": 10, "Q": 10, "J": 10,
                   "10": 10, "9": 9, "8": 8, "7": 7,
                   "6": 6, "5": 5, "4": 4, "3": 3,
                   "2": 2}
    
    if 9 <= card_values[card_one] + card_values[card_two] <= 11:
        return True
    else:
        return False
