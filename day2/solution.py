import os 
input_file = open(os.getcwd() + '/input.txt', 'r').read().split(',')
sample_input_file = open(os.getcwd() + '/sample_input.txt', 'r').read().split(',')
sample_array = ["11-22"]

def check_invalid_id_2(id):
    for window_len in range(1, len(id)//2 + 1):
            

            if len(id) % (window_len) != 0:
                continue

            substring = id[0:window_len]

            repetitions = 1

            isRepeated = True
            while window_len * (repetitions + 1) <= len(id):
                start_index = window_len*(repetitions)
                end_index = start_index + window_len
                temp_substring = id[start_index: end_index]
                if temp_substring != substring:
                    isRepeated = False 
                    break 
                repetitions += 1

            if isRepeated:
                return True
            
    return False

def get_invalid_id_2(input_file):

    invalid_id_array = []

    for id_range in input_file:
        first_id = int(id_range.split("-")[0])
        last_id = int(id_range.split("-")[1])
        invalid_ids = []

        for id in range(first_id, last_id+1):
            if check_invalid_id_2(str(id)):
                invalid_ids.append(id)

        if len(invalid_ids) > 0:
            print(f"{id_range} has {len(invalid_ids)} invalid ID(s), {invalid_ids}")
        invalid_id_array += invalid_ids
            
    print("The rest of the ranges contain no invalid IDs.")

    invalid_id_array = [int(i) for i in invalid_id_array]

    print(f"Invalid IDs: {invalid_id_array}. ")
    print(f"Adding up all the invalid IDs produces {sum(invalid_id_array)}.")


def get_invalid_id_1(input_file):

    invalid_id_array = []

    for id_range in input_file:
        first_id = int(id_range.split("-")[0])
        last_id = int(id_range.split("-")[1])
        invalid_ids = []

        for id in range(first_id, last_id+1):
            id_string = str(id)
            if id_string[0:len(id_string)//2] == id_string[len(id_string)//2: len(id_string)]:
                invalid_ids.append(id_string)

        if len(invalid_ids) > 0:
            print(f"{id_range} has {len(invalid_ids)} invalid ID(s), {invalid_ids}")
        invalid_id_array += invalid_ids
            
    print("The rest of the ranges contain no invalid IDs.")

    invalid_id_array = [int(i) for i in invalid_id_array]

    print(f"Invalid IDs: {invalid_id_array}. ")
    print(f"Adding up all the invalid IDs produces {sum(invalid_id_array)}.")

#get_invalid_id_1(sample_input_file)
#get_invalid_id_1(input_file)

#get_invalid_id_2(sample_array)
#get_invalid_id_2(sample_input_file)           
get_invalid_id_2(input_file)

