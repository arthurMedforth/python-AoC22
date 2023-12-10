from parseInput import parseInput

# def readPipe(_char):
#     if _char == 'S':

#     elif _char == '|':

#     elif _char == '-':

#     elif _char == 'L':
        
#     elif _char == 'J':
        
#     elif _char == 'Z':
        
#     elif _char == 'F':
        
#     elif _char == '.':
#     else:
#         raise ValueError(f'char: {_char} not a valid character for this code problem')

def findCoords(_char, grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == _char:
                return r,c
            else:
                continue

    return None, None

if __name__ == '__main__':
    grid = parseInput()
    # Find S
    r, c = findCoords('S', grid)
    print([r, c])