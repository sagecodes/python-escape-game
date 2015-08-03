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
    #player = (x,y)
    x, y = player

    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        y -= 1
    elif move == 'DOWN':
        y += 1

    return x, y

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

    if move in moves:
        player = move_player(player, move)
    else:
        print("You run in to a wall. You'll have to go another direction...")
        continue

    if player == door:
        print("You push up against a door, it opens! You've escaped!")
        break
    elif player == monster:
        print("A foul stench fills your lungs, as your head is crushed by the mighty minotaur")
        break







