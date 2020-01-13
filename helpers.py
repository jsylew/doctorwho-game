import random
from A3.grid_plot import *


def roll_die(number_of_rolls, number_of_sides):
    """
    Returns total of dice rolls.

    :param number_of_rolls: an int
    :param number_of_sides: an int
    :precondition: number_of_rolls must be positive ints
    :precondition: number_of_sides must be positive ints
    :postcondition: calculate the sum of number_of_rolls of a die with number_of_sides
    :return: an int
    """

    # Create empty list for rolls
    rolls = []

    # Roll die and add result to list
    for roll in range(number_of_rolls):
        rolls.append(random.randint(1, number_of_sides))

    # Return the sum of list rolls
    return sum(rolls)


def generate_map(player):
    """
    Generate game map.

    :postcondition: create a dictionary of a 5x5 grid
    :return: a dictionary
    """
    game_map = {(0, 0): grid_00(), (0, 1): grid_01(), (0, 2): grid_02(),
                (0, 3): grid_03(), (0, 4): grid_04(),
                (1, 0): grid_10(), (1, 1): grid_11(), (1, 2): grid_12(),
                (1, 3): grid_13(player), (1, 4): grid_14(),
                (2, 0): grid_20(player), (2, 1): grid_21(), (2, 2): grid_22(),
                (2, 3): grid_23(), (2, 4): grid_24(),
                (3, 0): grid_30(player), (3, 1): grid_31(), (3, 2): grid_32(),
                (3, 3): grid_33(player), (3, 4): grid_34(),
                (4, 0): grid_40(player), (4, 1): grid_41(), (4, 2): grid_42(),
                (4, 3): grid_43(), (4, 4): grid_44()}

    return game_map
