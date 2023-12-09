from parseInput import *

def outcomeValue(dialogue):
    player1Move = dialogue[0]
    player2Move = dialogue[1]
    #WIN
    if (player2Move == 'X' and player1Move == 'C'):
        points = 6
    elif (player2Move == 'Y' and player1Move == 'A'):
        points = 6
    elif (player2Move == 'Z' and player1Move == 'B'):
        points = 6
    #LOSS
    elif (player1Move == 'A' and player2Move == 'Z'):
        points = 0
    elif (player1Move == 'B' and player2Move == 'X'):
        points = 0
    elif (player1Move == 'C' and player2Move == 'Y'):
        points = 0
    #DRAW
    else:
        points = 3

    return points

def gestureValue(move):

    if (move=='A'):
        points = 1
    elif (move=='B'):
        points = 2
    elif (move=='C'):
        points = 3
    elif (move=='X'):
        points = 1
    elif (move=='Y'):
        points = 2
    elif (move=='Z'):
        points = 3
    else:
        raise('error, this letter is unexpected')

    return points

def calcPointsForMove(dialogue):
    player2Move = dialogue[1]
    player2GesturePoints = gestureValue(player2Move)
    player2OutcomePoints = outcomeValue(dialogue)

    return player2GesturePoints + player2OutcomePoints


def calculateTotalScore(input_data):
    points_sum = 0
    for dialogue in input_data:
        player2pointsFromMove = calcPointsForMove(dialogue)
        points_sum = points_sum + player2pointsFromMove

    return points_sum

if (__name__ == "__main__"):
    input_data = parseInput()
    print(calculateTotalScore(input_data))