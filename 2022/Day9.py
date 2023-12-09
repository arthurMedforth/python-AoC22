from parseInput import *
from math import sqrt

def visitedSpace(pos, visited_positions):
    found_bool = False
    for visited_pos in visited_positions:
        if pos ==visited_pos:
            found_bool = True 
            break
        else: 
            continue
    return found_bool

def moveTail(head_pos,tail_pos):
    horiz_diff = abs(head_pos[0]-tail_pos[0])
    vert_diff = abs(head_pos[1]-tail_pos[1])
    new_tail_pos = tail_pos.copy()
    modulus = sqrt(vert_diff**2 + horiz_diff**2)

    if modulus >= 2:
        if head_pos[0]!=tail_pos[0] and head_pos[1]!=tail_pos[1]:
            # Diagonal move required
            if head_pos[0]-tail_pos[0] < 0 and head_pos[1]-tail_pos[1] < 0: # Tail is further to right than Head and further up
                new_tail_pos[0] -= 1
                new_tail_pos[1] -= 1
            elif head_pos[0]-tail_pos[0] < 0 and head_pos[1]-tail_pos[1] > 0: # Tail is further to right than Head and further down
                new_tail_pos[0] -= 1   
                new_tail_pos[1] += 1
            elif head_pos[0]-tail_pos[0] > 0 and head_pos[1]-tail_pos[1] < 0: # Tail is further to left than Head and further up
                new_tail_pos[0] += 1
                new_tail_pos[1] -= 1
            elif head_pos[0]-tail_pos[0] > 0 and head_pos[1]-tail_pos[1] > 0: # Tail is further to left than Head and further down
                new_tail_pos[0] += 1
                new_tail_pos[1] += 1
            else:
                raise ValueError("Something has gone wrong")

        else:
            if horiz_diff >= 2:
                if head_pos[0]-tail_pos[0] < 0: # Tail is further to right than Head
                    new_tail_pos[0] -= 1
                elif head_pos[0]-tail_pos[0] > 0: # Head is further to left than Tail
                    new_tail_pos[0] += 1
                else:
                    raise ValueError("Shouldn't land here because the modulus is less than 2 and horiz_diff > 2")
            elif vert_diff >= 2:
                if head_pos[1]-tail_pos[1] < 0: # Tail is further up than Head
                    new_tail_pos[1] -= 1
                elif head_pos[1]-tail_pos[1] > 0: # Head is further up than Tail
                    new_tail_pos[1] += 1
                else:
                    raise ValueError("Shouldn't land here because the modulus is less than 2 and vert_diff > 2")

    return new_tail_pos

if __name__ == "__main__":
    input_lines = parseInput()

    visited_cords=[]
    visited_cords.append([0,0])

    # Both represent an x,y coord
    head_pos = [0,0]
    tail_pos = [0,0]
    for instruction in input_lines:
        direction = instruction[0]
        count = int(instruction[1])
        for i in range(count):
            # Move Head
            if direction == 'R':
                head_pos[0] += 1
            elif direction == 'L':
                head_pos[0] -= 1
            elif direction == 'U':
                head_pos[1] += 1
            elif direction == 'D':
                head_pos[1] -= 1
            else:
                raise(ValueError("This direction doesn't exist"))

            new_tail_pos = moveTail(head_pos,tail_pos)
            # Has the tail_pos changed as a result of the head move?
            if new_tail_pos != tail_pos and not visitedSpace(new_tail_pos,visited_cords):
                # If YES --> we need to add the current position to our visited dirs list
                print("On instruction: " + str(instruction))
                visited_cords.append(new_tail_pos)
                print(new_tail_pos)

            # Now set the new tail_pos to the output of the function call
            tail_pos = new_tail_pos.copy()

print(len(visited_cords))