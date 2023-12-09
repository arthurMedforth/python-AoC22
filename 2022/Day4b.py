from parseInput import *
from Day4a import *

def checkRangeInclusionRevised(TaskSet1,TaskSet2):
    if int(TaskSet1[1])-int(TaskSet1[0])>0:
        Tasks1Iterable = list(range(int(TaskSet1[0]),int(TaskSet1[1])+1))
    else:
        Tasks1Iterable = list(range(int(TaskSet1[0]),int(TaskSet1[0])+1))

    result = 0
    print(Tasks1Iterable)
    for i in range(len(Tasks1Iterable)):
        if Tasks1Iterable[i]==int(TaskSet2[0]) or Tasks1Iterable[i]==int(TaskSet2[1]):
            result = 1
            break
        elif Tasks1Iterable[i]>int(TaskSet2[0]) and Tasks1Iterable[i]<int(TaskSet2[1]):
            result = 1
            break
        else:
            continue

    return result

def isSomeOverlap(elfPairArray):
    elf1 = elfPairArray[0]
    elf1Tasks = elf1.split("-")
    elf2 = elfPairArray[1]
    elf2Tasks = elf2.split("-")

    res = checkRangeInclusionRevised(elf1Tasks,elf2Tasks)
    if res == 0:
        res = checkRangeInclusionRevised(elf2Tasks,elf1Tasks)

    return res


if (__name__ == "__main__"):
    input_data = parseInput()
    conditionMetCount = 0
    for elfPair in input_data:
        elfPairSplit = elfPair[0].split(",")
        conditionMetCount += isSomeOverlap(elfPairSplit)

    print(conditionMetCount)
