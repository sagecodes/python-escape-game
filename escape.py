import random

CELLS = [(0,0), (0,1), (0,2),
         (1,0), (1,1), (1,2),
         (2,0), (2,1), (2,2)]

def get_locations():
    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or monster == start or door == start:
        return get_locations()
    return monster, door, start

def move_player(player, move):
   # get the players current location
   # if move is LEFT y - 1
   # if move is RIGHT y + 1
   # if move is UP x - 1
   # if move is DONW x + 1
    return player

def get_moves(player):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # player = to x and y

    if player[1] == 0:
        moves.remove('LEFT')
    if player[1] == 2:
        moves.remove('RIGHT')
    if player[0] == 0:
        moves.remove('UP')
    if player[0] == 2:
        moves.remove('DOWN')

    return moves


monster, door, player = get_locations()

while True:
    moves = get_moves(player)
    print("Welcome to the Dungeon!")
    print("You're currently in room {}".format(player))
    print("you can move {}".format(moves))
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

