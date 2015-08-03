import random

CELLS = [(0,0), (0,1), (0,2),
         (1,0), (1,1), (1,2),
         (2,0), (2,1), (2,2)]

def get_locations():
    # monster = random
    # door = random
    # start = random

    # if monster, door or start are the same, do it again

    # return monster, door, start
def move_player(player, move):
   # get the players current location
   # if move is LEFT y - 1
   # if move is RIGHT y + 1
   # if move is UP x - 1
   # if move is DONW x + 1
    return player

def get_moves(player):
    MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # if players y is 0 remove LEFT
    # if players x is zero remove UP
    # if players y is 2 remove right
    # if players x is 2 remove DOWN
    return MOVES

while True:
    print("Welcome to the Dungeon!")
    print("You're currently in room {}") # fill in with player position
    print("you can move {}") # fill in with available moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = movie.upper()

    if move == 'QUIT':
        break

    # If its a valid move, change the players position
    # if its not a valid move do not change position. Provide feedback
    # if if the new position is the door, they win!
    # if the new player position is the monster they lose!
    # otherwise, continue

