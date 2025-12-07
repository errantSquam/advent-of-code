import os 

input_file = open(os.getcwd() + '/input/input.txt', 'r').read().split('\n')
sample_input_file = open(os.getcwd() + '/input/sample_input.txt', 'r').read().split('\n')

test_input_file = open(os.getcwd() + '/input/test_input.txt', 'r').read().split('\n')

def parse_input(input):
    input = [list(i) for i in input if [j for j in list(i) if j != '.'] != []]
    #remove useless strings
    return input

def print_input(input):
    print('\n'.join([''.join(i) for i in input]))

def split_tachyon_1(input):
    input = parse_input(input)

    print_input(input)
    
    starting_location = input[0].index('S')
    beam_array = [starting_location]

    times_split = 0
    
    for row_index in range(1, len(input)):
        row = input[row_index]

        beam_array.sort()
        beam_array = list(set(beam_array))

        temp_beam_array = beam_array[:]

        print("\n")

        for beam_index in beam_array:
            #print(f"Symbol is {row[beam_index]} at index {beam_index}")
            if row[beam_index] == ".":
                input[row_index][beam_index] = "|"

            elif row[beam_index] == '^':
                #print(f"Splitting {beam_index} to {beam_index -1} and {beam_index + 1}")
                temp_beam_array.remove(beam_index)
                times_split +=1 

                if beam_index - 1 >= 0 and input[row_index][beam_index-1] != "|":
                    input[row_index][beam_index-1] = "|"
                    temp_beam_array.append(beam_index - 1)
                if beam_index + 1 < len(row) and input[row_index][beam_index+1] != "|":
                    input[row_index][beam_index+1] = "|"
                    temp_beam_array.append(beam_index + 1)
                
        beam_array = temp_beam_array
        print_input(input)
    print(f"Tachyon beams split {times_split} times.")

#split_tachyon_1(sample_input_file)
split_tachyon_1(input_file)