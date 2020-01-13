def choose_companion():
    """
    Get user choice of companion.

    :postcondition: return user choice
    :return: a string
    """
    # Declare list of companions
    companions = ["Amy Pond", "Clara Oswald", "Donna Noble", "Jack Harkness", "Martha Jones",
                  "River Song", "Rory Williams", "Rose Tyler"]

    # Print empty line for formatting
    print()

    print("In this game, you will play as one of the Doctor's past companions.\nWho do you want to play as?\n")

    # Print list of companions
    for number in range(0, len(companions)):
        print(str(number + 1) + ".\t", companions[number])

    # Print empty line for formatting
    print()

    player_choice = int(input("Enter the number of the companion of your choice: "))
    character = companions[player_choice - 1].upper()

    return character


def create_companion():
    """
    Generate companion dictionary.

    :postcondition: dictionary with chosen companion name
    :return: a dictionary
    """
    character = {"Name": choose_companion().split(None, 1), "HP": 10, "X-Pos": 0, "Y-Pos": 4}

    return character
