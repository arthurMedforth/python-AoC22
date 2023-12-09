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

def generate_values_from_pairs(pair_list):
    pair_list = [int(i) for i in pair_list] 
    return (value for start, size in zip(pair_list[0::2], pair_list[1::2]) for value in range(start, start + size))

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
                range_dict = processMap(el)
                _dict[key].append(range_dict)
    locations = []

    # This is where it gets really slow as this main loop alone is huge
    for seed in generate_values_from_pairs(complete_dict['seeds']):
        # print(f'Processing seed {seed}')
        _key_of_interest = int(seed)
        for key in _dict.keys(): # Loop through the map keys
            if key == 'seeds':
                continue
            for range_dict in _dict[key]: # For each set of source and destination ranges
                if _key_of_interest in range_dict["source_range"]: # Is the current seed/soil/water in the source range?
                    #print(f'Seed no:{seed} maps to {key} {range_dict["dest_range"][range_dict["source_range"].index(_key_of_interest)]}')
                    _key_of_interest = range_dict["dest_range"][range_dict["source_range"].index(_key_of_interest)]
                    break           
            #print(f'_key_of_interest remains the same: {_key_of_interest} for key map {key}')
            if key == 'humidity-to-location map':
                locations.append(_key_of_interest)
    
    print(min(locations))
    