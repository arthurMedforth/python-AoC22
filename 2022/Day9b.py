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

def moveRope(rope,counter):
    current_knot = rope[counter - 1].copy()
    next_knot = rope[counter].copy()
    horiz_diff = abs(current_knot[0]-next_knot[0])
    vert_diff = abs(current_knot[1]-next_knot[1])
    new_next_knot = next_knot.copy()
    modulus = sqrt(vert_diff**2 + horiz_diff**2)
    if modulus >= 2:
        if current_knot[0]!=next_knot[0] and current_knot[1]!=next_knot[1]:
            # Diagonal move required
            if current_knot[0]-next_knot[0] < 0 and current_knot[1]-next_knot[1] < 0: # Tail is further to right than Head and further up
                next_knot[0] -= 1
                next_knot[1] -= 1
            elif current_knot[0]-next_knot[0] < 0 and current_knot[1]-next_knot[1] > 0: # Tail is further to right than Head and further down
                next_knot[0] -= 1   
                next_knot[1] += 1
            elif current_knot[0]-next_knot[0] > 0 and current_knot[1]-next_knot[1] < 0: # Tail is further to left than Head and further up
                next_knot[0] += 1
                next_knot[1] -= 1
            elif current_knot[0]-next_knot[0] > 0 and current_knot[1]-next_knot[1] > 0: # Tail is further to left than Head and further down
                next_knot[0] += 1
                next_knot[1] += 1
            else:
                raise ValueError("Something has gone wrong")

        else:
            if horiz_diff >= 2:
                if current_knot[0]-next_knot[0] < 0: # Tail is further to right than Head
                    next_knot[0] -= 1
                elif current_knot[0]-next_knot[0] > 0: # Head is further to left than Tail
                    next_knot[0] += 1
                else:
                    raise ValueError("Shouldn't land here because the modulus is less than 2 and horiz_diff > 2")
            elif vert_diff >= 2:
                if current_knot[1]-next_knot[1] < 0: # Tail is further up than Head
                    next_knot[1] -= 1
                elif current_knot[1]-next_knot[1] > 0: # Head is further up than Tail
                    next_knot[1] += 1
                else:
                    raise ValueError("Shouldn't land here because the modulus is less than 2 and vert_diff > 2")
                
    rope[counter - 1] = current_knot
    rope[counter] = next_knot
    if counter + 1 != len(rope):
        rope = moveRope(rope,counter+1)
    return rope

if __name__ == "__main__":
    input_lines = parseInput()
    visited_cords=[]
    visited_cords.append([0,0])
    rope = []
    [rope.append([0,0]) for i in range(10)]
    pre_move_tail_pos = rope[-1]
    for instruction in input_lines:
        direction = instruction[0]
        count = int(instruction[1])
        for i in range(count):
            # Move Head
            if direction == 'R':
                rope[0][0] += 1
            elif direction == 'L':
                rope[0][0] -= 1
            elif direction == 'U':
                rope[0][1] += 1
            elif direction == 'D':
                rope[0][1] -= 1
            else:
                raise(ValueError("This direction doesn't exist"))
            rope = moveRope(rope,1)
            # Has the tail_pos changed as a result of the head move?
            if rope[-1] != pre_move_tail_pos and not visitedSpace(rope[-1],visited_cords):
                # If YES --> we need to add the current position to our visited dirs list
                print("On instruction: " + str(instruction))
                visited_cords.append(rope[-1])
                print(rope[-1])
            # Now set the new tail_pos to the output of the function call
            pre_move_tail_pos = rope[-1].copy()

print(len(visited_cords))