# progam to play snake and ladders
import random
pos1 = 0 #player 1 
pos2 = 0 #player 2

ladders = {14:32, 19:31, 26:48, 11:49, 56:79, 62:88, 80:98}
snakes = {17:7, 54:34, 61:42, 64:60, 87:24, 92:65 }

def move(pos):
    dice = random.randit(1,6)
    print("you have rolled ", dice)
    pos += dice
    if pos in ladders:
        print("we have found a ladder, lets move up")
        pos = ladders[pos]
    elif pos in snakes:
        print("we got bitten by snake, lets go down")
        pos = snakes[pos]
    print("new position:", pos)
    return pos


def start():

    while True:
        global pos1, pos2
        player1 = input('player1 turn\n enter "y" to continue')
        pos1 = move(pos1)
        if pos1 >= 100:
            print('player1 wins')
        break

        player2 = input('player2 turn\n enter "y" to continue')
        pos2 = move(pos2)
        if pos2 >= 100:
            print('player2 wins')
        break

        player1 = 'y' and player2 = 'y'
        print('you range quit punks')
        break

        

if __name__ == '__main__':
    start()

