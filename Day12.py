from parseInput import parseInput

def findStart(grid):
    for i in range(len(input_lines)): # Row
        for j in range(len(input_lines[i])): # Col
            if input_lines[i][j] == 'S':
                return i, j
            else: 
                continue

def getFeasibleDirs(curr_row, curr_col, row_lim, col_lim):
    dir_list = ['left','right','up','down']
    if curr_row == 0:
        dir_list.pop(2)
    if curr_col == 0:
        dir_list.pop(0)
    if curr_row == row_lim:
        dir_list.pop(3)
    if curr_col == col_lim:
        dir_list.pop(1)
    return dir_list

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
    
def checkNextCoords(curr_row, curr_col, grid, step_count):
    dir_list = getFeasibleDirs(curr_row, curr_col, len(grid) - 1, len(grid[0]) - 1)
    alphabet = 'abcdefghijeklmnopqrstuvwxyz'
    success_bool = False
    for dir in dir_list:
        maybe_new_row, maybe_new_col = getMaybeCoords(curr_row, curr_col, dir)
        if alphabet.rfind(grid[maybe_new_row][maybe_new_col]) - alphabet.rfind(grid[curr_row][curr_col]) > 1:
            # Cant move to destination square
            continue
        else: # Can move to destination as its either 1 higher, at the same height or much lower than current coord
            if grid[maybe_new_row][maybe_new_col] == 'E':
                success_bool = True
                step_count += 1
                return success_bool, step_count
            else:
                step_count += 1
                success_bool, step_count = checkNextCoords(maybe_new_row, maybe_new_col, input_lines, step_count)
    return success_bool, step_count
            
if __name__ == "__main__":
    input_lines = parseInput()
    alphabet = 'abcdefghijeklmnopqrstuvwxyz'
    start_row, start_col = findStart(input_lines)    
    dirs = getFeasibleDirs(start_row, start_col, len(input_lines) - 1, len(input_lines[0]) - 1)
    best_count = 20000000000000000000000000000000000
    for i, dir in enumerate(dirs):
        step_count = 0
        maybe_new_row, maybe_new_col = getMaybeCoords(start_row, start_col, dir)
        if alphabet.rfind(input_lines[maybe_new_row][maybe_new_col]) - alphabet.rfind('a') > 1:
            # Cant move to destination square
            continue
        else:
            step_count += 1
            success_bool, step_count = checkNextCoords(maybe_new_row, maybe_new_col, input_lines, step_count)

        if step_count < best_count and success_bool:
            best_count = step_count
        else: 
            continue

    print(best_count)

