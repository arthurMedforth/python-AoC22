from parseInput import *
import numpy as np

def occurrenceListProcessor(list,stringLength):
    halfwayIndex = stringLength/2-1
    itemInFirstHalf = False
    itemInSecondHalf = False
    for ind in list:
        if ind<=halfwayIndex:
            itemInFirstHalf = True
        else:
            itemInSecondHalf = True

    return itemInFirstHalf and itemInSecondHalf

def findCommonLetter(rucksackInstance):
    commonLetter = ''
    for i in range(len(rucksackInstance)-1):
        char = rucksackInstance[i]
        occurrenceList = [i for i, letter in enumerate(rucksackInstance) if letter == char]
        # print(char)
        # print(occurrenceList)
        if len(occurrenceList) > 1:
            success = occurrenceListProcessor(occurrenceList,len(rucksackInstance))
            if success:
                commonLetter = char
            else: 
                continue
        else:
            continue

    if commonLetter =='':
        print('problem')

    return commonLetter

def getLetterPriority(letter):
    if letter.islower():
        priorityValue = ord(letter)-ord('a')+1
    else:
        # make lowercase
        lowercaseChar = letter.lower()
        priorityValue = ord(lowercaseChar) - ord('a') + 1 + 26

    return priorityValue

if (__name__ == "__main__"):
    input_data = parseInput()
    priorityItemsValue = []
    for rucksack in input_data:
        commonLetter = findCommonLetter(rucksack[0])
        print(commonLetter)
        priorityItemsValue.append(getLetterPriority(commonLetter))

    print(sum(priorityItemsValue))