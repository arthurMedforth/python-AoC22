from parseInput import *

input_lines = parseInput()
# Develop recursive function that loops through contents of a file (after encountering ls _)

# cd _ means you will set an active folder and add it to a dictionary
# ls means loop through following entries (entering new recursion level if encoutering dir but adding to a contents count otherwise)
# cd .. means you can return a total

def contentsRecursion(contents_dict, incoming_dir,incoming_line_num,sum_dir):
    dir_found = False
    for line_num, line in enumerate(input_lines):
 
        if line[0] == "$": # We know that this is a command

            if line[1:] == ['cd', '..']:
                if dir_found:
                    # we can return from this recursion level
                    return int(contents_dict[current_key]), contents_dict, sum_dir
                else: 
                    continue

            elif line[1:] == ['ls']:
                # Following lines are contents for the current directory
                continue
            else:
 
                if line[2] == incoming_dir and line_num >= incoming_line_num:
                    # Add to dictionary and set as active directory line[2]
                    print("NEW DICT IS", line[2])
                    current_key = len(contents_dict.keys())+1
                    contents_dict[current_key] = 0
                    current_dir = line[2]
                    dir_found = True
                else:
                    if dir_found:
                        dir_found = False
                    else:
                        continue
        else: # we know that this is a directory listing
            if dir_found:
                if line[0] == "dir": # it is a directory
                    # Enter new recursion layer
                    num, contents_dict, sum_dir = contentsRecursion(contents_dict, line[1],line_num, sum_dir)
                    if num <= 100000:
                        sum_dir += num
                    contents_dict[current_key] += num
                else: # It must be a file
                    contents_dict[current_key] += int(line[0]) # Add to the total


    return contents_dict[current_key], contents_dict, sum_dir
                    
contents_dict = {}
num, contents_dict, sum_dir = contentsRecursion(contents_dict,"/",0,0)

print("Answer is", sum_dir)
print(contents_dict)


# GREAT TIME TO START LEARNING ABOUT CLASSES