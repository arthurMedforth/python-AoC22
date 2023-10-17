from parseInput import *
import numpy as np

def process_input(input_lines):
    grid = []
    # List comp to convert chars to ints
    for i,line in enumerate(input_lines):
        row_chars = [*line[0]]
        row = [int(x) for x in row_chars]
        grid.append(row)
    return grid

def path_find_left(row,positive_inds):
    first_ind_of_selection_max = row.index(max(row))
    positive_inds.append(first_ind_of_selection_max)
    new_selection = row[:first_ind_of_selection_max]
    if len(new_selection) >= 1:
        positive_inds = path_find_left(new_selection,positive_inds)
    return positive_inds

def process_forest_for_8a(grid):
    a = (4,len(grid),len(grid))
    state_grid = np.zeros(a) 
    count = 0
    while count < 4:
        state_grid_left = state_grid[count,:,:]
        # Looking to the left
        from_left_tree_count = 0
        for i, row in enumerate(grid):
            positive_inds = []
            positive_inds = path_find_left(row,positive_inds)
            new_state_row = [1 if i in positive_inds else 0 for i, el in enumerate(row)]        
            state_grid_left[i] = new_state_row
        state_grid[count,:,:] = np.rot90(state_grid_left,4-count)
        grid = np.rot90(grid)
        grid = grid.tolist()
        count += 1
    result_state_array = np.sum(state_grid,0)
    return np.count_nonzero(result_state_array)

if __name__ == '__main__':
    input_lines = parseInput()
    grid = process_input(input_lines)
    visible_tree_count = process_forest_for_8a(grid)
    print(visible_tree_count)