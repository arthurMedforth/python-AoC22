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

def generate_ranges_from_pairs(pair_list):
    pair_list = [int(i) for i in pair_list] 
    seed_ranges = []
    for i in range(0, len(pair_list), 2):
        seed_ranges.append((pair_list[i], pair_list[i] + pair_list[i+1]))
    return seed_ranges


def getSeedsToHit(overlaps):
    list_seeds = []
    for overlap in overlaps:
        overlap_list = []
        for i in range(overlap[0], overlap[1]+1):
            overlap_list.append(i)
        list_seeds.append([overlap_list, overlap[2]])
    return list_seeds


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
    
    # Get the ranges of the sources
    source_ranges = []
    dest_ranges = []
    for map_range in complete_dict["seed-to-soil map"]:
        for source_range in generate_ranges_from_pairs([map_range[1], map_range[2]]):
            source_ranges.append([source_range,  int(map_range[0])-int(map_range[1])]) # This is the range of source values
    # Get the ranges where the seeds overlap with the source ranges
    overlaps = []
    for seed_range in generate_ranges_from_pairs(complete_dict['seeds']):
        for source_range in source_ranges:
            if seed_range[1] > source_range[0][0]:
                overlaps.append([max(source_range[0][0], seed_range[0]), seed_range[1], source_range[1]])
            elif seed_range[0] < source_range[0][1] and seed_range[1] > source_range[0][0]:
                overlaps.append([seed_range[0], source_range[1], source_range[1]])
            elif seed_range[0] > source_range[0][0] and seed_range[1] < source_range[0][1]:
                overlaps.append([seed_range[0], seed_range[1], source_range[1]])
            else:
                continue
    seeds_list = getSeedsToHit(overlaps)
    # Loop through the seeds to get to locations 
    dest_list = []
    locations = []
    sum_s = 0
    for seeds in seeds_list:
        for seed in seeds:
            sum_s += 1
    print(f'Number of seeds to check {sum_s}')
    for seed_set in seeds_list: # Reduced search space
        conversion = seed_set[1]
        for seed in seed_set[0]:
            print(f'Processing seed id: {seed}')
            _key_of_interest = seed
            for key in _dict.keys(): # Loop through the map keys
                if key == 'seeds':
                    continue
                for range_dict in _dict[key]: # For each set of source and destination ranges
                    # Get overlaps and update the destinations as you go
                    if _key_of_interest in range_dict["source_range"]: 
                        _key_of_interest = range_dict["dest_range"][range_dict["source_range"].index(_key_of_interest)]
                        break           
                #print(f'_key_of_interest remains the same: {_key_of_interest} for key map {key}')
                if key == 'humidity-to-location map':
                    locations.append(_key_of_interest)
