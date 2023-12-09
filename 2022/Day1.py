from parseInput import *
import numpy as np

def reorderList(unordered_list):
    return sorted(unordered_list,reverse=True)


def findGreediestElves(input_data, quantity):
    sum_list = []
    current_sum = 0
    for i in range(len(input_data)):
        if (input_data[i]==''):
            sum_list.append(current_sum)
            current_sum = 0
        else:
            current_sum = current_sum + input_data[i]
            if (i==len(input_data)-1):
                sum_list.append(current_sum)

    ordered_list = reorderList(sum_list)
    elf_cal_sum = 0
    for j in range(quantity):
        elf_cal_sum = elf_cal_sum + ordered_list[j]

    return elf_cal_sum


if (__name__ == "__main__"):
    input_data = parseInput()
    print(findGreediestElves(input_data,3))