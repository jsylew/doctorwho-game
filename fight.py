from A3.helpers import roll_die
from time import sleep


def who_attacks(player, creature):
    """
    Determines who attacks first.

    :param player: a dictionary
    :param creature: a dictionary
    :precondition player: a dictionary
    :precondition creature: a dictionary
    :postcondition: return player and creature in order determined by die rolls
    :return: two dictionaries
    """
    # Roll to see who attacks first
    player_roll = roll_die(1, 6)
    creature_roll = roll_die(1, 6)

    # Return player and creature in order of attacker and defender
    if player_roll > creature_roll:
        print(f"{player['Name'][0]} attacks.")
        return player, creature

    else:
        print(f"{creature['Name'][0]} attacks.")
        return creature, player


def check_alive(player_or_creature):
    """
    Check if HP is higher than 0.

    :param player_or_creature: a dictionary
    :precondition: a dictionary with key "HP" and a numeric value
    :postcondition: determine if player_or_creature is alive
    :return: a boolean
    >>> player = {"HP": 5}
    >>> check_alive(player)
    True
    >>> player = {"HP": 0}
    >>> check_alive(player)
    False
    """
    # Check HP value
    if player_or_creature["HP"] > 0:
        return True
    else:
        return False


def hit_or_miss(attacker):
    """
    Determines if attacker hits or misses.

    :param attacker: a dictionary
    :precondition attacker: a dictionary with correct key values
    :postcondition: if hit roll is higher than defend roll, return True
    :return: a boolean
    """
    # See if hit lands
    hit = roll_die(1, 6)
    defend = roll_die(1, 6)

    if hit > defend:
        print(f"{attacker['Name'][0]}'s hit lands.\n")
        return True
    else:
        print(f"{attacker['Name'][0]} misses.\n")
        return False


def calc_damage():
    """
    Calculate how much damage is done.

    :postcondition: return result of die roll
    :return: an int
    """
    damage = roll_die(1, 6)
    return damage


def fight(player, creature):
    """
    Run combat sequence.

    :param player: a dictionary
    :param creature: a dictionary
    :precondition player: a dictionary with correct key values
    :precondition creature: a dictionary with correct key values
    :postcondition: update player dictionary with new HP value
    :return: a dictionary
    """
    print("\n++++++++++++++++++++++++ FIGHT ++++++++++++++++++++++++\n")

    # Loop combat until player or creature dies
    while check_alive(player) and check_alive(creature):

        # Determine who attacks
        attacker, defender = who_attacks(player, creature)

        # If hit lands, minus HP from defender
        if hit_or_miss(attacker):
            defender["HP"] -= calc_damage()

        sleep(1.5)

    # Once loop ends, check who's alive and print message
    if not check_alive(creature):
        print(f"{player['Name'][0]} defeated the {creature['Name'][0]}.")
        return player
    else:
        print(creature["Catchphrase"])
        print(f"{player['Name'][0]} was defeated by the {creature['Name'][0]}.")
        return player


def flight(player):
    """
    Determines if player successfully runs away.

    :param player: a dictionary
    :precondition player: a dictionary with a key "HP"
    :postcondition: update player "HP value if unsuccessful and hit
    :return: a dictionary
    """
    # Roll to see if successfully run away
    success = roll_die(1, 10)

    # If roll is 5, get stabbed in back
    if success == 5:
        damage = roll_die(1, 4)
        player["HP"] -= damage
        print(f"\n{player['Name'][0]} got injured as they ran away and suffered {damage} damage.\n")

    # Otherwise, no damage
    else:
        print(f"\n{player['Name'][0]} successfully escaped.\n")

    return player


def fight_or_flight(player, creature):
    """
    Get user choice on fighting or running away.

    :param player: a dictionary
    :param creature: a dictionary
    :precondition player: a dictionary with correct key values
    :precondition creature: a dictionary with correct key values
    :return: a boolean
    """
    player_move = False
    print(f"\n{player['Name'][0]} sees a {creature['Name'][0]} in front!\n"
          f"{creature['Description']}\n\nWhat to do?\n")

    # Loop until correct input
    while not player_move:
        # Get input on fight or run
        decision = input(f"Will {player['Name'][0]} FIGHT or RUN? ").upper().strip()

        if decision == "FIGHT":
            fight(player, creature)
            player_move = True

        elif decision == "RUN":
            flight(player)
            player_move = True

        else:
            print("\nThat's not a valid move. Enter FIGHT or RUN to continue.")
