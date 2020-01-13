from A3.ascii import print_doctor_who_logo
from A3.character import create_companion
from A3.fight import check_alive
from A3.grid_plot import print_intro, print_ending
from A3.helpers import generate_map
from A3.monster import encounter
from A3.movement import *
from time import sleep


def game_play():
    # Print logo
    print_doctor_who_logo()
    sleep(1)

    # Create player and board
    player = create_companion()
    board = generate_map(player)

    # Print game intro
    print_intro(player, board)

    # Set game conditions to false
    quit_game = False
    found_tardis = False

    # Run game
    while not quit_game:

        # Get player input
        movement = get_input()

        # Check if player wants to quit
        quit_game = check_quit(movement)

        if movement != "Q":

            # Validate movement
            if check_move(player, board, movement):

                # Move player
                move(player, movement)

                # See if player encounters a creature
                encounter(player)

                # Check if player is alive
                if not check_alive(player):
                    quit_game = True

                else:
                    # Print game story
                    print(board[(player["X-Pos"], player["Y-Pos"])]["Plot"])

                # Check if player found the TARDIS
                found_tardis = check_tardis(player, board)

                if found_tardis:
                    print_ending(player)
                    quit_game = True
            else:
                print("That's not a valid move. Choose again.\n")

    if quit_game:
        print("\n++++++++++++++++++++++++ THANK YOU FOR PLAYING ++++++++++++++++++++++++")


def main():
    game_play()


if __name__ == "__main__":
    main()
