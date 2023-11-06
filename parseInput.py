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

    file_lines=fin.readlines()
    input_data_list = []

    print(file_lines)
    # for i in range(0,3):
    #     line = file_lines[i].strip()
    #     line_move = line.split(' ')[1]
    #     input_data_list.append(line_move)


    return input_data_list



