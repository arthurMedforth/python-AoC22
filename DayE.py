from parseInput import parseInput6a, parseInput6b
import numpy as np

def getFeasibleWays(time_dest_pair):
    total_time = time_dest_pair[0]
    total_dist = time_dest_pair[1]
    feasible_ways = 0
    for millisecs_to_hold in range(0, total_time):
        speed_on_release = millisecs_to_hold
        if (total_time - millisecs_to_hold) * speed_on_release > total_dist:
            feasible_ways += 1
        else:
            continue
    return feasible_ways

def part1(input_lines):
    zipped_list = list(zip(input_lines[0],input_lines[1]))
    starting_speed = 0
    feasible_ways = []
    for pair in zipped_list:
        num_feas_ways = getFeasibleWays(pair)
        if num_feas_ways > 0:
            feasible_ways.append(num_feas_ways)
    return np.prod(feasible_ways)

def part2(input_lines):
    starting_speed = 0
    feasible_ways = []
    num_feas_ways = getFeasibleWays(input_lines)
    return num_feas_ways

if __name__ == '__main__':
    #input_lines = parseInput6a()
    #print(part1(input_lines))
    input_lines = parseInput6b()
    print(part2(input_lines))
