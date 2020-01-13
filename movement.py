import doctest
from time import sleep


def get_input():
    """
    Get input from user.

    :postcondition: change user input to upper case
    :return: a str
    """
    movement = input("Pick a direction to move (N/S/E/W) or Q to quit: ").upper().strip()
    return movement


def check_quit(movement):
    """
    Check if input is "Q".

    :param movement: a str
    :precondition: a str containing one letter
    :postcondition: return boolean based on if input is "Q"
    :return: a boolean
    >>> check_quit("Q")
    True
    >>> check_quit("E")
    False
    """
    if movement == "Q":
        return True
    else:
        return False


def check_move(player, board, movement):
    """
    Check if move is valid.

    :param player: a dictionary
    :param board: a dictionary
    :param movement: a string
    :precondition player: a dictionary with key values for X-Pos and Y-Pos
    :precondition board: a dictionary with coordinates as keys
    :precondition: movement: a string
    :postcondition: determine if move is valid and return boolean
    :return: a boolean
    """
    # Get boundaries locations
    boundaries = check_boundaries(player, board)

    # Get transmat location
    transmat = check_transmat(player, board)

    # Check if input is valid
    if (movement != "N" and movement != "S" and movement != "W"
            and movement != "E"):
        if movement == "T" and transmat:
            return True
        return False

    # Check if input runs into boundaries
    if movement in boundaries:
        return False

    else:
        return True


def check_boundaries(player, board):
    """
    Get the list of boundaries from the board using player position as key.

    :param player: a dictionary
    :param board: a dictionary
    :precondition player: a dictionary with key values for X-Pos and Y-Pos
    :precondition board: a dictionary with coordinates as keys and a sub dictionary with a "Walls" key
    :postcondition: return the list of boundaries from key "Walls"
    :return: a list
    >>> board = {(0,0): {"Walls": ["N", "S"]}, (0, 1): {"Walls": ["E"]}}
    >>> player = {"X-Pos": 0, "Y-Pos": 0}
    >>> check_boundaries(player, board)
    ['N', 'S']
    """
    boundaries = board[(player["X-Pos"], player["Y-Pos"])]["Walls"]
    return boundaries


def check_transmat(player, board):
    """
    Check if player is in the same room as the transmat.

    :param player: a dictionary
    :param board: a dictionary
    :precondition player: a dictionary with key values for X-Pos and Y-Pos
    :precondition board: a dictionary with coordinates as keys and a sub dictionary with a "Transmat" key
    :postcondition: return boolean from key "Transmat"
    :return: a boolean
    >>> board = {(0,0): {"Transmat": True}, (0, 1): {"Transmat": False}}
    >>> player = {"X-Pos": 0, "Y-Pos": 0}
    >>> check_transmat(player, board)
    True
    >>> board = {(0,0): {"Transmat": True}, (0, 1): {"Transmat": False}}
    >>> player = {"X-Pos": 0, "Y-Pos": 1}
    >>> check_transmat(player, board)
    False
    """
    if board[(player["X-Pos"], player["Y-Pos"])]["Transmat"]:
        return True
    else:
        return False


def check_tardis(player, board):
    """
    Check if player is in the same room as the TARDIS.

    :param player: a dictionary
    :param board: a dictionary
    :precondition player: a dictionary with key values for X-Pos and Y-Pos
    :precondition board: a dictionary with coordinates as keys and a sub dictionary with a "TARDIS" key
    :postcondition: return boolean from key "TARDIS"
    :return: a boolean
    >>> board = {(0,0): {"TARDIS": True}, (0, 1): {"TARDIS": False}}
    >>> player = {"X-Pos": 0, "Y-Pos": 0}
    >>> check_tardis(player, board)
    True
    >>> board = {(0,0): {"TARDIS": True}, (0, 1): {"TARDIS": False}}
    >>> player = {"X-Pos": 0, "Y-Pos": 1}
    >>> check_tardis(player, board)
    False
    """
    if board[(player["X-Pos"], player["Y-Pos"])]["TARDIS"]:
        return True
    else:
        return False


def move(player, movement):
    """
    Updated player position based on movement.

    :param player: a dictionary
    :param movement: a string
    :precondition player: a dictionary with key values for X-Pos and Y-Pos
    :precondition movement: a string that contains "N", "S", "W", "E", or "T"
    :postcondition: update player dictionary with new position
    :return: a dictionary
    >>> player = {"X-Pos": 2, "Y-Pos": 2}
    >>> move(player, "N")
    {'X-Pos': 2, 'Y-Pos': 1}
    >>> player = {"X-Pos": 2, "Y-Pos": 2}
    >>> move(player, "S")
    {'X-Pos': 2, 'Y-Pos': 3}
    >>> player = {"X-Pos": 2, "Y-Pos": 2}
    >>> move(player, "W")
    {'X-Pos': 1, 'Y-Pos': 2}
    >>> player = {"X-Pos": 2, "Y-Pos": 2}
    >>> move(player, "E")
    {'X-Pos': 3, 'Y-Pos': 2}
    """
    if movement == "N":
        player["Y-Pos"] -= 1
    elif movement == "S":
        player["Y-Pos"] += 1
    elif movement == "E":
        player["X-Pos"] += 1
    elif movement == "W":
        player["X-Pos"] -= 1
    else:
        print("\n++++++++++++++++++++++++ TRANSPORTING ++++++++++++++++++++++++\n")
        sleep(2)
        player["X-Pos"] = 3
        player["Y-Pos"] = 0

    return player
