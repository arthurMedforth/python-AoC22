<<<<<<< HEAD
def parseInput():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
=======
import json

def parseInput():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
    file_lines=fin.readlines()
    input_data_list = []
    for i in range(len(file_lines)):
        line = file_lines[i].strip()
        line_move = [*line]
        input_data_list.append(line_move)

    return input_data_list

def parseInput5a():
    # Read input
    fin=open('input.txt','rt') # File specified in command line or other
>>>>>>> cd0a864543d9c6ab2fd2a78bf08af93f338184e0

    file_lines=fin.readlines()
    input_data_list = []

<<<<<<< HEAD
    for i in range(len(file_lines)):
        line = file_lines[i].strip()
        line_move = line.split(' ')
        input_data_list.append(line_move)


    return input_data_list

=======
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



>>>>>>> cd0a864543d9c6ab2fd2a78bf08af93f338184e0
