from parseInput import parseInput

def processInput(line):
    new_input_lines = []
    new_list = []
    for i, el in enumerate(line): 
        if el not in ['.', '*', '$', '#']:
            new_list.append(el)
        else:
            if len(new_list) == 3:
                new_input_lines.append(''.join(new_list))
            new_input_lines.append(el.strip())
            new_list = []
    return new_input_lines

if __name__ == '__main__':
    input_lines = parseInput()
    new_input_lines = []
    for line in input_lines:
        new_input_lines.append(processInput(line))
    
    print(new_input_lines)