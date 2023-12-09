from parseInput import parseInput

def getFeasibleDirs(curr_row, curr_col, row_lim, col_lim, prev_dir):
    dir_conditions = {
        'left': curr_col != 0 and prev_dir != 'right',
        'right': curr_col != col_lim and prev_dir != 'left',
        'up': curr_row != 0 and prev_dir != 'down',
        'down': curr_row != row_lim and prev_dir != 'up'
    }
    return [dir for dir, condition in dir_conditions.items() if condition]


def getNewCoordHeight(curr_row, curr_col, maybe_new_row, maybe_new_col, grid):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if grid[maybe_new_row][maybe_new_col] == 'E':
        new_char = 'z'
    else:
        new_char = grid[maybe_new_row][maybe_new_col]
    if grid[curr_row][curr_col] == 'S':
        curr_char = 'a'
    else:
        curr_char = grid[curr_row][curr_col]
    diff = alphabet.rfind(new_char) - alphabet.rfind(curr_char)
    if diff > 1:
        height = None
    else:
        height = diff
    return height

def getMaybeCoords(curr_row, curr_col, dir):
    if dir == 'left':
        maybe_new_row = curr_row
        maybe_new_col = curr_col - 1
    elif dir == 'right':
        maybe_new_row = curr_row
        maybe_new_col = curr_col + 1
    elif dir == 'up':
        maybe_new_row = curr_row - 1 
        maybe_new_col = curr_col
    else:
        maybe_new_row = curr_row + 1 
        maybe_new_col = curr_col
    return maybe_new_row, maybe_new_col

def nextBestStep(curr_row, curr_col, prev_dir, grid, move_stack):
    if [curr_row, curr_col] == E_coords:
        move_stacks.append(move_stack.copy())
        success_steps_list.append(len(move_stack)-1)
        print(f"Found successful path with length = {len(move_stack)-1}")
        success_bool = True
        return success_bool, move_stack
    else:
        success_bool = False
    row_lim = len(grid) - 1
    col_lim = len(grid[0]) - 1
    dir_list = getFeasibleDirs(curr_row, curr_col, row_lim, col_lim, prev_dir)
    rankings = []
    # For each of my feasible next directions - rank them in terms of priority
    # where 1 is the best score, then 0, then negative numbers (if you go down, you'll have to come back up...)
    for dir in dir_list:
        new_row, new_col = getMaybeCoords(curr_row, curr_col, dir)
        rankings.append([dir, [new_row, new_col], getNewCoordHeight(curr_row, curr_col, new_row, new_col, grid)])
    rankings = [element for element in rankings if element[2] != None]
    sorted_rankings = sorted(rankings, key = lambda y:y[2], reverse = True)
    # MAYBE: If you get to the end of this and can't move anywhere
    # MAYBE: You should add that coord to a list to backout from if you land there again
    for ranked_dir in sorted_rankings:
        # Have we already been to this point
        if [ranked_dir[1][0], ranked_dir[1][1]] in move_stack: # YES
            continue
        else:
            # NO so we can add it to the current stack
            move_stack.append([ranked_dir[1][0],ranked_dir[1][1]]) 
        success_bool, move_stack = nextBestStep(ranked_dir[1][0],ranked_dir[1][1], ranked_dir[0], grid, move_stack)
        move_stack.pop(-1)
    return success_bool, move_stack

def findChar(grid,char):
    for i in range(len(input_lines)): # Row
        for j in range(len(input_lines[i])): # Col
            if input_lines[i][j] == char:
                return i, j
            else: 
                continue

if __name__ == "__main__":
    # This code is starting at the start and trying to find the end
    input_lines = parseInput()
    global success_steps_list 
    global E_coords
    global S_coords
    global move_stacks 
    global bad_moves
    bad_moves = []
    success_steps_list = []
    move_stacks = []
    move_stack = []
    E_coords = list(findChar(input_lines,'E'))
    S_coords = list(findChar(input_lines,'S'))
    move_stack.append(S_coords)
    success_bool, move_stack = nextBestStep(S_coords[0], S_coords[1], 'None', input_lines, move_stack)
    print(min(success_steps_list))