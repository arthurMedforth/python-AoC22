from parseInput import parseInput

def isLitPixel(X, curr_cycle, list_of_lit_pix_indices,bools):
    # is current cycle (position of CRT draw) within range of the Sprite
    spritePix1 = X - 1
    spritePix2 = X 
    spritePix3 = X + 1
    if (spritePix1 == curr_cycle or spritePix2 == curr_cycle or spritePix3 == curr_cycle) and not bools[curr_cycle]:
        list_of_lit_pix_indices.append(curr_cycle)
        bools[curr_cycle] = True
    return list_of_lit_pix_indices,bools

def newRow(happened, cycle_number, list_of_lit_pix_indices, bools, main_list):
    if cycle_number == 40:
        happened += 1
        main_list.append(list_of_lit_pix_indices)
        bools = [False for i in range(total_cycles)]
        list_of_lit_pix_indices = []
        cycle_number = 0
    
    return happened, cycle_number, list_of_lit_pix_indices, bools, main_list

if __name__ == "__main__":
    input_lines = parseInput()
    cycle_number = 0
    count = 0
    list_of_lit_pix_indices = []
    X = 1
    rows = [1,2,3,4,5,6]
    main_list = []
    happened = 0
    row_ind_vals = [39, 79, 119, 159, 199, 239]
    row_ind_vals_bools = [False, False, False, False, False]
    total_cycles = sum(instruction[0] == "noop" for instruction in input_lines) + sum(instruction[0] == "addx" for instruction in input_lines)*2
    bools = [False for i in range(total_cycles)]
    while cycle_number < total_cycles:
        curr_line = input_lines[count]
        if curr_line[0] == "noop":
            list_of_lit_pix_indices,bools = isLitPixel(X, cycle_number, list_of_lit_pix_indices, bools)
            cycle_number += 1
            happened, cycle_number, list_of_lit_pix_indices, bools, main_list = newRow(happened, cycle_number, list_of_lit_pix_indices, bools, main_list)
            list_of_lit_pix_indices,bools = isLitPixel(X, cycle_number, list_of_lit_pix_indices, bools)
        else: 
            list_of_lit_pix_indices,bools = isLitPixel(X, cycle_number, list_of_lit_pix_indices, bools)
            cycle_number += 1
            happened, cycle_number, list_of_lit_pix_indices, bools, main_list = newRow(happened, cycle_number, list_of_lit_pix_indices, bools, main_list)
            list_of_lit_pix_indices,bools = isLitPixel(X, cycle_number, list_of_lit_pix_indices, bools)
            cycle_number += 1
            happened, cycle_number, list_of_lit_pix_indices, bools, main_list = newRow(happened, cycle_number, list_of_lit_pix_indices, bools, main_list)
            X += int(curr_line[1])
            list_of_lit_pix_indices,bools = isLitPixel(X, cycle_number, list_of_lit_pix_indices, bools)

        if happened == 6:
            break
        else:
            count += 1

    CRT_row = [' ' for i in range(40)]
    CRT = []
    for list_of_pixels in main_list:
        for el in list_of_pixels:
            for i in range(len(CRT_row)):
                if i == el:
                    CRT_row[i] = "#"
                    break
        CRT.append(CRT_row)
        CRT_row = [' ' for i in range(40)]
            
    for el in CRT:
        print(''.join(el))