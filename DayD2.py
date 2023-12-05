from parseInput import parseInput5
import cProfile

def processInput(input_lines):
    dict = {}
    curr_key = ''
    for line in input_lines:
        if line.split(':')[0] == 'seeds':
            split_str = line.split(':')
            dict[split_str[0]] = split_str[1].strip().split(' ')
        elif line.split(':')[0][-3:] == 'map':
            curr_key = line.split(':')[0]
            dict[curr_key] = []
        else:
            dict[curr_key].append(line.strip().split(' '))
    return dict

def processMap(values):
    range_dict = {
        "dest_range": range(int(values[0]), int(values[0]) + int(values[2])),
        "source_range": range(int(values[1]), int(values[1]) + int(values[2])),
    }
    return range_dict

def processMapUpdated(values):
    range_dict = {
        "dest_range": [int(values[0]), int(values[0]) + int(values[2]) - 1],
        "source_range": [int(values[1]), int(values[1]) + int(values[2]) - 1]
    }
    return range_dict

def splitRange(original_range):
    start, end = original_range
    midpoint = (start + end) // 2

    # Split the range into two smaller ranges
    first_half = list((start, midpoint))
    second_half = list((midpoint + 1, end))

    return first_half, second_half

def generate_values_from_pairs(pair_list):
    pair_list = [int(i) for i in pair_list] 
    return (value for start, size in zip(pair_list[0::2], pair_list[1::2]) for value in range(start, start + size))

def checkRange(range_vals, key_val):
    if key_val <= range_vals[1] and key_val >= range_vals[0]:
        # Split this range into two and iterate over it
        for split_range in splitRange(range_vals):
            if split_range[0] == split_range[1]:
                return True, split_range[0]
            success_bool, val = checkRange(split_range, key_val)
            if success_bool:
                return success_bool, val
            else:
                continue
    else:
        return False, None

if __name__ == "__main__":
    input_lines = parseInput5()
    complete_dict = processInput(input_lines)
    _dict = dict(zip(complete_dict.keys(),[[] for i in range(len(complete_dict.keys()))]))
    for key in complete_dict.keys():
        if key == 'seeds':
            continue
        else:
            _dict[key] = []
            # Process key (lets assume this is seed-to-soil map for now)
            for el in complete_dict[key]:
                range_dict = processMapUpdated(el)
                _dict[key].append(range_dict)
    locations = []
    # You could try keeping track of which seed/soil/water types you get to so that you don't go to them again
    # This is where it gets really slow
    for seed in generate_values_from_pairs(complete_dict['seeds']):
        print(f'Processing seed {seed}')
        _key_of_interest = int(seed)
        for key in _dict.keys():
            if key == 'seeds':
                continue
            for range_dict in _dict[key]:
                success_bool, val = checkRange(range_dict["source_range"], _key_of_interest)
                if success_bool:
                    #print(f'Seed no:{seed} maps to {key} {range_dict["dest_range"][range_dict["source_range"].index(_key_of_interest)]}')
                    # Pick value in the destination range that corresponds to the value in the source range
                    # Get index of val in the source range
                    # Apply that index to the destination range
                    _key_of_interest = range(range_dict["dest_range"][0],range_dict["dest_range"][1]+1)[range(range_dict["source_range"][0],range_dict["source_range"][1]+1).index(val)]

            #print(f'_key_of_interest remains the same: {_key_of_interest} for key map {key}')
            if key == 'humidity-to-location map':
                locations.append(_key_of_interest)
    
    print(locations)
    print(min(locations))