from parseInput import *
from Day4a import *


def checkRangeInclusion(largerRangeTasks,smallerRangeTasks):
    
    if smallerRangeTasks[0] <= largerRangeTasks[1] and smallerRangeTasks[0] >= largerRangeTasks[0]:
        result = 1
    elif smallerRangeTasks[1] <= largerRangeTasks[1] and smallerRangeTasks[1] >= largerRangeTasks[0]:
        result = 1
    else:
        result = 0 

    # if result == 1:
    #     print(smallerRangeTasks,largerRangeTasks)

    return result

def isSomeOverlap(elfPairArray):
    elf1 = elfPairArray[0]
    elf1Tasks = elf1.split("-")
    elf2 = elfPairArray[1]
    elf2Tasks = elf2.split("-")

    # Calculate range
    elf1Range = int(elf1Tasks[1])-int(elf1Tasks[0])
    elf2Range = int(elf2Tasks[1])-int(elf2Tasks[0])
    
    if elf1Range > elf2Range:
        # Check if either elf number is within the two elf1Task numbers
        res = checkRangeInclusion(elf1Tasks,elf2Tasks)
    elif elf1Range < elf2Range:
        # Check if either elf number is within the two elf1Task numbers
        res = checkRangeInclusion(elf2Tasks,elf1Tasks)
    else:
        # Doesnt matter
        res = checkRangeInclusion(elf1Tasks,elf2Tasks)

    return res


if (__name__ == "__main__"):
    input_data = parseInput()
    conditionMetCount = 0
    for elfPair in input_data:
        elfPairSplit = elfPair[0].split(",")
        if isCompletelyOverlapping(elfPairSplit) == 1:
            # conditionMetCount += 1
            pin = 0
        else:
            conditionMetCount += isSomeOverlap(elfPairSplit)

    print(conditionMetCount)
