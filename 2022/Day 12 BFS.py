from parseInput import parseInput

def findChar(grid, char):
    coordinates = [[i, j] for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == char]
    return coordinates[0] if coordinates else None

def findMultiChar(grid, char):
    coords = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == char:
                coords.append([i,j])
    return coords

def getAdjNodes(curr_node_pos, grid):
    curr_row = curr_node_pos[0] 
    curr_col = curr_node_pos[1] 
    adj_nodes = [[curr_row,curr_col+1],[curr_row,curr_col-1],[curr_row+1,curr_col],[curr_row-1,curr_col]]
    if curr_row == 0:
        adj_nodes.pop(3)
    elif curr_row == len(grid)-1:
        adj_nodes.pop(2)
    else:
        adj_nodes = adj_nodes

    if curr_col == 0:
        adj_nodes.pop(1)
    elif curr_col == len(grid[0])-1:
        adj_nodes.pop(0)
    else:
        adj_nodes = adj_nodes
    return adj_nodes 
        
def isViableNode(adj_node_row, adj_node_col, curr_node_row, curr_node_col, grid):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if grid[adj_node_row][adj_node_col] == 'E':
        new_char = 'z'
    else:
        new_char = grid[adj_node_row][adj_node_col]
    if grid[curr_node_row][curr_node_col] == 'S':
        curr_char = 'a'
    else:
        curr_char = grid[curr_node_row][curr_node_col]
    diff = alphabet.rfind(new_char) - alphabet.rfind(curr_char)
    if diff > 1:
        viable_bool = False
    else:
        viable_bool = True
    return viable_bool

def BFS(grid, start_pos):
    queue = []
    visited = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
    queue.insert(0, start_pos)
    visited[start_pos[0]][start_pos[1]] = True
    found = False
    end_coords = findChar(grid, 'E')
    parent = {}
    while queue:
        curr_node_pos = queue[-1]
        if curr_node_pos == end_coords:
            found = True
        adj_nodes = getAdjNodes(curr_node_pos, grid)
        for node in adj_nodes:
            if not visited[node[0]][node[1]] and isViableNode(node[0],node[1],curr_node_pos[0],curr_node_pos[1],grid):
                queue.insert(0, node)
                visited[node[0]][node[1]] = True
                parent[tuple(node)] = tuple(curr_node_pos)
        queue.pop(-1)
    return parent

def reconstruct_path(start, end, parent):
    path = [end]
    while path[-1] != start:
        try:
            path.append(parent[tuple(path[-1])])  # Convert to tuple before using as a key
        except:
            return None
    path.reverse()
    return path

if __name__ == "__main__":
    grid = parseInput()
    start_coords = findChar(grid, 'S')
    end_coords = findChar(grid, 'E')
    all_start_coords = findMultiChar(grid, 'a')
    all_start_coords.append(start_coords)
    potentials = []
    # PART 1
    # parent = BFS(grid, start_coords)
    # shortest_path = reconstruct_path(tuple(start_coords), tuple(end_coords), parent)
    # print(len(shortest_path)-1)
    # PART 2
    for coords in all_start_coords:
        parent = BFS(grid, coords)
        shortest_path = reconstruct_path(tuple(coords), tuple(end_coords), parent)
        if shortest_path == None:
            continue
        else:
            potentials.append(len(shortest_path)-1)
    print(min(potentials))