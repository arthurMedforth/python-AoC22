import json

def parseInput():
    # Read input
    fin=open('/Users/arthurmedforth/python-AoC22/2023/input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    input_data_list = []
    for i in range(len(file_lines)):
        line = file_lines[i].strip()
        line_move = line.split(' ')
        line = [*line_move[0]]
        input_data_list.append(line)

    return input_data_list

def parseInput5a():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other

    file_lines=fin.readlines()
    input_data_list = []

    print(file_lines)
    # for i in range(0,3):
    #     line = file_lines[i].strip()
    #     line_move = line.split(' ')[1]
    #     input_data_list.append(line_move)

    return input_data_list

def typeCastStringLists():
    input_data_list = []
    curr_pair = []
    with open('input.txt','rt') as fin: # File specified in command line or others
        file_lines = fin.readlines()
        for i, line in enumerate(file_lines):
            stripped_line = line.strip('\n')
            if not stripped_line:
                input_data_list.append(curr_pair)
                curr_pair = []
                continue
            else:
                try:
                    actual_list = json.loads(line)
                    curr_pair.append(actual_list)
                    if i == len(file_lines)-1:
                        input_data_list.append(curr_pair)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON on line {i}: {e}")
    return input_data_list


def parseInput3():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    games = {}
    for i in range(len(file_lines)):
        line = file_lines[i].strip()
        subset_list = line.split(':')
        games[subset_list[0]] = subset_list[1].split(';')

    return games

def parseInput5():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    input_data_list = []
    for i in range(len(file_lines)):
        if file_lines[i] == '\n':
            continue
        line = file_lines[i].strip()
        input_data_list.append(line)

    return input_data_list

def parseInput6a():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    input_data_list = []
    for i in range(len(file_lines)):
        if file_lines[i] == '\n':
            continue
        line = file_lines[i].strip()
        line_move = line.split(' ')
        line_move = [int(el) for el in line_move if el not in  ['', 'Time:','Distance:']]
        input_data_list.append(line_move)

    return input_data_list

def parseInput6b():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    input_data_list = []
    for i in range(len(file_lines)):
        if file_lines[i] == '\n':
            continue
        line = file_lines[i].strip()
        line_move = line.split(' ')
        line_move = [el for el in line_move if el not in  ['', 'Time:','Distance:']]
        line_move = int(''.join(line_move))
        input_data_list.append(line_move)

    return input_data_list

def parseInput4():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    input_data = []
    for i in range(len(file_lines)):
        line = file_lines[i].strip()
        subset_list = line.split(':')
        input_data.append(subset_list)
    
    return input_data