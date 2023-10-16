from parseInput import *

input_lines = parseInput()

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.file_sizes = []
        self.file_names = []
        self.sub_dirs = []
        self.parent = parent
        self.direct_size = 0
        self.total_size = 0
        self.ID = 0
        self.parent_ID = 0

    def give_directory_name(self):
        print('This is directory '  + self.name)

    def add_file(self, file_size, file_name):
        self.file_sizes.append(int(file_size))
        self.file_names.append(file_name)

    def add_sub_dir(self, sub_dir_name):
        self.sub_dirs.append(sub_dir_name)

    def calc_direct_size(self):
        return sum(self.file_sizes)
    
    

def main():
    pass_unfinished = True
    count = 0
    all_directories = []
    dir_visit_ledger = []
    while pass_unfinished:
        current_line = input_lines[count]
        if current_line[0] == '$': # This line is a command
            if current_line[1] == 'cd' and current_line[2] != '..': # We are entering a new directory
                if current_line[2] == '/': # Parent doesn't exist
                    all_directories.append(Directory('/',''))
                    all_directories[-1].ID += len(all_directories)
                    dir_visit_ledger.append(all_directories[-1])
                else:
                    all_directories.append(Directory(current_line[2], dir_visit_ledger[-1].name))
                    all_directories[-1].parent_ID = dir_visit_ledger[-1].ID
                    all_directories[-1].ID += len(all_directories)
                    dir_visit_ledger.append(all_directories[-1])
            elif current_line[1] == 'cd' and current_line[2] == '..': # We are backing out
                dir_visit_ledger.pop(-1) # We need to backout a level so update ledger
            else: # We are listing the contents of the current directory @visited_dirs[-1]
                print('About to list the contents of directory ' + all_directories[-1].name)
        else: # This line is listing a directory or a file
            if current_line[0] == 'dir':
                all_directories[-1].add_sub_dir(current_line[1])
            else:
                all_directories[-1].add_file(current_line[0], current_line[1])

        if count == len(input_lines) - 1:
            pass_unfinished = False
        else:
            # Increment the counter
            count += 1 

    return all_directories

def sum_files(obj, dirs):
    current_level_files_total = obj.calc_direct_size()
    lower_level_files_total = 0
    for name in obj.sub_dirs:
        # if name == 'd':
        #     print('happening')

        for obj_iter in dirs:
            if obj_iter.name == name and obj_iter.parent_ID == obj.ID:
                lower_level_files_total = sum_files(obj_iter, dirs)
                current_level_files_total += lower_level_files_total
                break

    obj.total_size = current_level_files_total    
    return current_level_files_total


def get_answer_a(dirs):
    rolling_sum = 0 
    for obj in dirs:
        current_sum = sum_files(obj,dirs) 
        obj.total_size = current_sum
        if current_sum <= 100000:
            rolling_sum = rolling_sum + current_sum
        else:
            continue

    return rolling_sum

if __name__ == "__main__":
    all_directories = main()
    name_parent_combos = []
    for obj in all_directories:
        obj.total_size = sum_files(obj, all_directories)

    unused_space = 70000000 - all_directories[0].total_size
    diff_required = 30000000 - unused_space
    
    options = []
    for obj in all_directories:
        if obj.total_size >= diff_required:
            options.append(obj.total_size)
    
    print(min(options))

    # sum_root = 0
    # for line in input_lines:
    #     if line[0] != '$' and line[0] != 'dir':
    #         sum_root += int(line[0])


    # print(sum_root)
  
  
  
   # for obj in all_directories:
    #     size = sum_files(obj, all_directories)
    #     if obj.name == 'lddhdslh':
    #         print('look ohere')
    #     print('Directory '+ obj.name + ' is this big: ' + str(size))

