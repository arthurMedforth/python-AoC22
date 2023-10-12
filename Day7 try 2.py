from parseInput import *

input_lines = parseInput()

class Directory:
    def __init__(self, name):
        self.name = name
        self.file_sizes = []
        self.file_names = []
        self.sub_dirs = []
        self.parent = ''

    def give_directory_name(self):
        print('This is directory '  + self.name)

    def add_file(self, file_size, file_name):
        self.file_sizes.append(int(file_size))
        self.file_names.append(file_name)

    def add_sub_dir(self, sub_dir_name):
        self.sub_dirs.append(sub_dir_name)

    def sum_files(self):
        return sum(self.file_sizes)


def dir_already_exists(name, parent, dirs):
    exists_flag = False
    for obj in dirs:
        if obj.name == name and obj.parent == parent:
            exists_flag = True
            break
        else:
            continue
    
    return exists_flag

base_dir = Directory('/')
dirs = [base_dir]

counter = 0
while counter < len(input_lines):
    current_line = input_lines[counter]
    if current_line[1] == 'cd' and current_line[2] != '..':
        parent = current_line[2]
        counter = counter + 1
        continue
    if current_line[0] == 'dir' and not dir_already_exists(current_line[1],parent,dirs):
        dirs.append(Directory(current_line[1]))
        dirs[-1].parent = parent

    counter = counter + 1

counter = 1
visited_dirs_stack = []
current_directory = [obj if obj.name == '/' else None for obj in dirs]
current_directory = current_directory[0]
visited_dirs_stack.append(current_directory)
while counter < len(input_lines):
    current_line = input_lines[counter]
    if current_line[0] == '$' and current_line[1] == 'cd' and current_line[2] != '..':
        for obj in dirs:
            if obj.name == current_line[2] and obj.parent == visited_dirs_stack[-1].name:
                current_directory = obj
                visited_dirs_stack.append(current_directory)
                break
            else:
                continue
    elif current_line[0] == '$' and current_line[1] == 'ls':
        counter = counter + 1 
        continue
    elif current_line[0] != '$':
        if current_line[0] == 'dir':
            current_directory.add_sub_dir(current_line[1])
        else:
            current_directory.add_file(current_line[0], current_line[1])
    else: # we must be backing out
        #  Go to previous layer
        visited_dirs_stack.pop(-1)

    counter = counter + 1


# for obj in dirs:
#     print('Directory ' + obj.name + ' has the following')
#     print(obj.sub_dirs)
#     print(obj.file_names)
#     print('parent is '+ obj.parent)
#     print('-----------')

def sum_files(obj,dirs):
    current_level_files_total = obj.sum_files()
    for name in obj.sub_dirs:
        for obj_iter in dirs:
            if obj_iter.name == name and obj_iter.parent == obj.name:
                sub_obj = obj_iter
                break
        lower_level_files_total = sum_files(sub_obj,dirs)
        current_level_files_total = current_level_files_total + lower_level_files_total
    return current_level_files_total

def get_answer(dirs):
    rolling_sum = 0 
    for obj in dirs:
        current_sum = sum_files(obj,dirs) 
        if current_sum <= 100000:
            rolling_sum = rolling_sum + current_sum
        else:
            continue

    return rolling_sum

def total_for_single_dir(name, parent, dirs):
    for element in dirs:
        if name == element.name and parent == element.parent:
            print(element.sub_dirs)
            answer = sum_files(element,dirs)
            break

    return answer

print(get_answer(dirs))
# print(total_for_single_dir('fwdwq','gwlwp',dirs))

# name_parent_combos = []
# for obj in dirs:
#     combo = [obj.name,obj.parent]
#     name_parent_combos.append(combo)

# for i, element in enumerate(name_parent_combos):
#     for j, new_el in enumerate(name_parent_combos):
#         if element == new_el and i!=j:
#             print(element)

# print(len(name_parent_combos))
# print(len)

# for obj in dirs:
#     if obj.name == 'qzgsswr':
#         print('hello')


# for obj in dirs:
#     if obj.name == obj.parent:
#         print('happend')
