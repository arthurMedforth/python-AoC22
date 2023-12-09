from parseInput import parseInput
import numpy as np 

def processInput(line):
    new_list = []
    for i, el in enumerate(line): 
        new_list.append(el)
    return new_list

def getCharCoords(r, c, grid):
    coords = [[r, c]]
    if c+2 < len(grid[r]) and grid[r][c+2].isalnum() and grid[r][c+1].isalnum():
        coords.append([r,c+1])
        coords.append([r,c+2])
    elif c+1 < len(grid[r]) and grid[r][c+1].isalnum():
        coords.append([r,c+1])
    else:
        coords = coords    
    return coords

def adjacentToSymbol(coords, grid, val):
    for coord in coords_list:
        r, c = coord
        adj_coords = [[r-1, c-1],[r, c-1],[r+1, c-1],[r-1, c],[r+1, c],[r-1, c+1],[r, c+1], [r+1, c+1]]
        for adj_coord in adj_coords:
            adj_r, adj_c = adj_coord
            if adj_r < 0 or adj_r > len(grid)-1 or adj_c < 0 or adj_c > len(grid[r])-1:
                continue
            else:
                if not grid[adj_r][adj_c].isalnum() and grid[adj_r][adj_c] != '.':
                    print(f'{val} adjacent to symbol')
                    if grid[adj_r][adj_c] == '*':
                        return True, [adj_r, adj_c]
                    else:
                        return True, [] 
    return False, []

def getID(_coord, _dict):
    for key in _dict.keys():
        if _dict[key] == _coord:
            return key
        else:
            continue
    return None

if __name__ == '__main__':
    input_lines = parseInput()
    new_input_lines = []
    for line in input_lines:
        new_input_lines.append(processInput(line))
    part_sum = 0 
    tracking = []
    ast_coord_dict = {}
    ast_val_dict = {}
    _id = 0
    for r, row in enumerate(new_input_lines):
        for v, val in enumerate(row):
            if val.isalnum() and [r, v] not in tracking:
                # print(f'Found a part number: {val} at v: {v}')
                coords_list = getCharCoords(r, v, new_input_lines)
                success_bool, ast_coord =  adjacentToSymbol(coords_list, new_input_lines, val)
                if success_bool:
                    num = []
                    for coords in coords_list:
                        r, c = coords
                        num.append(new_input_lines[r][c])
                        tracking.append(coords)
                    part_sum += int(''.join(num))
                    if ast_coord: 
                        if ast_coord not in ast_coord_dict.values():
                            _id += 1
                            ast_coord_dict[_id] = ast_coord
                            ast_val_dict[_id] = [int(''.join(num))]
                        else:
                            id_for_ast = getID(ast_coord, ast_coord_dict)
                            ast_val_dict[id_for_ast].append(int(''.join(num)))
                else:
                    print(f'{val} not adjacent to symbol')

    print(ast_val_dict)
    prod_sum = 0
    for key in ast_val_dict.keys():
        if len(ast_val_dict[key]) == 2:
            prod_sum += np.prod(ast_val_dict[key])
    print(part_sum)
    print(prod_sum)