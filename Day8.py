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

def get_viewing_distance(dir_flag,vertic_index,horiz_index,row_const,col_const,grid,viewing_dist):
    if dir_flag == 'Left':
        if horiz_index - 1 < 0:
            return viewing_dist
        else:
            if grid[vertic_index][horiz_index-1] < grid[vertic_index][horiz_index]and grid[vertic_index][horiz_index-1] < grid[row_const][col_const]:
                # Can increment viewing dist
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Left',vertic_index,horiz_index-1,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index][horiz_index-1] == grid[vertic_index][horiz_index] and grid[vertic_index][horiz_index-1] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Left',vertic_index,horiz_index-1,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index][horiz_index-1] > grid[vertic_index][horiz_index] and grid[vertic_index][horiz_index-1] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Left',vertic_index,horiz_index-1,row_const,col_const,grid,viewing_dist)
            else:
                viewing_dist += 1
                return viewing_dist
    elif dir_flag == 'Right':
        if horiz_index + 1 > len(grid[0])-1:
            return viewing_dist
        else:
            if grid[vertic_index][horiz_index+1] < grid[vertic_index][horiz_index] and grid[vertic_index][horiz_index+1] < grid[row_const][col_const]:
                # Can increment viewing dist
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Right',vertic_index,horiz_index+1,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index][horiz_index+1] == grid[vertic_index][horiz_index] and grid[vertic_index][horiz_index+1] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Right',vertic_index,horiz_index+1,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index][horiz_index+1] > grid[vertic_index][horiz_index] and grid[vertic_index][horiz_index+1] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Right',vertic_index,horiz_index+1,row_const,col_const,grid,viewing_dist)
            else:
                viewing_dist += 1
                return viewing_dist 
    elif dir_flag == 'Up':
        if vertic_index - 1 < 0:
            return viewing_dist
        else:
            if grid[vertic_index-1][horiz_index] < grid[vertic_index][horiz_index] and grid[vertic_index-1][horiz_index] < grid[row_const][col_const]:
                # Can increment viewing dist
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Up',vertic_index-1,horiz_index,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index-1][horiz_index] == grid[vertic_index][horiz_index] and grid[vertic_index-1][horiz_index] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Up',vertic_index-1,horiz_index,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index-1][horiz_index] > grid[vertic_index][horiz_index] and grid[vertic_index-1][horiz_index] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Up',vertic_index-1,horiz_index,row_const,col_const,grid,viewing_dist)
            else:
                viewing_dist += 1
                return viewing_dist 
    elif dir_flag == 'Down':
        if vertic_index + 1 > len(grid)-1:
            return viewing_dist
        else:
            if grid[vertic_index+1][horiz_index] < grid[vertic_index][horiz_index]and grid[vertic_index+1][horiz_index] < grid[row_const][col_const]:
                # Can increment viewing dist
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Down',vertic_index+1,horiz_index,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index+1][horiz_index] == grid[vertic_index][horiz_index] and grid[vertic_index+1][horiz_index] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Down',vertic_index+1,horiz_index,row_const,col_const,grid,viewing_dist)
            elif grid[vertic_index+1][horiz_index] > grid[vertic_index][horiz_index] and grid[vertic_index+1][horiz_index] < grid[row_const][col_const]:
                viewing_dist += 1
                viewing_dist = get_viewing_distance('Down',vertic_index+1,horiz_index,row_const,col_const,grid,viewing_dist)
            else:
                viewing_dist += 1
                return viewing_dist 
    else:
        raise(ValueError('This direction doesnt exist'))
    return viewing_dist

def find_best_scenic_score(grid):
    highest_viewing_distance_score = 0
    for row_num in range(len(grid)):
        for col_num in range(len(grid[0])):
            viewing_dist_left = get_viewing_distance('Left',row_num,col_num,row_num,col_num,grid,0)
            viewing_dist_right = get_viewing_distance('Right',row_num,col_num,row_num,col_num,grid,0)
            viewing_dist_up = get_viewing_distance('Up',row_num,col_num,row_num,col_num,grid,0)
            viewing_dist_down = get_viewing_distance('Down',row_num,col_num,row_num,col_num,grid,0)

            current_viewing_dist = viewing_dist_left * viewing_dist_right * viewing_dist_up * viewing_dist_down
            if current_viewing_dist > highest_viewing_distance_score:
                highest_viewing_distance_score = current_viewing_dist
    return highest_viewing_distance_score

if __name__ == '__main__':
    input_lines = parseInput()
    grid = process_input(input_lines)
    visible_tree_count = process_forest_for_8a(grid)
    most_scenic_score = find_best_scenic_score(grid)
    print(most_scenic_score)