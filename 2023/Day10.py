from parseInput import parseInput
import sys



def findCoords(_char, grid):
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if col == _char:
                return [r,c]
            else:
                continue
    return [None, None]

# def getNextpoint(r_pos, c_pos, grid, r_old, c_old, S_found, moves):
#     curr_char = grid[r_pos][c_pos]
#     if curr_char == 'S':
#         S_found += 1
#     # Look all around
#     adj_coords = [[r_pos, c_pos-1],[r_pos-1, c_pos],[r_pos+1, c_pos],[r_pos, c_pos+1]]
#     for adj_coord in adj_coords:
#         r, c = adj_coord
#         # Check that the coords are valid
#         if [r, c] == [r_old, c_old]:
#             continue
#         if not (r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[r]) - 1):
#             # Get the character that the coords correspond to
#             new_char = grid[r][c]
#             if new_char == '.' or [r,c] in moves:
#                 continue
#             if curr_char == '7': # new_char can only be to the left or below the curr char 
#                 if c == c_pos - 1 and new_char in ['-','L','F','S']:
#                     moves.append([r,c])
#                     # VALID
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)      
#                     if S_found != 2:
#                         moves.pop(-1)  
#                 elif r == r_pos + 1 and new_char in ['|','L','J','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)     
#                     if S_found != 2:
#                         moves.pop(-1)     
#                 else:
#                     continue
#             elif curr_char == 'F': # new_char can only be to the right or below the curr char 
#                 if c == c_pos + 1 and new_char in ['-','7','J','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)   
#                     if S_found != 2:
#                         moves.pop(-1)       
#                 elif r == r_pos + 1 and new_char in ['|','L','J','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)     
#                     if S_found != 2:
#                         moves.pop(-1)     
#                 else:
#                     continue 
#             elif curr_char == 'L': # new_char can only be to the right or above the curr char 
#                 if c == c_pos + 1 and new_char in ['-','J','7','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)    
#                     if S_found != 2:
#                         moves.pop(-1)      
#                 elif r == r_pos - 1 and new_char in ['|','7','F','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)       
#                     if S_found != 2:
#                         moves.pop(-1)   
#                 else:
#                     continue
#             elif curr_char == 'J': # new_char can only be to the left or above the curr char 
#                 if c == c_pos - 1 and new_char in ['-','L','F','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)  
#                     if S_found != 2:
#                         moves.pop(-1)        
#                 elif r == r_pos - 1 and new_char in ['|','7','F','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)   
#                     if S_found != 2:
#                         moves.pop(-1)       
#                 else:
#                     continue
#             elif curr_char == '|':
#                 # new_char can only be to above or below the curr char 
#                 if r == r_pos - 1 and new_char in ['|','7','F','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)   
#                     if S_found != 2:
#                         moves.pop(-1)       
#                 elif r == r_pos + 1 and new_char in ['|','L','J','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves) 
#                     if S_found != 2:
#                         moves.pop(-1)         
#                 else:
#                     continue
#             elif curr_char == '-':
#                 # new_char can only be to the left or right of the curr_char
#                 if c == c_pos - 1 and new_char in ['-','L','F','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)   
#                     if S_found != 2:
#                         moves.pop(-1)       
#                 elif c == c_pos + 1 and new_char in ['-','7','J','S']:
#                     # VALID
#                     moves.append([r,c])
#                     S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)    
#                     if S_found != 2:
#                         moves.pop(-1)      
#                 else:
#                     continue
#             elif curr_char == 'S':
#                 moves.append([r,c])
#                 S_found, moves = getNextpoint(r, c, grid, r_pos, c_pos, S_found, moves)   
#                 if S_found != 2:
#                         moves.pop(-1)  
#             else:
#                 raise ValueError(f'curr_char value {curr_char} invalid')
#         if S_found == 2:
#             return S_found, moves
#     return S_found, moves

def findConnectingPipes(r_pos,c_pos,grid):
    connecting_pipes = []
    curr_char = grid[r_pos][c_pos]
    # List of adjacent coords
    adj_coords = [[r_pos, c_pos-1],[r_pos-1, c_pos],[r_pos+1, c_pos],[r_pos, c_pos+1]]
    for adj_coord in adj_coords:
        r, c = adj_coord
        # Check that the coords are valid
        if not (r < 0 or c < 0 or r > len(grid) - 1 or c > len(grid[r]) - 1):
            new_char = grid[r][c]
            if curr_char == '7': # new_char can only be to the left or below the curr char 
                if c == c_pos - 1 and new_char in ['-','L','F','S']:
                    connecting_pipes.append([r,c])
                elif r == r_pos + 1 and new_char in ['|','L','J','S']:
                    connecting_pipes.append([r,c])
                else:
                    continue
            elif curr_char == 'F': # new_char can only be to the right or below the curr char 
                if c == c_pos + 1 and new_char in ['-','7','J','S']:
                    connecting_pipes.append([r,c])
                elif r == r_pos + 1 and new_char in ['|','L','J','S']:
                    connecting_pipes.append([r,c])
                else:
                    continue 
            elif curr_char == 'L': # new_char can only be to the right or above the curr char 
                if c == c_pos + 1 and new_char in ['-','J','7','S']:
                    connecting_pipes.append([r,c])
                elif r == r_pos - 1 and new_char in ['|','7','F','S']:
                    connecting_pipes.append([r,c])
                else:
                    continue
            elif curr_char == 'J': # new_char can only be to the left or above the curr char 
                if c == c_pos - 1 and new_char in ['-','L','F','S']:
                    connecting_pipes.append([r,c])
                elif r == r_pos - 1 and new_char in ['|','7','F','S']:
                    connecting_pipes.append([r,c])
                else:
                    continue
            elif curr_char == '|':
                # new_char can only be to above or below the curr char 
                if r == r_pos - 1 and new_char in ['|','7','F','S']:
                    connecting_pipes.append([r,c])
                elif r == r_pos + 1 and new_char in ['|','L','J','S']:
                    connecting_pipes.append([r,c])
                else:
                    continue
            elif curr_char == '-':
                # new_char can only be to the left or right of the curr_char
                if c == c_pos - 1 and new_char in ['-','L','F','S']:
                    connecting_pipes.append([r,c])
                elif c == c_pos + 1 and new_char in ['-','7','J','S']:
                    connecting_pipes.append([r,c])
                else:
                    continue
            else:
                raise ValueError(f'curr_char value {curr_char} invalid')
        if len(connecting_pipes) == 2:
            break
    return connecting_pipes

if __name__ == '__main__':
    grid = parseInput()
    # Initialise position at S
    r_pos, c_pos = findCoords('S', grid)
    connecting_pipes = [[75,52],[75,54]]
    # connecting_pipes = [[1,2],[2,1]]
    # connecting_pipes = [[3,0],[2,1]]
    found_s_again = False
    promising_connection = connecting_pipes[1]
    end_cond = connecting_pipes[0]
    moves = []
    while not found_s_again:
        moves.append(promising_connection)
        if promising_connection == end_cond:
            found_s_again == True
            break
        new_connecting_pipes = findConnectingPipes(promising_connection[0],promising_connection[1],grid)
        ind = new_connecting_pipes.index([r_pos,c_pos])
        if ind == 0:
            r_pos, c_pos = promising_connection
            promising_connection = new_connecting_pipes[1]
        elif ind == 1:
            r_pos, c_pos = promising_connection
            promising_connection = new_connecting_pipes[0]
        else:
            raise ValueError('Something went wrong')
    
    # Part 1
    print(len(moves)//2+1)

    # Part 2
    