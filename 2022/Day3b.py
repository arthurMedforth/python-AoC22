from parseInput import *
from Day3a import *


def findBadge(bag1,bag2,bag3):
    bag1List = set(bag1)
    bag2List = set(bag2)
    bag3List = set(bag3)

    firstIntersection = bag1List.intersection(bag2List)
    secondIntersection = firstIntersection.intersection(bag3List)
    intersectionlist = list(secondIntersection)

    return intersectionlist[0]

if (__name__ == "__main__"):
    input_data = parseInput()
    priorityItemsValue = []
    ElfCount = 0
    while (ElfCount <= len(input_data) - 3):
        # Get elf bags
        elf1Bag = input_data[ElfCount][0]
        ElfCount = ElfCount + 1

        elf2Bag = input_data[ElfCount][0]
        ElfCount = ElfCount + 1

        elf3Bag = input_data[ElfCount][0]

        badgeLetter = findBadge(elf1Bag,elf2Bag,elf3Bag)
        priorityItemsValue.append(getLetterPriority(badgeLetter))

        # For next loop
        ElfCount = ElfCount + 1

    print(sum(priorityItemsValue))
