class Directory:
    def __init__(self, name):
        self.name = name
        self.file_sizes = []
        self.sub_dirs = []

    def add_file(self, file_size):
        self.file_sizes.append(int(file_size))

    def add_sub_dir(self, sub_dir):
        self.sub_dirs.append(sub_dir)


def sum_files(obj, dirs):
    current_level_files_total = sum(obj.file_sizes)
    for sub_dir_name in obj.sub_dirs:
        for sub_dir in dirs:
            if sub_dir.name == sub_dir_name:
                lower_level_files_total = sum_files(sub_dir, dirs)
                current_level_files_total += lower_level_files_total
                break
    return current_level_files_total


def total_for_single_dir(name, dirs):
    for element in dirs:
        if name == element.name:
            answer = sum_files(element, dirs)
            break
    return answer


def parseInput(filename):
    with open(filename, 'r') as file:
        input_lines = [line.strip() for line in file]
    return input_lines


def main():
    input_lines = parseInput('input.txt')

    base_dir = Directory('/')
    dirs = [base_dir]

    for line in input_lines:
        parts = line.split()
        if parts[0] == 'dir':
            new_dir = Directory(parts[1])
            dirs[-1].add_sub_dir(parts[1])
            dirs.append(new_dir)
        else:
            dirs[-1].add_file(parts[0])

    answer = total_for_single_dir('/', dirs)
    print(answer)


if __name__ == "__main__":
    main()