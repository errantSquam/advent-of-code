import os 
input_file = open(os.getcwd() + '/input/input.txt', 'r').read().split('\n')
sample_input_file = open(os.getcwd() + '/input/sample_input.txt', 'r').read().split('\n')

def standardize_char(array_char):
    if array_char == '@':
        return 1
    else:
        return 0

def print_adjacency_tuple(adj_tuple):
    if adj_tuple[0] == 1 and adj_tuple[1] <4:
        return "x"
    elif adj_tuple[0] == 1:
        return "@"
    else:
        return "."

def removed_tuple(adj_tuple):
    if adj_tuple[0] == 1 and adj_tuple[1] <4:
        return 0
    elif adj_tuple[0] == 1:
        return 1
    else:
        return 0


def get_rolls_1(input):
    
    roll_array = [[standardize_char(roll) for roll in list(row)] for row in input]

    adjacency_matrix = [[[roll, 0] for roll in row] for row in roll_array]

    for col_index in range(len(roll_array)):
        for row_index in range(len(roll_array[0])):    

            if adjacency_matrix[col_index][row_index][0] == 1:
                #If contains roll
                for i in range(-1, 1+1):
                    for j in range(-1, 1+1):

                        #Don't add to yourself!
                        if i == 0 and j == 0:
                            continue
                        temp_col_index = col_index + i
                        temp_row_index = row_index + j

                        #Range checks
                        if (temp_col_index < 0 or temp_col_index >= len(roll_array) \
                        or temp_row_index < 0 or temp_row_index >= len(roll_array[0])):
                            continue

                        adjacency_matrix[temp_col_index][temp_row_index][1] +=1

    valid_rolls_array = [[roll for roll in row if roll[0] == 1 and roll[1] <4] for row in adjacency_matrix]

    valid_rolls_amount = sum([sum([i[0] for i in row]) for row in valid_rolls_array])

    valid_rolls_print = '\n'.join([''.join([print_adjacency_tuple(roll) for roll in row]) for row in adjacency_matrix])

    print(valid_rolls_print)


    print(f"There are {valid_rolls_amount} roll(s) of paper that can be accessed with a forklift.")

def get_removable_rolls(roll_array):
    adjacency_matrix = [[[roll, 0] for roll in row] for row in roll_array]

    for col_index in range(len(roll_array)):
        for row_index in range(len(roll_array[0])):    

            if adjacency_matrix[col_index][row_index][0] == 1:
                #If contains roll
                for i in range(-1, 1+1):
                    for j in range(-1, 1+1):

                        #Don't add to yourself!
                        if i == 0 and j == 0:
                            continue
                        temp_col_index = col_index + i
                        temp_row_index = row_index + j

                        #Range checks
                        if (temp_col_index < 0 or temp_col_index >= len(roll_array) \
                        or temp_row_index < 0 or temp_row_index >= len(roll_array[0])):
                            continue

                        adjacency_matrix[temp_col_index][temp_row_index][1] +=1

    valid_rolls_array = [[roll for roll in row if roll[0] == 1 and roll[1] <4] for row in adjacency_matrix]

    valid_rolls_amount = sum([sum([i[0] for i in row]) for row in valid_rolls_array])

    valid_rolls_print = '\n'.join([''.join([print_adjacency_tuple(roll) for roll in row]) for row in adjacency_matrix])

    print(f"Remove {valid_rolls_amount} roll(s) of paper:")

    print(valid_rolls_print)

    return ([[removed_tuple(roll) for roll in row] for row in adjacency_matrix], valid_rolls_amount)



def get_rolls_2(input):
    roll_array = [[standardize_char(roll) for roll in list(row)] for row in input]
    removed_rolls = 0

    can_remove = True 

    removed_result = get_removable_rolls(roll_array)

    while can_remove:
        if removed_result[1] == 0:
            can_remove = False
            break

        removed_rolls += removed_result[1]
        removed_result = get_removable_rolls(removed_result[0])

    print(f"A total of {removed_rolls} rolls can be removed.")

#get_rolls_1(sample_input_file)
#get_rolls_1(input_file)

#get_rolls_2(sample_input_file)
get_rolls_2(input_file)