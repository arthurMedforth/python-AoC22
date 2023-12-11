from parseInput import parseInput

def findCoords(_char, grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == _char:
                return [r,c]
            else:
                continue
    return [None, None]

def getValidChars(char):
    char_list = ['|', '-', 'L', 'J', '7', 'F']
    # if char == '|':
    #     char_list.remove('-')
    # elif char == '-':
    #     char_list.remove('|')
    # elif char == 'L':
    #     char_list.remove('J')
    # elif char == 'J':
    #     char_list.remove('L')
    # elif char == '7':
    #     char_list.remove('F')
    # elif char == 'F':
    #     char_list.remove('7')
    # else:
    #     raise ValueError(f'char: {char} not a valid character for this code problem')
    
    return char_list

def pathFind(coord, moves, grid):
    gotBack = False
    r_pos, c_pos = coord
    moves.append([r_pos, c_pos])
    curr_char = grid[r_pos][c_pos]
    OK_chars = getValidChars(curr_char)
    adj_coords = [[r_pos, c_pos-1],[r_pos-1, c_pos],[r_pos+1, c_pos],[r_pos, c_pos+1]]
    for adj_coord in adj_coords:
        r, c = adj_coord
        if not (r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[r]) - 1):
            new_char = grid[r][c]
            if new_char == '7'  and not ([r_pos, c_pos] == [r+1, c] or ([r_pos, c_pos] == [r, c-1]) and curr_char != '-'):
                continue
            elif new_char == 'F' and not ([r_pos, c_pos] == [r+1, c] or ([r_pos, c_pos] == [r, c+1]) and curr_char != '-'):
                continue
            elif new_char == 'L' and not ([r_pos, c_pos] == [r-1, c] or ([r_pos, c_pos] == [r, c+1] and curr_char not in '|')):
                continue
            elif new_char == 'J' and not ([r_pos, c_pos] == [r-1, c] or ([r_pos, c_pos] == [r, c-1] and curr_char != '|')):
                continue
            elif new_char == '|' and not ([r_pos, c_pos] == [r-1, c] or [r_pos, c_pos] == [r+1, c]):
                continue
            elif new_char == '-' and not ([r_pos, c_pos] == [r, c-1] or [r_pos, c_pos] == [r, c+1]):
                continue
            else:
                print('Think the new char could be valid')

            if new_char == 'S' and len(moves) > 1:
                gotBack = True
                return True, moves
            else:
                if new_char != '.' and new_char in OK_chars and [r, c] not in moves:
                    gotBack, moves = pathFind([r, c], moves, grid)
                    if gotBack:
                        return True, moves
                    else:
                        moves.pop(-1)
    return False, moves
                
if __name__ == '__main__':
    grid = parseInput()
    # Initialise position at S
    r_pos, c_pos = findCoords('S', grid)
    curr_char = 'S'
    # Look all around
    adj_coords = [[r_pos, c_pos-1],[r_pos-1, c_pos],[r_pos+1, c_pos],[r_pos, c_pos+1]]
    moves = []
    for adj_coord in adj_coords:
        r, c = adj_coord
        if not (r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[r]) - 1):
            new_char = grid[r][c]
            if new_char == '7'   and not (([r_pos, c_pos] == [r+1, c]) or ([r_pos, c_pos] == [r, c-1] and curr_char in ['-','L','F'])):
                continue
            elif new_char == 'F' and not (([r_pos, c_pos] == [r+1, c]) or ([r_pos, c_pos] == [r, c+1] and curr_char in ['-','J','7'])):
                continue
            elif new_char == 'L' and not (([r_pos, c_pos] == [r-1, c]) or ([r_pos, c_pos] == [r, c+1] and curr_char in ['-','7','J'])):
                continue
            elif new_char == 'J' and not (([r_pos, c_pos]) == [r-1, c] or ([r_pos, c_pos] == [r, c-1] and curr_char in ['-','L','F'])):
                continue
            elif new_char == '|' and not ([r_pos, c_pos] == [r-1, c] or [r_pos, c_pos] == [r+1, c]):
                continue
            elif new_char == '-' and not ([r_pos, c_pos] == [r, c-1] or [r_pos, c_pos] == [r, c+1]):
                continue
            else:
                print('Think the new char could be valid')
            if new_char != '.':
                gotBack, moves = pathFind([r, c], moves, grid)
                if gotBack:
                    print(moves)
                    break
                else:
                    moves.pop(-1)
    if len(moves) % 2 == 0:
        answer = len(moves) // 2
    else:
        answer = len(moves) // 2

    print(answer+1)
