def parseInput8():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    input_data_list = []
    node_dict = {}
    for i, line in enumerate(file_lines):
        if i == 0:
            instructions = line.strip()
            instructions = [*instructions]
        else:
            if line != '\n':
                split_line = line.strip().split('=')
                options = split_line[1].strip()
                options = options.strip('(')
                options = options.strip(')')
                options = options.split(',')
                options = [el.strip() for el in options]
                node_dict[split_line[0].strip()] = options
    return instructions, node_dict

if __name__ == '__main__':
    instructions, node_dict = parseInput8()
    curr_key = 'AAA'
    found = False
    steps_required = 0
    while not found:
        for instruction in instructions:
            steps_required += 1
            if instruction == 'R':
                curr_key = node_dict[curr_key][1]
            else:
                curr_key = node_dict[curr_key][0]
            if curr_key == 'ZZZ':
                found = True
                break
    print(steps_required)