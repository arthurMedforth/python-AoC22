from parseInput import parseInput
from word2number import w2n

def partA(input_lines):
    sum_of = 0
    for line in input_lines:
        inds = [char for char in line if char.isnumeric()]
        first_and_last = [inds[0], inds[-1]]
        sum_of += int(''.join(map(str,first_and_last)))
    return sum_of

def find_lowest(found_wordnums,str_length, pos):
    if pos == 'first':
        lowest_ind = str_length
        lowest_ind_copy = 0
        for i, tuple in enumerate(found_wordnums):
            if tuple[1] <= lowest_ind:
                lowest_ind = tuple[1]
                lowest_ind_copy = i
        return lowest_ind_copy
    else:
        highest_ind = 0
        highest_ind_copy = 0
        for i, tuple in enumerate(found_wordnums):
            if tuple[1] >= highest_ind:
                highest_ind = tuple[1]
                highest_ind_copy = i
        return highest_ind_copy



if __name__ == "__main__":
    input_lines = parseInput()  
    # partA(input_lines)
    word_nums = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9    }
    sum_2 = 0
    for line in input_lines:
        line_str = ''.join(map(str,line))    
        found_wordnums = []   
        
        for i, word_num in enumerate(list(word_nums.keys())):
            start = 0 
            while start < len(line_str):
                index = line_str.find(word_num, start)
                if index == -1:
                    break
                found_wordnums.append((word_num, index))
                start = index + 1

        found_nums = [(int(char), i) for i, char in enumerate(line) if char.isnumeric()]
        if len(found_nums) == 0:
            first_num = word_nums[found_wordnums[find_lowest(found_wordnums, len(line_str)-1, 'first')][0]]
            last_num = word_nums[found_wordnums[find_lowest(found_wordnums, len(line_str)-1, 'last')][0]]
        elif len(found_wordnums) == 0:
            first_num = found_nums[0][0]
            last_num = found_nums[-1][0]
        else:
            if found_wordnums[find_lowest(found_wordnums, len(line_str)-1, 'first')][1] < found_nums[0][1]:
                first_num = word_nums[found_wordnums[find_lowest(found_wordnums, len(line_str)-1, 'first')][0]]
            else: 
                first_num = found_nums[0][0]

            if found_wordnums[find_lowest(found_wordnums, len(line_str)-1, 'last')][1] > found_nums[-1][1]:
                last_num = word_nums[found_wordnums[find_lowest(found_wordnums, len(line_str)-1, 'last')][0]]
            else:
                last_num = found_nums[-1][0]
        
        num = str(first_num) + str(last_num)
        print(num)
        sum_2 += int(num)
    
    print(sum_2)
    