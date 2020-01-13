from A3.helpers import roll_die
from A3.fight import fight_or_flight


def create_creature():
    """
    Determine a random creature from list.

    :return: a dictionary
    """
    # Declare list of creatures

    cyberman = {"Name": ["CYBERMAN"], "HP": 5, "Catchphrase": "The CYBERMAN said, 'You. Will. Be. Upgraded.'",
                "Description": "A coldly logical and calculating cyborg, the emotionless Cyberman wants to convert "
                               "you into their ranks."}

    dalek = {"Name": ["DALEK"], "HP": 5, "Catchphrase": "The DALEK screamed, 'EXTERMINATE!'",
             "Description": "The Doctor's greatest enemy. Violent, merciless and pitiless mutant creatures who live "
                            "in mobile armour, there is no reasoning with a Dalek."}

    silence = {"Name": ["SILENCE"], "HP": 5, "Catchphrase": "** Stares expressionlessly **",
               "Description": "A rogue group of confessional priests under a splinter group the Silence cannot be "
                              "remembered unless they are being looked at."}

    silurian = {"Name": ["SILURIAN"], "HP": 5, "Catchphrase": "The SILURIAN scoffed, 'Apes.'",
                "Description": "The original inhabitants of Earth, these scientifically advanced reptilian humanoids "
                               "want their planet back after a long hibernation."}

    sontaran = {"Name": ["SONTARAN"], "HP": 5, "Catchphrase": "The SONTARAN chanted, 'SONTAR-HA!",
                "Description": "Ruthless and fearless, the militaristic Sontarans sees dying in battle as their "
                               "ultimate goal"}

    weeping_angel = {"Name": ["WEEPING ANGEL"], "HP": 5, "Catchphrase": "The WEEPING ANGEL reaches out.",
                     "Description": "The deadliest, most malevolent life-form, the Weeping Angels move quickly and "
                                    "silently only when they are not observed by another being. Don't blink."}

    creatures = {1: cyberman, 2: dalek, 3: silence, 4: silurian, 5: sontaran, 6: weeping_angel}

    # Roll to select creature
    roll = roll_die(1, 6)

    return creatures[roll]


def encounter(player):
    """
    Determines if player encounters a monster.

    :param player: a dictionary
    :precondition player: a dictionary with correct key values
    :postcondition: move player to fight or flight or increase HP
    :return: nothing or player with updated HP
    """
    roll = roll_die(1, 4)

    if roll == 3:
        creature = create_creature()
        fight_or_flight(player, creature)

    else:
        if player["HP"] <= 8:
            player["HP"] += 2
        elif player["HP"] == 9:
            player["HP"] += 1
        return player

