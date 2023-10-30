from parseInput import parseInput

def checkForCriticalCycle(X, curr_cycle, total_signal_strength_sum):
    cycles_of_interest = [20,60,100,140,180,220]
    if curr_cycle in cycles_of_interest and not bools[cycles_of_interest.index(curr_cycle)]:
        total_signal_strength_sum += (X * curr_cycle)
        bools[cycles_of_interest.index(curr_cycle)] = True
    return total_signal_strength_sum

if __name__ == "__main__":
    input_lines = parseInput()
    cycle_number = 0
    count = 0
    signal_strength_sum = 0
    X = 1
    bools = [False,False,False,False,False,False]
    total_cycles = sum(instruction[0] == "noop" for instruction in input_lines) + sum(instruction[0] == "addx" for instruction in input_lines)*2
    while cycle_number < total_cycles:
        curr_line = input_lines[count]
        if curr_line[0] == "noop":
            signal_strength_sum = checkForCriticalCycle(X, cycle_number, signal_strength_sum)
            cycle_number += 1
            signal_strength_sum = checkForCriticalCycle(X, cycle_number, signal_strength_sum)
        else: 
            signal_strength_sum = checkForCriticalCycle(X, cycle_number, signal_strength_sum)
            cycle_number += 1
            signal_strength_sum = checkForCriticalCycle(X, cycle_number, signal_strength_sum)
            cycle_number += 1
            signal_strength_sum = checkForCriticalCycle(X, cycle_number, signal_strength_sum)
            X += int(curr_line[1])
            signal_strength_sum = checkForCriticalCycle(X, cycle_number, signal_strength_sum)
        count += 1
    print(signal_strength_sum)