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


def getSource(_dict, ind, input_dest):
    answer = None
    keys = list(_dict.keys())
    key_map = _dict[keys[ind]]
    for val_set in key_map:
        for i, dest in enumerate(val_set['dest_range']):
            if input_dest == dest:
                if keys[ind] == 'seed-to-soil map' and val_set['source_range'][i] in _dict['seeds']:
                    return val_set['source_range'][i]
                else:
                    answer = getSource(_dict, ind - 1, val_set['source_range'][i])
                    if answer:
                        return answer
            else:
                continue
    return answer

if __name__ == "__main__":
    input_lines = parseInput5()
    complete_dict = processInput(input_lines)
    _dict = dict(zip(complete_dict.keys(),[[] for i in range(len(complete_dict.keys()))]))
    _dict['seeds'] = [int(val) for val in complete_dict['seeds']]
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
    # Loop every location in the location map
    for location_set in _dict['humidity-to-location map']:
        for location in location_set['dest_range']:
            if location == 82: 
                print('stop')
            answer = getSource(_dict, len(_dict.keys())-1, location)
            if answer:
                locations.append(location)