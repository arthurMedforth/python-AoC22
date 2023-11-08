from parseInput import parseInput

def getFeasibleDirs(curr_row, curr_col, row_lim, col_lim, prev_dir):
    dir_list = ['left','right','up','down']
    if curr_row == row_lim or prev_dir == 'up': # Dont go down
        dir_list.pop(3) 
    if curr_row == 0 or prev_dir == 'down': # Dont go up
        dir_list.pop(2)
    if curr_col == col_lim or prev_dir == 'left': # Dont go right
        dir_list.pop(1)
    if curr_col == 0 or prev_dir == 'right': # Dont go left
        dir_list.pop(0) 
    return dir_list

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
    row_lim = len(grid) - 1
    col_lim = len(grid[0]) - 1
    dir_list = getFeasibleDirs(curr_row, curr_col, row_lim, col_lim, prev_dir)
    rankings = []
    success_bool = False
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
            # Try the next ranked direction
            # MAYBE: Worth noting that things probably aren't going well if we are here!
            continue
        else:
            # NO so we cann add it to the current stack
            move_stack.append([ranked_dir[1][0],ranked_dir[1][1]]) 
            # Lets check that if its possible to beat the best so far if we theoretically took 
            # the smallest journey physically possible to destination from where we are now
            if len(success_steps_list) > 0:
                theoretical_smallest_dist = abs(S_coords[0]-ranked_dir[1][0]) + abs(S_coords[1]-ranked_dir[1][1])
                if theoretical_smallest_dist + (len(move_stack) - 1) >= min(success_steps_list):
                    # There is no point carrying on with this traverse because 
                    # we can't do better than best
                    move_stack.pop(-1)
                    break
        # Is where we have just arrived our destination?
        if move_stack[-1] == E_coords:
            success_bool = True
            success_steps_list.append(len(move_stack)-1)
            print('Found successful path: '+ str(len(move_stack)-1))
            move_stacks.append(move_stack.copy())
            move_stack.pop(-1)
            break
        else:
            success_bool, move_stack = nextBestStep(ranked_dir[1][0],ranked_dir[1][1], ranked_dir[0], grid, move_stack)
        # You need to check whether or not this is right
        # Why aren't you checking the success_bool condition at all before 
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
    success_steps_list = []
    move_stacks = []
    move_stack = []
    E_coords = list(findChar(input_lines,'E'))
    S_coords = list(findChar(input_lines,'S'))
    move_stack.append(S_coords)
    success_bool, move_stack = nextBestStep(S_coords[0], S_coords[1], 'None', input_lines, move_stack)
    print(min(success_steps_list))