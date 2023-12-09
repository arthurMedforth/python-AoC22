from parseInput import *

def isCompletelyOverlapping(elfPairArray):
    elf1 = elfPairArray[0]
    elf1Tasks = elf1.split("-")
    elf2 = elfPairArray[1]
    elf2Tasks = elf2.split("-")

    if int(elf1Tasks[0]) <= int(elf2Tasks[0]) and int(elf1Tasks[1]) >= int(elf2Tasks[1]):
        result = 1
    elif int(elf2Tasks[0]) <= int(elf1Tasks[0]) and int(elf2Tasks[1]) >= int(elf1Tasks[1]):
        result = 1
    else:
        result = 0

    return result



if (__name__ == "__main__"):
    input_data = parseInput()
    conditionMetCount = 0
    for elfPair in input_data:
        elfPairSplit = elfPair[0].split(",")
        conditionMetCount += isCompletelyOverlapping(elfPairSplit)

    print(conditionMetCount)