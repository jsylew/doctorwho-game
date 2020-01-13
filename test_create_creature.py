from unittest import TestCase
from unittest.mock import patch

from A3.monster import *


class TestCreate_creature(TestCase):
    @patch("A3.monster.roll_die", return_value=6)
    def test_create_creature(self, mock_roll):
        cyberman = {"Name": ["CYBERMAN"], "HP": 5, "Catchphrase": "The Cyberman said, 'You. Will. Be. Upgraded.'",
                    "Description": "A coldly logical and calculating cyborg, the emotionless +\
                     Cyberman wants to convert you into their ranks."}

        dalek = {"Name": ["DALEK"], "HP": 5, "Catchphrase": "The Dalek screamed, 'EXTERMINATE!'",
                 "Description": "The Doctor's greatest enemy. Violent, merciless and pitiless +\
                 mutant creatures who live in mobile armour, there is no reasoning with a Dalek."}

        silence = {"Name": ["SILENCE"], "HP": 5, "Catchphrase": "** Stares at you expressionlessly **",
                   "Description": "A rogue group of confessional priests under a splinter group +\
                  the Silence cannot be remembered unless they are being looked at."}

        silurian = {"Name": ["SILURIAN"], "HP": 5, "Catchphrase": "The Silurian scoffed, 'Apes.'",
                    "Description": "The original inhabitants of Earth, these scientifically +\
                   advanced reptilian humanoids want their planet back after a long hibernation."}

        sontaran = {"Name": ["SONTARAN"], "HP": 5, "Catchphrase": "The Sontaran chanted, 'SONTAR-HA!",
                    "Description": "Ruthless and fearless, the militaristic Sontarans sees dying in battle +\
                    as their ultimate goal"}

        weeping_angel = {"Name": ["WEEPING ANGEL"], "HP": 5,
                         "Description": "The deadliest, most malevolent life-form, the Weeping Angels move +\
                         quickly and silently only when they are not observed by another being. Don't blink."}

        zygon = {"Name": "Zygon", "HP": 5,
                 "Description": "A shape-shifting race, the Zygon can replicate the appearance of another being."}

        creatures = {1: cyberman, 2: dalek, 3: silence, 4: silurian, 5: sontaran, 6: weeping_angel, 7: zygon}
        self.assertEqual(create_creature()["Name"][0], weeping_angel["Name"][0])
