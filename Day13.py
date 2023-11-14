import json

def typeCastStringLists():
    pairs = []
    curr_pair = []
    with open('input.txt','rt') as fin: # File specified in command line or others
        file_lines = fin.readlines()
        for i, line in enumerate(file_lines):
            stripped_line = line.strip('\n')
            if not stripped_line:
                pairs.append(curr_pair)
                curr_pair = []
                continue
            else:
                try:
                    actual_list = json.loads(line)
                    curr_pair.append(actual_list)
                    if i == len(file_lines)-1:
                        pairs.append(curr_pair)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON on line {i}: {e}")
    return pairs

def intCheck(left_int, right_int):
    parity_flag = False
    if left_int > right_int:
        incorrect_bool = True
    elif left_int < right_int:
        incorrect_bool = False
    else:
        incorrect_bool = False
        parity_flag = True

    # Could return a flag to say if the values were true
    return incorrect_bool, parity_flag

def listCheck(left_list, right_list):
    parity_flag = False
    incorrect_bool = False
    if len(left_list) < len(right_list):
        lim = ['left', len(left_list)] 
    elif len(right_list) < len(left_list):
        lim = ['right', len(right_list)]
    else:
        lim = ['neither',len(left_list)]


    for i in range(lim[1]):
        # Need code here to check the data types
        incorrect_bool, parity_flag = processOperands(left_list[i], right_list[i])
        if incorrect_bool:
            break

    # If the last two values compared were equal AND there is a limiting list - if its the right list, we set the incorrect bool
    if parity_flag and not incorrect_bool and lim[0] == 'right':
        incorrect_bool = True

    return incorrect_bool, parity_flag

def processOperands(left, right):
    if type(left) is type(right):
        if type(left) == int:
            # Both integers
            incorrect_bool, parity_flag = intCheck(left, right)
        else:
            # Both lists
            incorrect_bool, parity_flag = listCheck(left, right)
    else:
        # One list one int
        if type(left) is list:
            incorrect_bool, parity_flag = listCheck(left, [right])
        else:
            incorrect_bool, parity_flag = listCheck([left], right)
    return incorrect_bool, parity_flag

if __name__ == "__main__":
    pairs_list = typeCastStringLists()
    incorrect_order_inds = []
    for i, pair in enumerate(pairs_list):
        incorrect_bool = False
        while not incorrect_bool:
            left = pair[0]
            right = pair[1]
            incorrect_bool, parity_flag = processOperands(left, right)
            if incorrect_bool:
                incorrect_order_inds.append(i+1)
            else:
                break
    
    inds = [j+1 for j in range(len(pairs_list))]
    for ind in reversed(inds):
        for incorrect_ind in reversed(incorrect_order_inds):
            if incorrect_ind == ind:
                inds.pop(ind-1)

    print(inds)