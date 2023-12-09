from parseInput import parseInput

def flipInputData(input_data):
    new_input_data = []
    for line in input_data:
        new_input_data.append([el for el in reversed(line)])
    return new_input_data

def getDiffList(_list):
    diff_list = []
    all_zero = True
    for i in range(0, len(_list)):
        if i+1 > len(_list) - 1:
            break
        else:
            diff = _list[i+1] - _list[i]
            if diff != 0:
                all_zero = False
            diff_list.append(diff)
    
    return diff_list, all_zero

if __name__ == '__main__':
    input_data = parseInput()
    # Part 2 - comment out for part 1
    input_data = flipInputData(input_data)
    part1_sum = 0
    for line in input_data:
        master_diff_list = [line]
        diff_list, all_zero = getDiffList(line)
        master_diff_list.append(diff_list)
        while not all_zero:
            diff_list, all_zero = getDiffList(diff_list)
            if not all_zero: # Do you need this condition
                master_diff_list.append(diff_list)
        # Iterate back through the master_diff_list cascading upwards
        rolling_sum = 0
        for i in reversed(range(0,len(master_diff_list))):
            if i - 1 < 0:
                break
            elif i == len(master_diff_list) - 1:
                rolling_sum = master_diff_list[i-1][-1] + master_diff_list[i][-1]
            else:
                rolling_sum = master_diff_list[i-1][-1] + rolling_sum
        part1_sum += rolling_sum
    print(part1_sum)
