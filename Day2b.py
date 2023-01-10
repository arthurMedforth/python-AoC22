from parseInput import *

def getGesturePoints(player1Gesture, requiredOutcome):

    if (player1Gesture=='A'):
        if (requiredOutcome=='Win'):
            # Paper needed
            points = 2

        elif (requiredOutcome == 'Draw'):
            # Rock needed
            points = 1

        elif (requiredOutcome == 'Loss'):
            # Scissors needed
            points = 3

        else:
            raise('unknown outcome')
            
    elif (player1Gesture=='B'):
        if (requiredOutcome=='Win'):
            # Scissors needed
            points = 3
            
        elif (requiredOutcome == 'Draw'):
            # Paper needed
            points = 2

        elif (requiredOutcome == 'Loss'):
            # Rock needed
            points = 1

        else:
            raise('unknown outcome')

    elif (player1Gesture=='C'):
        if (requiredOutcome=='Win'):
            # Rock needed
            points = 1

        elif (requiredOutcome == 'Draw'):
            # Scissors needed
            points = 3

        elif (requiredOutcome == 'Loss'):
            # Paper needed
            points = 2

        else:
            raise('unknown outcome')

    else:
        raise('unexpected input')

    return points

def calcPointsForMove(dialogue):
    player1Move = dialogue[0]
    player2DesiredOutcome = dialogue[1]

    # WIN condition
    if (player2DesiredOutcome == 'X'):
        outcomePoints = 0
        gesturePoints = getGesturePoints(player1Move,'Loss')

    elif (player2DesiredOutcome == 'Y'):
        outcomePoints = 3
        gesturePoints = getGesturePoints(player1Move,'Draw')


    elif (player2DesiredOutcome == 'Z'):
        outcomePoints = 6
        gesturePoints = getGesturePoints(player1Move,'Win')


    return outcomePoints+gesturePoints


def calculateTotalScore(input_data):
    points_sum = 0
    for dialogue in input_data:
        player2pointsFromMove = calcPointsForMove(dialogue)
        points_sum = points_sum + player2pointsFromMove

    return points_sum

if (__name__ == "__main__"):
    input_data = parseInput()
    print(calculateTotalScore(input_data))