from A3.ascii import return_tardis
from time import sleep


def print_intro(player, board):
    """
    Print game story intro.

    :param player: a dictionary
    :param board: a dictionary
    :precondition player: a dictionary with the key Name
    :precondition board: a dictionary with the key (0,4) to a sub-dictionary with key Plot
    :postcondition: print out the story game intro
    :return: print statements
    """
    print(f'\n+++++++++++++++++++++++ DOCTOR WHO ADVENTURE: THE MISSING TARDIS +++++++++++++++++++++++\n')
    print(f'"Doctor, this doesn\'t feel right," {player["Name"][0]} said hesitantly, "Are'
          f' you sure we should be here? \nThe TARIDS really didn\'t want to land just now."'
          f' "The old girl is just being temperamental, {player["Name"][0]}. \nDon\'t worry,"'
          f' the DOCTOR said nonchalantly as he fiddled with the monitors at'
          f' the console. \n"The note sent to the psychic paper was from an old friend. '
          f'We are just going to pop by,\nhelp him out, and be back in'
          f' time for tea at Space Florida!" he continued \nas he sauntered out the TARDIS.\n')
    sleep(2)
    print(f'"I thought we were going swimming at Poosh!" {player["Name"][0]} yelled as'
          f' they followed the DOCTOR out the door. \nThe TARDIS doors slammed shut '
          f'behind {player["Name"][0]}, and the unmistakable sound of the TARDIS \n'
          f'dematerialising was heard. The DOCTOR and {player["Name"][0]} could only stare'
          f' as the TARDIS disappeared from view.\n')
    sleep(2)
    print(f'Before the DOCTOR could say anything, the two heard the unmistakable screams of "EX-TER-MIN-ATE" \n'
          f'from down the hall. They quickly looked at each other, "RUN!"\n')
    sleep(2)
    print(f'"{player["Name"][0]}, go find the TARDIS, she\'ll protect you!" the DOCTOR whispered quickly\n'
          f'and ran off. "DOCTOR! Wait!" {player["Name"][0]} angrily grumbled, "Damn he runs fast."\n'
          f'Hopefully they don\'t run into any monster as they look for that blue police box.\n')
    sleep(2)
    print(board[(0, 4)]["Plot"])


def grid_00():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "W"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe writings on some of these blueprints look Gallifreyan. Could it be the Master?\n"
                    "Is he crazy enough to help the DALEKS and others build a TARDIS?\n"
                    "The room continues to the SOUTH and EAST.\n"}
    return plot


def grid_01():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["S", "W", "E"], "TARDIS": False, "Transmat": False,
            "Plot": "\nMore junk parts. Nothing new.\n"}
    return plot


def grid_02():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "S", "W"], "TARDIS": False, "Transmat": False,
            "Plot": "\nJust a broom closet. Nothing useful. There is a door to the EAST.\n"}
    return plot


def grid_03():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "S", "W"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe room is filled with sleeping SILENCE hanging from the ceiling. \n"
                    "Should probably back out the door to the EAST before they wake up.\n"}
    return plot


def grid_04():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "S", "W"], "TARDIS": False, "Transmat": False,
            "Plot": f'\nEerie blue lights lit the cold corridors. To the NORTH, SOUTH, and WEST are solid metal walls.\n'}
    return plot


def grid_10():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "S"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThere are bits and pieces of machinery lying around. Images of the TARDIS,\n"
                    "and what looks like blueprints covered the walls. Are they trying to make \n"
                    "their own TARDIS? The room continues to the WEST. The door is to the EAST.\n"}
    return plot


def grid_11():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "W"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe corridor continues to the EAST and SOUTH. The walls to the WEST and NORTH\n"
                    "sounds hollow, maybe there is something behind them?\n"}
    return plot


def grid_12():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["E"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe corridor continues to the NORTH and SOUTH, and there is a door to the WEST.\n"}
    return plot


def grid_13(player):
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["E"], "TARDIS": False, "Transmat": False,
            "Plot": f"\nFeeling their way through the dim corridor, {player['Name'][0]} "
                    f"finds a secret door to the WEST. \nThe corridor continues to the NORTH, "
                    f"and there is a door to the SOUTH.\n"}
    return plot


def grid_14():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["S", "E"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThere are walls to the EAST and SOUTH, and a door to the NORTH.\n"}
    return plot


def grid_20(player):
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "E"], "TARDIS": False, "Transmat": False,
            "Plot": f"\nThe wall to the WEST sounded hollow, and after a few minutes of feeling\n"
                    f"around, {player['Name'][0]} finds the switch to open the door to the WEST.\n"
                    f"A faint mechanical sound can be heard through the wall to the EAST.\n"}
    return plot


def grid_21():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["S"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe corridor continues to the NORTH, WEST, and EAST. This place is \n"
                    "too exposed, best move along.\n"}
    return plot


def grid_22():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "W", "E"], "TARDIS": False, "Transmat": False,
            "Plot": "\nNothing at this end of the room. The sound got fainter.\n"}
    return plot


def grid_23():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["W"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe humming sound is a little clearer now. Definitely not the TARIDS's\n"
                    "familiar noise. What could it be? The room continues to the NORTH and SOUTH.\n"}
    return plot


def grid_24():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["S", "W"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe humming got a little louder. The room continues to the NORTH and EAST.\n\n"}
    return plot


def grid_30(player):
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "S", "W"], "TARDIS": False, "Transmat": False,
            "Plot": f"\nThe TRANSMAT transported {player['Name'][0]} into yet another dark room.\n"
                    f"What's that light to the EAST?\n"}
    return plot


def grid_31():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "E"], "TARDIS": False, "Transmat": False,
            "Plot": "\nThe faint hum of machinery can be heard through the wall to the NORTH\n"
                    "It doesn\'t sound like the TARDIS, but maybe it is something useful?\n"
                    "There is a door to the SOUTH.\n"}
    return plot


def grid_32():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["W"], "TARDIS": False, "Transmat": False,
            "Plot": "\nSmoke and sparks filled the room. The DOCTOR must have been here\n"
                    "Only he can create such chaos. It\'s hard to see, but the room continues\n"
                    "to the SOUTH and EAST.\n"}
    return plot


def grid_33(player):
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["S"], "TARDIS": False, "Transmat": False,
            "Plot": f"\nThere\'s a faint hum of machinery through the SOUTH wall. Feeling their\n"
                    f"way through the smoke, {player['Name'][0]} finds a switch to a hidden "
                    f"door to the WEST.\n"}
    return plot


def grid_34():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "S"], "TARDIS": False, "Transmat": True,
            "Plot": "\nThe humming was coming from a TRANSMAT! Where does it lead to?\n"
                    "// Enter T to use the TRANSMAT // The room continues to the WEST and EAST.\n"}
    return plot


def grid_40(player):
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "E"], "TARDIS": True, "Transmat": False,
            "Plot": return_tardis() + f"\n\nThat blue police box has never looked so "
                                      f"beautiful. {player['Name'][0]} ran as fast as "
                                      f"\nthey could into the TARDIS. Hopefully the DOCTOR is already in there.\n"}
    return plot


def grid_41():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["S", "W", "E"], "TARDIS": False, "Transmat": False, "Plot": ""}
    return plot


def grid_42():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "E"], "TARDIS": False, "Transmat": False,
            "Plot": "More smoke and sparks. The room continues to the WEST and SOUTH.\n"}
    return plot


def grid_43():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["S", "E"], "TARDIS": False, "Transmat": False,
            "Plot": "There are more cut wires and blinking lights on this side of the room.\n"
                    "Hopefully the DOCTOR got out ok. Best find the TARDIS soon.\n"}
    return plot


def grid_44():
    """
    Create dictionary for a section of the game board.

    :postcondition: a dictionary with correct key values
    :return: a dictionary
    """
    plot = {"Walls": ["N", "S", "E"], "TARDIS": False, "Transmat": False,
            "Plot": "Nothing interesting at this end of the room.\n"}
    return plot


def print_ending(player):
    """
    Print game story intro.

    :param player: a dictionary
    :precondition player: a dictionary with the key Name
    :postcondition: print out the story game ending
    :return: print statements
    """
    print(f'"{player["Name"][0]}! Finally! What took you so long?!" the DOCTOR exclaimed as '
          f'soon as \n{player["Name"][0]} ran into the TARDIS. Before they can even open their mouth '
          f'to respond, \nhe continued, "Nevermind. We need to get a move on. I locked the MASTER\n'
          f'in a deadlock sealed room, but that won\'t stop him for long."\n\n'
          f'"So the MASTER is involved?"\n\n'
          f'"Yes, {player["Name"][0]}. Keep up. He gathered all my enemies together and promised\n'
          f'them their own TARDIS if they follow his lead in setting this trap for me.\n'
          f'Of course it was all a lie. Even the MASTER can\'t build a TARDIS from scratch.\n'
          f'Even I can\'t do that."')
    sleep(2)
    print(f'{player["Name"][0]} rolled their eyes, "So what now?"\n\n'
          f'"I think we can still make it for tea at Barcelona," the DOCTOR said, already running around\n'
          f'the TARDIS console like a mad man.\n\n'
          f'"I thought it was tea at Space Florida? But nevermind that! You promised we would\n'
          f'go swimming at Poosh!"\n\n')
